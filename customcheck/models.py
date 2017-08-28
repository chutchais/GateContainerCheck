from django.db import models


# Create your models here.

class container(models.Model):
	container_no = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.container_no
