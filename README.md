# Toolkit - Progressive Web App template for spatial data collection

This toolkit has been developed based on the BAYSICS web portal (Bavarian Citizen Science Information Platform for Climate Research and Science Communication, 2018 - 2024).

This toolkit provides the functionalities essential for citizen science projects involving the collection of spatial data: user registaration, contact form, FAQ page, data entry form and data list, offline interface, rankings and challanges features, data visualisation on a map, data export funtion through CSV and Excel, REST API, and a CMS page to be managed by superuser (admin).

For re-usage please take into account that this is the result of a research project, and any responsible re-use needs a prior security assessment of code and environment under the planned usage scenario.

The license and conditions for re-usage are available in LICENSE.txt.

Relevant publication: Batsaikhan et al. (2024): A Progressive Web App Template for Citizen Science Projects Involving Spatial Data Collection (https://doi.org/10.1109/e-Science58273.2023.10254925).


# Installation of prerequisites

Confirmed working environment: Debian 11 and Python 3.9

1. Install software-properties-common which provides an abstraction of the used apt repositories

- sudo apt install software-properties-common

2. Install python dependencies

- sudo apt install build-essential zlib1g-dev libncurses5-dev
libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev
libsqlite3-dev wget libbz2-dev

3. Check if python3 installed, otherwise install

- python3 --version

- sudo apt-get install python3


# a) Installation of necessary softwares and packages for the toolkit

1. Install postgreSQL and postgis (confirmed working version: PostgreSQL14)

- sudo apt-get install libpq-dev postgresql postgresql-client postgis postgresql-postgis 
  (PostgreSQL and PostGIS)

- sudo -u postgres psql 
  (check if it is correctly installed and you can login)

2. Install GDAL

- sudo apt-get install gdal-bin libgdal-dev

- gdalinfo --version 
  (check and note the gdal version)

3. Install packages necessary for virtual environment creation, Anaconda is recommended for OS Windows, Virtualenv is recommended for OS Mac

- sudo apt-get install python3-venv python3-pip

4. Install Nginx

- /usr/sbin/nginx -v 
  (check if nginx is installed)

- sudo apt-get install nginx 
  (install if not installed yet)

5. Install git

- sudo apt-get install git 


# b) Web user, database, and repository setup 

1. Create user (e.g. my-www-user) without sudo right, to run the webserver

- sudo adduser my-www-user

*attention: the nginx must run under the same user (configure in nginx.conf), otherwise the download of observation images can fail on wrong permissions, as this goes directly via nginx; after the reconfiguration make sure that the nginx cache directories (in Debian /var/lib/nginx subdirectories) are writeable buy that user, and anything in there (from possible previous nginx starts...) is owned by that user*

2. Create posgresql user and the database

- sudo -u postgres psql

    - postgres=# CREATE USER my-db-user WITH PASSWORD 'xxxxxxx'; 

    - postgres=# CREATE DATABASE "myappDB" OWNER my-db-user;

    - postgres=# ALTER USER my-db-user WITH SUPERUSER; 

3. As my-www-user user, clone the repository, such as in /home/my-www-user

- git clone https://github.com/baysics-lrz/pwa-template

4. Create and activate an virtual environment

- python3 -m venv venv

- source venv/bin/activate 
  (activate the virtual environment)

5. Install the packages listed in requirements.txt in the activated
virtual environment (requiements.txt is included in git repository)

- pip3 install wheel 
  (install wheel)

- vim requirements.txt 
  (please edit here requirements.txt to work -  the version of gdal must match the one installed in the machine, please also remove the version setting of numpy, psycopg2, psycopg2-binary)

- pip3 install -r requirements.txt

6. Create and edit settings_personal.py so that it matches with the information of database created above

- vim /home/my-www-user/pwa-template/webportal/webportal/settings_personal.py

  change the setting to connect to PostgreSQL not sqlite3 (Please adjust the setting to your database)

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            #'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'myappDB',
            'USER': 'my-db-user',
            'PASSWORD': '.........',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }


7. Adjust the allowed host for serving Django in settings.py

- vim /home/my-www-user/pwa-template/webportal/webportal/settings.py

        ALLOWED_HOSTS = ['............',    ]       
        # (for tests you can use    ALLOWED_HOSTS = ['*'])


# c) Toolkit setup (in activated virtual environment)

1. Create the database through Django migration

- python manage.py makemigrations

- python manage.py migration

2. Collect static files

- python3 manage.py collectstatic

3. Create an admin account to access admin feature such as CMS

- python manage.py createsuperuser

4. Test that gunicorn whether it can serve the application

- gunicorn --bind 0.0.0.0:8000 webportal.wsgi:application

5. Edit and activate gunicorn settings

