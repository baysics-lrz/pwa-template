import json
import os
from PIL import Image, ImageOps
from observations.models import get_municipal_via_coordinates, get_hexagon_via_coordinates, get_climate_station_via_coordinates

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webportal.settings")

import django

django.setup()

from observations.models import Municipal, ClimateStation, Hexagon
from django.contrib.gis.geos import Polygon, Point
from django.contrib.gis.gdal import DataSource, OGRGeometry
from observations.models import Category1, Category2, Category3, Category4

def parse_hexagons():
    res_list = []
    with open('geo_util/hexagons.txt', encoding='utf-8') as file:
        for line in file:
            line = line[:len(line) - 2]
            climate_station = json.loads(line)
            climate_station['geometry']['coordinates'] = climate_station['geometry']['coordinates'][0]
            for point in climate_station['geometry']['coordinates']:
                y = point[0]
                point[0] = point[1]
                point[1] = y
            res_list.append(climate_station)
    return res_list


def parse_climate_stations():
    res_list = []
    with open('geo_util/climatestations.txt', encoding='utf-8') as file:
        for line in file:
            line = line[:len(line) - 2]
            climate_station = json.loads(line)
            climate_station['geometry']['coordinates'] = climate_station['geometry']['coordinates'][0]
            for point in climate_station['geometry']['coordinates']:
                y = point[0]
                point[0] = point[1]
                point[1] = y
            res_list.append(climate_station)
    return res_list


def parse_municipals():
    res_list = []
    with open('geo_util/gemeinden.txt', encoding='utf-8') as file:
        for line in file:
            line = line[:len(line) - 2]
            municipals = json.loads(line)
            municipals['geometry']['coordinates'] = municipals['geometry']['coordinates'][0]
            for point in municipals['geometry']['coordinates']:
                y = point[0]
                point[0] = point[1]
                point[1] = y
            res_list.append(municipals)
    return res_list


def store_municipal_instance(bez_gem: str, bez_krs: str, bez_rbz: str, tile: str, geometry: list):
    polygon = Polygon(tuple(tuple(x) for x in geometry))
    new_municipal = Municipal(bez_gem=bez_gem, bez_krs=bez_krs, bez_rbz=bez_rbz, tile=tile, geometry=polygon)
    new_municipal.save()


def store_climate_station_instance(station_id: int, name: str, height: float, lat: float, lon: float, tile: str,
                                   geometry: list):
    polygon = Polygon(tuple(tuple(x) for x in geometry))
    new_climate_station = ClimateStation(station_id=station_id, name=name, height=height, lat=lat, lon=lon, tile=tile,
                                         geometry=polygon)
    new_climate_station.save()


def store_hexagon_instance(id: int, tile: str, geometry: list):
    polygon = Polygon(tuple(tuple(x) for x in geometry))
    new_hexagon = Hexagon(id=id, tile=tile, geometry=polygon)
    new_hexagon.save()


def store_everything_in_database():
    # check to not write Municipal geometries multiple times, which causes errors for new entries.
    # If we need to update the geometries we need to delte the table entries of the table in question (Municipal, ClimateStation, or Hexagon)
    if (Municipal.objects.all().count() == 0):
            municipals = parse_municipals()
            print('Storing municipals...')
            for mun in municipals:
                store_municipal_instance(bez_gem=mun['properties']['BEZ_GEM'], bez_krs=mun['properties']['BEZ_KRS'],
                                         bez_rbz=mun['properties']['BEZ_RBZ'], tile=mun['properties']['TILE'],
                                         geometry=mun['geometry']['coordinates'])
    else:
        print("Table Municipal already has entries.")

    if (ClimateStation.objects.all().count() == 0):
        climate_stations = parse_climate_stations()
        print('Storing climate-stations...')
        for cs in climate_stations:
            store_climate_station_instance(station_id=cs['properties']['station_id'], name=cs['properties']['name'],
                                           height=cs['properties']['height'], lat=cs['properties']['lat'],
                                           lon=cs['properties']['lng'], tile=cs['properties']['TILE'],
                                           geometry=cs['geometry']['coordinates'])
    else:
        print("Table ClimateStation already has entries.")

    if (Hexagon.objects.all().count() == 0):
        hexagons = parse_hexagons()
        print('Storing hexagons...')
        for hexa in hexagons:
            store_hexagon_instance(id=hexa['properties']['id'], tile=hexa['properties']['TILE'],
                                   geometry=hexa['geometry']['coordinates'])
    else:
        print("Table Hexagon already has entries.")

# checking the geometries of the observations and flipping them if necessary
# if the latitude is larger than the longitude for Bavarian entries the lat and long seem to be flipped
def check_point_geom():
    flip_lat_lon(Category1.objects.all(), "category1")
    flip_lat_lon(Category2.objects.all(), "Category2")
    flip_lat_lon(Category3.objects.all(), "category3")
    flip_lat_lon(Category4.objects.all(), "category4")


