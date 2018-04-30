from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.urls import reverse

# Create your models here.
class vessel(models.Model):
	code			= models.CharField(max_length=50,primary_key=True)
	name 			= models.CharField(max_length=50)
	description 	= models.TextField(blank=True, null=True)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey('auth.User',blank=True,null=True)
	def __str__(self):
		return '%s %s' %(self.code,self.name)

class voy(models.Model):
	voy				= models.CharField(max_length=50,primary_key=True)
	vessel 			= models.ForeignKey(vessel)
	description 	= models.TextField(blank=True, null=True)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey('auth.User',blank=True,null=True)
	def __str__(self):
		return self.voy

class booking(models.Model):
	booking 		= models.CharField(max_length=50,primary_key=True)
	line			= models.CharField(max_length=50)
	voy 			= models.ForeignKey(voy)
	description 	= models.TextField(blank=True, null=True)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey('auth.User',blank=True,null=True)
	def __str__(self):
		return self.booking

class container(models.Model):
	number 			= models.CharField(max_length=15)
	slug 			= models.SlugField(unique=True,blank=True, null=True)
	terminal		= models.CharField(max_length=10)
	booking 		= models.ForeignKey(booking)
	order_date		= models.DateTimeField(blank=True, null=True)
	imo1			= models.CharField(max_length=20)
	imo2			= models.CharField(max_length=20)
	move			= models.CharField(max_length=50)
	temperature		= models.CharField(max_length=20)
	pod				= models.CharField(max_length=20)
	size			= models.CharField(max_length=20)
	iso 			= models.CharField(max_length=10)
	plate_id		= models.CharField(max_length=20)
	truck_company 	= models.CharField(max_length=100)
	consignee		= models.CharField(max_length=100)
	seal1			= models.CharField(max_length=50)
	seal2			= models.CharField(max_length=50)
	weight			= models.FloatField(default=0)
	exception		= models.CharField(max_length=100)
	genset			= models.CharField(max_length=100)
	damage			= models.CharField(max_length=200)
	remark			= models.CharField(max_length=200)
	checker			= models.CharField(max_length=100)
	check_date		= models.DateTimeField(blank=True, null=True)
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey('auth.User',blank=True,null=True)
	
	class Meta:
		unique_together = ('number','booking')

	def __str__(self):
		return self.number

	def get_absolute_url(self):
		return reverse('gateout:detail', kwargs={'slug': self.slug})

def image_directory_path(instance, filename):
    from datetime import datetime
    today = datetime.now()
    year = today.year
    month = today.month
    day = today.day
    return 'images/%s/%s/%s/%s/%s' % (instance.container.terminal,year,month,day, filename)

def thumbnails_directory_path(instance, filename):
    from datetime import datetime
    today = datetime.now()
    year = today.year
    month = today.month
    day = today.day
    return 'thumbnails/%s/%s/%s/%s/%s' % (instance.container.terminal,year,month,day, filename)

# Support multiple image for each contianer
class container_images(models.Model):
	container 		= models.ForeignKey(container)
	image 			= models.ImageField(upload_to =image_directory_path )
	thumbnails_image= models.ImageField(upload_to =thumbnails_directory_path )
	created_date 	= models.DateTimeField(auto_now_add=True)
	modified_date 	= models.DateTimeField(blank=True, null=True,auto_now=True)
	user 			= models.ForeignKey('auth.User',blank=True,null=True)

	def __str__(self):
		return self.container.number

	def get_image_url(self):
		return self.image.url


# def image_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'containers/%Y/%m/%d/{0}/{1}'.format(instance.user.id, filename)
    

def create_container_slug(instance, new_slug=None):
    slug = slugify("%s-%s" %(instance.number, instance.booking))
    if new_slug is not None:
        slug = new_slug
    qs = container.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.count())
        return create_container_slug(instance, new_slug=new_slug)
    return slug


def pre_save_container_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_container_slug(instance)

pre_save.connect(pre_save_container_receiver, sender=container)