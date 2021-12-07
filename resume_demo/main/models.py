from enum import auto
from os import name
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import date, slugify
from ckeditor.fields import RichTextField

# Create your models here.

class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skill'
        verbose_name = 'Skill'
        
    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(max_length=20, blank=True, null=True)
    image = models.FileField(blank=True, null= True, upload_to="skills")
    is_key_skills = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
    

class UserProfile(models.Model):
    class Meta:
        verbose_name_plural = 'UserProfile'
        verbose_name = "User Profile"
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to =" avatars")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TimeField(blank=True, null=True)
    Skill = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv')
    
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    

class ContractProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contract Profile'
        verbose_name = 'Contract Profile'
        ordering = ["timestamp"]
        
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Massage")
    
    def  __str__(self):
        return f'{self.name}'
    
    
class Testimonials(models.Model):
    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonials'
        ordering = ["timestamp"]
        
    thumbnail = models.ImageField(blank=True, null=True, upload_to="thumbnail")
    name = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    qoute = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    

class Media(models.Model):
    class Meta:
        verbose_name_plural = 'Media file'
        verbose_name = 'Media'
        ordering = ["name"]
    
    image = models.ImageField(blank=True, null=True, upload_to="media_image")
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    

class Portfolio(models.Model):
    class Meta:
        verbose_name_plural = "Portfolio profile"
        verbose_name = "Portfolio"
        ordering = ["name"]
    
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio_image")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def  save(self, *args, **kwarge):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwarge)
def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"


class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/blog/{self.slug}"


class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