def flip_lat_lon(obs, typ):
    for o in obs:
        try:
            if (o.geom[0] >= o.geom[1]):
                o.geom = Point(o.geom[1],o.geom[0]) # flipp it
                print(o.geom, "flipped")
            o.save()
        except:
            print("exception while comparing lat lon in", typ)



def check_categoryX_dgm():
    #Please replace X with relevant Category
    categoryXs = CategoryX.objects.all()
    for categoryX in categoryXs:
        try:
            if (categoryX.Altitude_m is None):
                print("found categoryX without altitude")
                categoryX.Altitude_m = return_dgm_altitude(categoryX.Lat, categoryX.Lon)
                categoryX.save()
        except:
            print("couldn't set Altitude_m for categoryX")

def check_categoryX_mntrange():
    # Please replace X with relevant Category
    categoryXs = CategoryX.objects.all()
    for categoryX in categoryXs:
        try:
            if (categoryX.MountainRange is None or categoryX.MountainRange == ""):
                print("found categoryX without mountain range")
                categoryX.MountainRange = return_mnt_range(categoryX.Lat, categoryX.Lon)
                print(return_mnt_range(categoryX.Lat, categoryX.Lon))
                print(categoryX)
                categoryX.save()
        except:
            print("couldn't set mountain range for categoryX")

def return_mnt_range(lat, lon):
        try:
            p = OGRGeometry("Point("+str(lon) + " " + str(lat)+")") # create a OGR Geometry point from lon and lat
            # # example: p = OGRGeometry("Point(9.835 50.3629)")
            fp = "geo_util/mountainrange_poly.geojson"
            print(fp, p)
            ds = DataSource(fp) # load geojson as data source
            for layer in ds:  # load layer(s) from data source
                for feature in layer: # search features in loaded layer
                    if (feature.geom.contains(p)): # check if point is within a feature's geometry
                        print(("mountain range for lon:%s lat:%s is %sm") % (lat, lon, feature.get("NAME")))
                        return feature.get("NAME")
        except:
            print(("error while trying to fetch mountain range for lon:%s lat:%s") % (lon, lat))

