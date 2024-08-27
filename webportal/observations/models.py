from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
import datetime
from django.core.exceptions import ValidationError
from django.db.models import Count, Q, F
import os
from django.utils.crypto import get_random_string
# Geodjango models
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Polygon, Point


# User = settings.AUTH_USER_MODEL
from accounts.models import User as User
from messenger.models import ReportMessage


# Create your models here.

def file_validator(value):
    max_file_size_allowed = 15 * 1024 * 1024
    print(value.size)
    if value.size > max_file_size_allowed:
        print('file size too large (Max.MB).')
        raise ValidationError("The file size exceeds the maximum size (max. 15 MB). Please attach a smaller file.",
                              code='Invalid')


def no_future_date(value):
    today = datetime.date.today()
    if value > today:
        raise ValidationError('The date of observation cannot be a future date.')


CERTAINTY_CHOICES = (
    ('Uncertain', 'Uncertain'),
    ('Certain', 'Certain'),
)

POSITION_CHOICES = (
    ('automatic', 'automatic'),
    ('map/manual', 'map/manual'),
)


# The model for category1

CATEGORY1SUBJECT_CHOICES = (
    ('Category1Subject1', 'Category1Subject1'),
    ('Category1Subject2', 'Category1Subject2'),
)

CATEGORY1FEATURE1_CHOICES = (
    ('Category1Feature1-1', 'Category1Feature1-1'),
    ('Category1Feature1-2', 'Category1Feature1-2'),
    ('Category1Feature1-3', 'Category1Feature1-3'),
)

CATEGORY1FEATURE3_CHOICES = (
    ('Category1Feature3-1', 'Category1Feature3-1'),
    ('Category1Feature3-2', 'Category1Feature3-2'),
    ('Category1Feature3-3', 'Category1Feature3-3'),
    ('Category1Feature3-4', 'Category1Feature3-4'),
)

