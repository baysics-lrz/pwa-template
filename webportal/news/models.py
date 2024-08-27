import datetime

from django.db import models
from accounts.models import User
from django.core.validators import FileExtensionValidator
from django.utils.crypto import get_random_string
import os

def file_validator(value):
    max_file_size_allowed = 15 * 1024 * 1024
    print(value.size)
    if value.size > max_file_size_allowed:
        print('file size too large (Max.MB).')
        raise ValidationError("The file size exceeds the maximum size (max. 15 MB). Please attach a smaller file.",
                              code='Invalid')


def content_file_name_news(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.date.today()
    today_path = today.strftime("%Y/%m/%d")
    # today_path_name = today.strftime("%Y%m%d")
    filename = "%s.%s" % (get_random_string(4), ext)
    return os.path.join('news/', today_path, filename)

# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    text2 = models.TextField(blank=True, default="")
    text3 = models.TextField(blank=True, default="")
    text4 = models.TextField(blank=True, default="")
    text5 = models.TextField(blank=True, default="")
    text6 = models.TextField(blank=True, default="")
    header = models.TextField(blank=True, default="")
    header2 = models.TextField(blank=True, default="")
    header3 = models.TextField(blank=True, default="")
    header4 = models.TextField(blank=True, default="")
    header5 = models.TextField(blank=True, default="")
    header6 = models.TextField(blank=True, default="")
    photo = models.ImageField(blank=True, upload_to=content_file_name_news, default="",
                              verbose_name='Upload image (optional)',
                              validators=[file_validator,
                                          FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    photo2 = models.ImageField(blank=True, upload_to=content_file_name_news, default="",
                              verbose_name='Upload image (optional)',
                              validators=[file_validator,
                                          FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    photo2caption = models.TextField(blank=True, default="")
    photo3 = models.ImageField(blank=True, upload_to=content_file_name_news, default="",
                               verbose_name='Upload image (optional)',
                               validators=[file_validator,
                                           FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    photo3caption = models.TextField(blank=True, default="")
    photo4 = models.ImageField(blank=True, upload_to=content_file_name_news, default="",
                               verbose_name='Upload image (optional)',
                               validators=[file_validator,
                                           FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    photo4caption = models.TextField(blank=True, default="")
    photo5 = models.ImageField(blank=True, upload_to=content_file_name_news, default="",
                               verbose_name='Upload image (optional)',
                               validators=[file_validator,
                                           FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    photo5caption = models.TextField(blank=True, default="")
    photo6 = models.ImageField(blank=True, upload_to=content_file_name_news, default="",
                               verbose_name='Upload image (optional)',
                               validators=[file_validator,
                                           FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    photo6caption = models.TextField(blank=True, default="")

    def __str__(self):
        return str(self.title)
