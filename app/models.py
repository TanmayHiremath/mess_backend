from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
from urllib import request
from django.core.files import File
import os
from django.utils.html import mark_safe

def upload_location(instance, filename):
    return 'images/{}'.format(instance.roll_number)
class User(models.Model):
    name = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=12, primary_key=True)
    status = models.CharField(max_length=15)
    card_no = models.CharField(max_length=100, unique=True)
    image_url = models.CharField(max_length=200,null=True)
    image_file = models.ImageField(upload_to=upload_location,null=True,blank=True)
    def get_remote_image(self):
        if self.image_url and not self.image_file:
            result = request.urlretrieve(self.image_url)
            self.image_file.save(
                    os.path.basename(self.image_url),
                    File(open(result[0], 'rb'))
                    )
            self.save()
    def image_tag(self):
            return mark_safe('<img src="/images/%s" width="150" height="150" />' % (self.image_file))		

    def save(self, *args, **kwargs):
        self.get_remote_image()
        super().save(*args, **kwargs)  
    

class Month(models.Model):
    MONTH_CHOICES = [
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December'),
    ]
    roll_number = models.ForeignKey(
        User, on_delete=models.CASCADE, default="19D070061")
    data = ArrayField(models.CharField(max_length=7), size=31, default=['99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999',
                                                                        '99999'])
    month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES, null=True)

    class Meta:
        unique_together = ('roll_number', 'month',)
