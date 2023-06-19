from django.db import models

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "name should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "description should be at least 15 characters"
    
        return errors
    
class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()
    
	

class Description(models.Model):
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    