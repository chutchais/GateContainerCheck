from django.db import models
from django.urls import reverse

# Create your models here.
class Machine(models.Model):
	name				= models.CharField(max_length=50,primary_key=True)
	machine_type		= models.CharField(max_length=10,blank=True, null=True)
	description 		= models.TextField(blank=True, null=True)
	created_date 		= models.DateTimeField(auto_now_add=True)
	last_loggin_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	ip 					= models.GenericIPAddressField(protocol='both', unpack_ipv4=False)

	def __str__(self):
		return '%s' % self.name