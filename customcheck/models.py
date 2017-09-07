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

class reject(models.Model):
	container_no = models.CharField(max_length=50)
	description = models.TextField(blank=True, null=True)
	no_shore = models.BooleanField(verbose_name ='No Shore',default=False)
	no_paid = models.BooleanField(verbose_name ='ติดจ่ายตังค์',default=False)
	no_customs = models.BooleanField(verbose_name ='ติด Custom',default=False)
	no_vgm = models.BooleanField(verbose_name ='No VGM',default=False)
	late_gate = models.BooleanField(verbose_name ='Late Gate',default=False)
	other = models.CharField(verbose_name ='อื่นๆ',max_length=100)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(blank=True, null=True,auto_now=True)
	user = models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.container_no