- sudo vim /etc/systemd/system/gunicorn.service

        [Unit]
        Description=gunicorn daemon
        Requires=gunicorn.socket
        After=network.target
    
        [Service]
        User=my-www-user
        Group=www-data
        WorkingDirectory=/home/my-www-user/pwa-template/webportal
        ExecStart=/home/my-www-user/venv/bin/   
        gunicorn \
        --access-logfile - \
        --workers 3 \
        --bind unix:/run/gunicorn.sock \
        webportal.wsgi:application
    
        [Install]
        WantedBy=multi-user.target


- sudo vim /etc/systemd/system/gunicorn.socket

        [Unit]
        Description=gunicorn socket
    
        [Socket]
        ListenStream=/run/gunicorn.sock
    
        [Install]
        WantedBy=sockets.target


6. Start and enable the gunicorn socket and gunicorn

- sudo systemctl start gunicorn.socket

- sudo systemctl enable gunicorn.socket

- sudo systemctl status gunicorn.socket

- curl --unix-socket /run/gunicorn.sock localhost (test the socket activation)

- sudo systemctl status gunicorn (check gunicorn activation is working through socket)

- sudo systemctl daemon-reload

- sudo systemctl restart gunicorn 


7. Edit and activate nginx settings

- sudo vim /etc/nginx/sites-available/webportal

        server {
            listen 80;
            server_name <Please insert here the IP address>;
            location = /favicon.ico { access_log off; log_not_found off; }
            location /static/ {
            alias /home/my-www-user/pwa-template/webportal/static_root/;
            autoindex on;
            }
        location /media/ {
            alias /home/my-www-user/pwa-template/webportal/media/;
            autoindex on;
            }
        location / {
            include proxy_params;
            proxy_pass http://unix:/run/gunicorn.sock;
            client_max_body_size 0;
            proxy_request_buffering off;
            }
        }

- sudo ln -s /etc/nginx/sites-available webportal /etc/nginx/sites-enabled (enable the settings)

- sudo systemctl restart nginx


# d) Geodata related setup

**Loading the geospatial data in to the tables observations_climatestatoion, observations_hexagon, observations_municipal**

- python manage.py shell

- from geo_util.store_geo_data import store_everything_in_database

- store_everything_in_database()

*attention: Please include the "dgm" folder with the dgm tile geojsons in the "geo_util" folder on the sever.*

**Fixing the geometry attribute of the entries**
- python manage.py shell

- from geo_util.store_geo_data import check_point_geom

- check_point_geom()

**Fixing the empty DGM Altitude (Altitude_m) of the categoryX entries**

- python manage.py shell

- from geo_util.store_geo_data import check_categoryX_dgm

- check_categoryX_dgm()

**Fixing the empty Mountain Ranges (MountainRange) of the categoryX entries**

*attention: category3s outside the alpine area wills till have an empty mountain range.*

- python manage.py shell

- from geo_util.store_geo_data import check_categoryX_mntrange

- check_categoryX_mntrange()

**Fixing the broken thumbnails on the map**

*attention: only works of the original photo still exists at the media/photos/... location.*

- python manage.py shell

- from geo_util.store_geo_data import check_thumbnails

- check_thumbnails()

**Checking municipalities, Hexagonal Cells and Climate Stations**
- python manage.py shell

- from geo_util.store_geo_data import check_places

- check_places()

**Dumping data (if necessary)**
- manage.py loaddata db.json (to load the data file (db.json) into the dabase)

**Resoring data (if necessary)**
- manage.py dumpdata --natural-primary --indent 4 --exclude auth.permission --exclude contenttypes > db.json (to create the new data file (db.json))

**Changing Map Extent**

Our Example files are open data of Bavaria by the Bayerische Vermessungsverwaltung (Bavarian State Office for Survey) https://geodaten.bayern.de/opengeodata/ . At the time of creating and reusing the files were provided under a CC BY 3.0  DE License.

Our map view and scale are chosen to be suitable for Bavaria.
Here is an example how to change it:

    var map = L.map('map',).setView([49, 11], 7)
    //change to
    var map = L.map('map',).setView([view coordinates], zoom)

And changing the geofiles:

    <script src="/static/leaflet/spatial_files/landesgrenze.js" type="text/javascript"></script>
    //change to
    <script src="your own geojson" type="text/javascript"></script>

**DEM Altitude lookup**

In our example we precut multiple small raster files from Bavarian open data DEM.
On entering a new observation coordinate a lookup decides in which small tile the information about the elevation is. The code for this can be adapted in */geoutil/store_geo_data.py* and */geoutil/bayerntiles.geojson*.
This process requires OGRGeometries. In our case we used GDAL.

## Data Flagging (Flag)

Submitted data can be flagged with an integer number (PhotoFlag) according to the needs of app operators.
