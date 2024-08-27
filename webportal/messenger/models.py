from django.db import models
from accounts.models import User


class ReportMessage(models.Model):
    id = models.AutoField(primary_key=True)
    date_created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