def return_dgm_altitude(lat, lon):
    # lookup for altitude tiles (dgm)
    # <tilenumber>[left, right, bottom, top] (391 means tile 39 section 1)
    tiledict = {
        2:[9.39100,9.89100,50.32075,50.82075],
        3:[9.89100,10.39100,50.32075,50.82075],
        4:[10.39100,10.89100,50.32075,50.82075],
        5:[10.89100,11.39100,50.32075,50.82075],
        6:[11.39100,11.89100,50.32075,50.82075],
        7:[11.89100,12.39100,50.32075,50.82075],
        11:[8.89100,9.39100,49.82075,50.32075],
        12:[9.39100,9.89100,49.82075,50.32075],
        13:[9.89100,10.39100,49.82075,50.32075],
        14:[10.39100,10.89100,49.82075,50.32075],
        15:[10.89100,11.39100,49.82075,50.32075],
        16:[11.39100,11.89100,49.82075,50.32075],
        17:[11.89100,12.39100,49.82075,50.32075],
        18:[12.39100,12.89100,49.82075,50.32075],
        21:[8.89100,9.39100,49.32075,49.82075],
        22:[9.39100,9.89100,49.32075,49.82075],
        23:[9.89100,10.39100,49.32075,49.82075],
        24:[10.39100,10.89100,49.32075,49.82075],
        25:[10.89100,11.39100,49.32075,49.82075],
        26:[11.39100,11.89100,49.32075,49.82075],
        27:[11.89100,12.39100,49.32075,49.82075],
        28:[12.39100,12.89100,49.32075,49.82075],
        29:[12.89100,13.39100,49.32075,49.82075],
        33:[9.89100,10.39100,48.82075,49.32075],
        34:[10.39100,10.89100,48.82075,49.32075],
        35:[10.89100,11.39100,48.82075,49.32075],
        36:[11.39100,11.89100,48.82075,49.32075],
        37:[11.89100,12.39100,48.82075,49.32075],
        38:[12.39100,12.89100,48.82075,49.32075],
        392:[12.89100,13.39100,48.82075,49.07075],
        391:[12.89100,13.39100,49.07075,49.32075],
        40:[13.39100,13.89100,48.82075,49.32075],
        43:[9.89100,10.39100,48.32075,48.82075],
        44:[10.39100,10.89100,48.32075,48.82075],
        45:[10.89100,11.39100,48.32075,48.82075],
        46:[11.39100,11.89100,48.32075,48.82075],
        47:[11.89100,12.39100,48.32075,48.82075],
        48:[12.39100,12.89100,48.32075,48.82075],
        49:[12.89100,13.39100,48.32075,48.82075],
        50:[13.39100,13.89100,48.32075,48.82075],
        53:[9.89100,10.39100,47.82075,48.32075],
        54:[10.39100,10.89100,47.82075,48.32075],
        55:[10.89100,11.39100,47.82075,48.32075],
        56:[11.39100,11.89100,47.82075,48.32075],
        57:[11.89100,12.39100,47.82075,48.32075],
        58:[12.39100,12.89100,47.82075,48.32075],
        59:[12.89100,13.39100,47.82075,48.32075],
        62:[9.39100,9.89100,47.32075,47.82075],
        631:[9.89100,10.14100,47.32075,47.82075],
        632:[10.14100,10.39100,47.32075,47.82075],
        64:[10.39100,10.89100,47.32075,47.82075],
        651:[10.89100,11.14100,47.32075,47.82075],
        652:[10.14100,11.39100,47.32075,47.82075],
        661:[11.39100,11.64100,47.32075,47.82075],
        662:[11.64100,11.89100,47.32075,47.82075],
        67:[11.89100,12.39100,47.32075,47.82075],
        681:[12.39100,12.64100,47.32075,47.82075],
        682:[12.64100,12.89100,47.32075,47.82075],
        69:[12.89100,13.39100,47.32075,47.82075],
        73:[9.89100,10.39100,46.82075,47.32075]
    }


    found = False
    for t in tiledict:
        if ((float(lon) >= tiledict[t][0]) & (float(lon) <= tiledict[t][1])): # check lon for tile
            if ((float(lat) >= tiledict[t][2]) & (float(lat) <= tiledict[t][3])): # check lat
                found = True
                print(("coordinates lon:%s lat:%s within tile %s") % (lon, lat, t))
                try:
                    p = OGRGeometry("Point("+str(lon) + " " + str(lat)+")") # create a OGR Geometry point from lon and lat
                    # # example: p = OGRGeometry("Point(9.835 50.3629)")
                    fp = "geo_util/dgm/dgm_"+str(t)+".geojson"
                    print(fp, p)
                    ds = DataSource(fp) # load geojson as data source
                    for layer in ds:  # load layer(s) from data source
                        for feature in layer: # search features in loaded layer
                            if (feature.geom.contains(p)): # check if point is within a feature's geometry
                                print(("DGM Altitude for lon:%s lat:%s is %sm") % (lat, lon, feature.get("VALUE")))
                                return float(feature.get("VALUE"))
                except:
                    print(("error while trying to fetch altitude for lon:%s lat:%s") % (lon, lat))
    if (found is False):
        print("couldn't find matching tile")


from observations.views.util import create_thumbnail

def check_thumbs(observations):
    for obs in observations:
        try:
            if (obs.Photo is not None):
                if (os.path.isfile("media/" + str(obs.Photo))):
                    # if photo exists
                    thumbnailpath = str(obs.Photo).split("/")
                    thumbnailpath[-1] = str(obs.Photo).split("/")[-1].split(".")[0]+"_small.jpg"
                    thumbnailpath = "/".join(thumbnailpath)
                    thumbnailpath = "media/thumbnails/" + thumbnailpath
                    if (os.path.isfile(thumbnailpath)):
                        # has a thumbnail
                        pass
                    else:
                        # has no thumbnail
                        create_thumbnail(str(obs.Photo))
                        print("thumbnail created")
                else:
                    print("No photo on file path %s. Can't create thumbnail." % str(obs.Photo) )
        except:
            print("error while checking thumbnails")

def check_thumbnails():
    check_thumbs(Category1.objects.all())
    check_thumbs(Category2.objects.all())
    check_thumbs(Category3.objects.all())
    check_thumbs(Category4.objects.all())

def check_municipal_climatestation_hexagon(observations):
    for obs in observations:
        try:
            lat = float(obs.Lat)
            lon = float(obs.Lon)
            print("updating %s at lat:%s lon:%s" % (obs, lat, lon))
            obs.Municipal = get_municipal_via_coordinates(lat, lon)
            obs.Cell = get_hexagon_via_coordinates(lat, lon)
            obs.ClimateStation = get_climate_station_via_coordinates(lat, lon)
            obs.save()
            print("updated municipal/hexagon cell/climate station")
        except:
            print("couldn't set municipal/hexagon cell/climate station")

def check_places():
    check_municipal_climatestation_hexagon(Category1.objects.all())
    check_municipal_climatestation_hexagon(Category2.objects.all())
    check_municipal_climatestation_hexagon(Category3.objects.all())
    check_municipal_climatestation_hexagon(Category4.objects.all())

