import datetime
from msilib.schema import AdminExecuteSequence
import os
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Region(models.Model):
    region_name = models.CharField(max_length=25)

    def __str__(self):
        return self.region_name
        
    class Meta:
        ordering = ['region_name']


class Countrie(models.Model):
    country_name = models.CharField(max_length=40,default='DEFAULT VALUE')
    regions = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name

    class Meta:
        ordering = ['country_name']


class Location(models.Model):
    street_address = models.CharField(max_length=25)
    postal_code = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    state_province = models.CharField(max_length=12)
    countries = models.ForeignKey(Countrie, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.street_address

    class Meta:
        ordering = ['street_address']

class Department(models.Model):
    depart_name = models.CharField(max_length=30,default='DEFAULT VALUE')
    locations = models.ForeignKey(Location,on_delete=models.CASCADE)

    def __str__(self):
        return self.depart_name

    class Meta:
        ordering = ['depart_name']      

class Job(models.Model):
    job_title = models.CharField(max_length=35)
    min_salaty = models.IntegerField()
    max_salary = models.IntegerField()
    
    def __str__(self):
        return self.job_title

    class Meta:
        ordering = ['job_title'] 

from django.urls import reverse


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField()
    salary = models.IntegerField()
    commission_pct = models.IntegerField()
    content = models.TextField(null=True,blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    file = models.FileField(null=True,blank=True,upload_to='Files')
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    departments = models.ForeignKey(Department,on_delete=models.CASCADE)
    jobs= models.ForeignKey(Job,on_delete=models.CASCADE)

    class Meta:
        ordering = ["-first_name"]


    def __str__(self):
        return self.first_name

    def extension(self):
        name,extension = os.path.splitext(self.file.name)
        return extension

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})           
    
    @property
    def file_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url

    def was_published_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)

class Job_History(models.Model):
    jobs = models.ForeignKey(Job, on_delete=models.CASCADE)
    departments = models.ForeignKey(Department,on_delete=models.CASCADE)
    employees = models.ForeignKey(Employee,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.start_date

    class Meta:
        ordering = ['start_date']   

      







  