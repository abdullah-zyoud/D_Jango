from django.db import models
import datetime


class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["description"] = "description should be at least 10 characters"
        
        
        return errors
    
class Show(models.Model):
	title = models.CharField(max_length=255)
	network = models.TextField(max_length=255)
	release_date = models.DateField(auto_now=True)
	description = models.TextField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = BlogManager()