def content_file_name_category1(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.date.today()
    today_path = today.strftime("%Y/%m/%d")
    filename = "%s.%s" % (get_random_string(4), ext)
    return os.path.join('photos/category1/', today_path, filename)


class Category1(models.Model):
    # Metadata
    id = models.AutoField(primary_key=True)
    Creator = models.CharField(max_length=30, default='Project XXX Citizen Scientists')
    Title = models.CharField(max_length=80, default='Project XXX Citizen Science Data')
    Publisher = models.CharField(max_length=20, default='Project XXX')
    PublicationYear = models.CharField(max_length=4, default=str(datetime.datetime.now().year))
    Subject = models.CharField(max_length=30, default='Environmental Science')
    Contributor = models.CharField(max_length=30, default='XXX project partners')
    ResourceType = models.CharField(max_length=10, default='dataset')
    DateFirstCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    DateLastUpdated = models.DateTimeField(auto_now=True, null=True, blank=True)
    # Attributes related to GeneralInfo
    ObservationDate = models.DateField(default=datetime.date.today, verbose_name='Observation date')
    ObservationTime = models.TimeField(null=True, blank=True, verbose_name='Observation time')
    Lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, verbose_name='Latitude')
    Lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Longitude')
    AccuracyGPS = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='AccuracyGPS')
    Position = models.CharField(max_length=30, choices=POSITION_CHOICES, default="", verbose_name='Position')
    Altitude_m = models.IntegerField(null=True, blank=True, verbose_name='Altitude_m')
    Certainty = models.CharField(max_length=10, choices=CERTAINTY_CHOICES, default="", verbose_name='Certainty')
    # Information about observations made for category 1
    Category1Subject = models.CharField(max_length=30, choices=CATEGORY1SUBJECT_CHOICES, verbose_name='Category1Subject')
    Number = models.IntegerField(blank=True, null=True, verbose_name='Number', validators=[MinValueValidator(1)])
    Category1Feature1= models.CharField(max_length=20, default="", blank=True, choices=CATEGORY1FEATURE1_CHOICES, verbose_name='Category1Feature1')
    Category1Feature2 = models.CharField(max_length=100, default="", blank=True,
                                 verbose_name='Category1Feature2')
    Category1Feature3 = models.CharField(max_length=20, choices=CATEGORY1FEATURE3_CHOICES,
                                         verbose_name='Category1Feature3')
    # Photo related attributes
    Photo = models.ImageField(blank=True, upload_to=content_file_name_category1, default="",
                              verbose_name='Image upload (optional)',
                              validators=[file_validator,
                                          FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    Reliability = models.IntegerField(null=True, blank=True)
    ClimateStation = models.IntegerField(null=True, blank=True)
    Municipal = models.CharField(max_length=30, default="", blank=True)
    Cell = models.IntegerField(null=True, blank=True)
    # Postgis Geometry object
    geom = gismodels.PointField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Flag = models.IntegerField(null=True, blank=True)
    License = models.CharField(max_length=10, default='CC-BY')
    ReportComment = models.ForeignKey(ReportMessage, null=True, default=None, blank=True, on_delete=models.SET_NULL,
                                      related_name='category1_admin_comment')
    PublicComment = models.ForeignKey(ReportMessage, null=True, default=None, blank=True, on_delete=models.SET_NULL,
                                      related_name='category1_public_comment')


    def __str__(self):
        return '%s %s %s' % (self.id, self.Category1Subject, self.ObservationDate)


# The model for category 2

CATEGORY2SUBJECT_CHOICES = (
    ('Category2Subject1', 'Category2Subject1'),
    ('Category2Subject2', 'Category2Subject2'),
)

YESNO_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


def content_file_name_category2(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.date.today()
    today_path = today.strftime("%Y/%m/%d")
    filename = "%s.%s" % (get_random_string(4), ext)
    return os.path.join('photos/Category2/', today_path, filename)


class Category2(gismodels.Model):
    # Metadata
    id = models.AutoField(primary_key=True)
    Creator = models.CharField(max_length=30, default='Project XXX Citizen Scientists')
    Title = models.CharField(max_length=80,
                             default='Project XXX Citizen Science Data')
    Publisher = models.CharField(max_length=20, default='Project XXX')
    PublicationYear = models.CharField(max_length=4, default=str(datetime.datetime.now().year))
    Subject = models.CharField(max_length=30, default='Environmental Science')
    Contributor = models.CharField(max_length=30, default='XXX project partners')
    ResourceType = models.CharField(max_length=10, default='dataset')
    DateFirstCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    DateLastUpdated = models.DateTimeField(auto_now=True, null=True, blank=True)
    # Attributes related to GeneralInfo
    ObservationDate = models.DateField(default=datetime.date.today, verbose_name='Observation date',
                                       validators=[no_future_date])
    Lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, verbose_name='Latitude')
    Lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Longitude')
    AccuracyGPS = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='AccuracyGPS')
    Position = models.CharField(max_length=30, choices=POSITION_CHOICES, default="", verbose_name='Position')
    Altitude_m = models.IntegerField(null=True, blank=True, verbose_name='Altitude_m')
    Certainty = models.CharField(max_length=10, choices=CERTAINTY_CHOICES, default="", verbose_name='Certainty')
    # Information about observations made for category2
    Category2Subject = models.CharField(max_length=30, choices=CATEGORY2SUBJECT_CHOICES,
                                  verbose_name='Category2Subject')
    Category2Feature1 = models.CharField(max_length=4, choices=YESNO_CHOICES,
                                      verbose_name='Category2Feature1', default='No')
    Category2Feature2 = models.CharField(max_length=4, choices=YESNO_CHOICES,
                                                    verbose_name='Category2Feature2', default='No')
    Category2Feature3 = models.CharField(max_length=4, choices=YESNO_CHOICES, verbose_name='Category2Feature3', default='No')
    Category2Feature4 = models.CharField(max_length=4, choices=YESNO_CHOICES, verbose_name='Category2Feature4', default='No')
    Category2Feature5 = models.CharField(max_length=4, choices=YESNO_CHOICES, verbose_name='Category2Feature5', default='No')
    Category2Feature6 = models.CharField(max_length=4, choices=YESNO_CHOICES, verbose_name='Category2Feature6', default='No')
    Category2Feature7 = models.IntegerField(null=True, blank=True, verbose_name='Percentage1 (%)',
                                       validators=[
                                           MaxValueValidator(100),
                                           MinValueValidator(0)
                                       ])
    Category2Feature8 = models.IntegerField(null=True, blank=True, verbose_name='Percentage2(%)',
                                           validators=[
                                               MaxValueValidator(100),
                                               MinValueValidator(0)
                                           ]
                                           )
    # image related attributes
    Photo = models.ImageField(blank=True, upload_to=content_file_name_category2, default="",
                              verbose_name='Image upload (optional)',
                              validators=[file_validator,
                                          FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    Reliability = models.IntegerField(null=True, blank=True)
    ClimateStation = models.IntegerField(null=True, blank=True)
    Municipal = models.CharField(max_length=30, default="", blank=True)
    Cell = models.IntegerField(null=True, blank=True)
    # Postgis Geometry object
    geom = gismodels.PointField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Flag = models.IntegerField(null=True, blank=True)
    License = models.CharField(max_length=10, default='CC-BY')
    ReportComment = models.ForeignKey(ReportMessage, null=True, default=None, blank=True, on_delete=models.SET_NULL,
                                      related_name='category2_admin_comment')
    PublicComment = models.ForeignKey(ReportMessage, null=True, default=None, blank=True, on_delete=models.SET_NULL,
                                      related_name='category2_public_comment')

    def __str__(self):
        return '%s %s %s' % (self.id, self.Category2Subject, self.ObservationDate)


# The model for category3

CATEGORY3SUBJECT_CHOICES = (
    ('Category3Subject1', 'Category3Subject1'),
    ('Category3Subject2', 'Category3Subject2'),
)

CATEGORY3FEATURE1_CHOICES = (
    ('Category3Feature1-1', 'Category3Feature1-1'),
    ('Category3Feature1-2', 'Category3Feature1-2'),
    ('Category3Feature1-3', 'Category3Feature1-3'),
)


def content_file_name_category3(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.date.today()
    today_path = today.strftime("%Y/%m/%d")
    filename = "%s.%s" % (get_random_string(4), ext)
    return os.path.join('photos/category3/', today_path, filename)


class Category3(models.Model):
    # Metadata
    id = models.AutoField(primary_key=True)
    Creator = models.CharField(max_length=30, default='Project XXX Citizen Scientists')
    Title = models.CharField(max_length=80, default='Project XXX Citizen Science Data')
    Publisher = models.CharField(max_length=20, default='Project XXX')
    PublicationYear = models.CharField(max_length=4, default=str(datetime.datetime.now().year))
    Subject = models.CharField(max_length=30, default='Environmental Science')
    Contributor = models.CharField(max_length=30, default='XXX project partners')
    ResourceType = models.CharField(max_length=10, default='dataset')
    DateFirstCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    DateLastUpdated = models.DateTimeField(auto_now=True, null=True, blank=True)
    # Attributes related to GeneralInfo
    ObservationDate = models.DateField(default=datetime.date.today, verbose_name='Observation date',
                                       validators=[no_future_date])
    Lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, verbose_name='Latitude')
    Lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Longitude')
    AccuracyGPS = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='AccuracyGPS')
    Position = models.CharField(max_length=30, choices=POSITION_CHOICES, default="", verbose_name='Position')
    Altitude_m = models.IntegerField(null=True, blank=True, verbose_name='Altitude_m')
    Certainty = models.CharField(max_length=10, choices=CERTAINTY_CHOICES, default="", verbose_name='Certainty')
    # Information about observations made for Category3
    Category3Subject = models.CharField(max_length=30, choices=CATEGORY3SUBJECT_CHOICES,
                                   verbose_name='Category3Subject')
    Category3Feature1 = models.CharField(max_length=20, choices=CATEGORY3FEATURE1_CHOICES, verbose_name='Category3Feature1')
    Category3Feature2 = models.IntegerField(null=True, blank=True, verbose_name='Category3Feature2',validators=[MinValueValidator(0)])
    # Photo related attributes
    Photo = models.ImageField(upload_to=content_file_name_category3, default="",
                              verbose_name='Image upload (mandatory)',
                              validators=[file_validator,
                                          FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    Reliability = models.IntegerField(null=True, blank=True)
    ClimateStation = models.IntegerField(null=True, blank=True)
    Municipal = models.CharField(max_length=30, default="", blank=True)
    MountainRange = models.CharField(max_length=100, null=True, blank=True)  # the name is longer than 30 chars
    Cell = models.IntegerField(null=True, blank=True)
    # Postgis Geometry object
    geom = gismodels.PointField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Flag = models.IntegerField(null=True, blank=True)
    License = models.CharField(max_length=10, default='CC-BY')
    ReportComment = models.ForeignKey(ReportMessage, null=True, default=None, blank=True, on_delete=models.SET_NULL,
                                      related_name='category3_admin_comment')
    PublicComment = models.ForeignKey(ReportMessage, null=True, default=None, blank=True, on_delete=models.SET_NULL,
                                      related_name='category3_public_comment')

    def __str__(self):
        return '%s %s %s' % (self.id, self.Category3Subject, self.ObservationDate)


# The model for category4

CATEGORY4SUBJECT_CHOICES = (
    ('Category4Subject1', 'Category4Subject1'),
    ('Category4Subject2', 'Category4Subject2'),
)

def content_file_name_category4(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.date.today()
    today_path = today.strftime("%Y/%m/%d")
    filename = "%s.%s" % (get_random_string(4), ext)
    return os.path.join('photos/Category4/', today_path, filename)


class Category4(gismodels.Model):
    # Metadata
    id = models.AutoField(primary_key=True)
    Creator = models.CharField(max_length=30, default='Project XXX Citizen Scientists')
    Title = models.CharField(max_length=80,
                             default='Project XXX Citizen Science Data')
    Publisher = models.CharField(max_length=20, default='Project XXX')
    PublicationYear = models.CharField(max_length=4, default=str(datetime.datetime.now().year))
    Subject = models.CharField(max_length=30, default='Environmental Science')
    Contributor = models.CharField(max_length=30, default='XXX project partners')
    ResourceType = models.CharField(max_length=10, default='dataset')
    DateFirstCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    DateLastUpdated = models.DateTimeField(auto_now=True, null=True, blank=True)
    # Attributes related to GeneralInfo
    ObservationDate = models.DateField(default=datetime.date.today, verbose_name='Observation date',
                                       validators=[no_future_date])
    Lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True, verbose_name='Latitude')
    Lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True, verbose_name='Longitude')
    AccuracyGPS = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, verbose_name='AccuracyGPS')
    Position = models.CharField(max_length=30, choices=POSITION_CHOICES, default="", verbose_name='Position')
    Altitude_m = models.IntegerField(null=True, blank=True, verbose_name='Altitude_m')
    Certainty = models.CharField(max_length=10, choices=CERTAINTY_CHOICES, default="", verbose_name='Certainty')
    # Information about observations made for category4
    Category4Subject = models.CharField(max_length=30, choices=CATEGORY4SUBJECT_CHOICES,
                                  verbose_name='Category4Subject')
    Category4Feature1 = models.CharField(max_length=4, choices=YESNO_CHOICES, verbose_name='Category4Feature1', default='No')
    Category4Feature2 = models.CharField(max_length=4, choices=YESNO_CHOICES, verbose_name='Category4Feature2', default='No')
    Category4Feature3 = models.CharField(max_length=4, choices=YESNO_CHOICES, verbose_name='Category4Feature3', default='No')
    # image related attributes
    Photo = models.ImageField(blank=True, upload_to=content_file_name_category4, default="",
                              verbose_name='Image upload (optional)',
                              validators=[file_validator,
                                          FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    Reliability = models.IntegerField(null=True, blank=True)
    ClimateStation = models.IntegerField(null=True, blank=True)
    Municipal = models.CharField(max_length=30, default="", blank=True)
    Cell = models.IntegerField(null=True, blank=True)
    # Postgis Geometry object
    geom = gismodels.PointField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Flag = models.IntegerField(null=True, blank=True)
    License = models.CharField(max_length=10, default='CC-BY')
    ReportComment = models.ForeignKey(ReportMessage, null=True, default=None, blank=True, on_delete=models.SET_NULL,
                                      related_name='category4_admin_comment')
    PublicComment = models.ForeignKey(ReportMessage, null=True, default=None, blank=True, on_delete=models.SET_NULL,
                                      related_name='category4_public_comment')

    def __str__(self):
        return '%s %s %s' % (self.id, self.Category4Subject, self.ObservationDate)


# Returns a QuerySet of the Users with the number of observations in descending order
# -> count_obs is the annotated attribute of each user, which determines the number of observation

def get_category1_ranking():
    return User.objects.annotate(count_obs=Count('category1')).order_by('-count_obs')

def get_category2_ranking():
    return User.objects.annotate(count_obs=Count('category2')).order_by('-count_obs')

def get_category3_ranking():
    return User.objects.annotate(count_obs=Count('category3')).order_by('-count_obs')

def get_category4_ranking():
    return User.objects.annotate(count_obs=Count('category4')).order_by('-count_obs')


class Hexagon(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    tile = models.CharField(max_length=50)
    geometry = gismodels.PolygonField()

    def __str__(self):
        return str(self.id)


class ClimateStation(models.Model):
    station_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    height = models.FloatField()
    lat = models.FloatField()
    lon = models.FloatField()
    tile = models.CharField(max_length=50)
    geometry = gismodels.PolygonField()

    def __str__(self):
        return self.name


class Municipal(models.Model):
    id = models.AutoField(primary_key=True)
    bez_gem = models.CharField(max_length=200)
    bez_krs = models.CharField(max_length=200)
    bez_rbz = models.CharField(max_length=200)
    tile = models.CharField(max_length=50)
    geometry = gismodels.PolygonField()

    def __str__(self):
        return self.bez_gem


def get_municipal_via_coordinates(lat, lon):
    place = Point(lat, lon)
    # NaN is also acceptable which will happen instead of throwing an error
    try:
        return Municipal.objects.get(geometry__contains=place).bez_gem
    except:
        return

def get_climate_station_via_coordinates(lat, lon):
    place = Point(lat, lon)
    # NaN is also acceptable which will happen instead of throwing an error
    try:
        return ClimateStation.objects.get(geometry__contains=place).station_id
    except:
        return

def get_hexagon_via_coordinates(lat, lon):
    place = Point(lat, lon)
    # NaN is also acceptable which will happen instead of throwing an error
    try:
        return Hexagon.objects.get(geometry__contains=place).id
    except:
        return
