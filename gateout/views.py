# from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
import sys
from django.db.models import Q,F
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views import View
from .models import vessel,voy,booking,container,container_images


# Create your views here.
# import os
# os.environ['NO_PROXY'] = url
# url = "http://localhost:5000/"
# fin = open('simple_table.pdf', 'rb')
# files = {'file': fin}
# try:
#   r = requests.post(url, files=files)
# 	print r.text
# finally:
# 	fin.close()
# r = requests.post(urls,files=files,data={'slug':'sdsdsd'})

# files = {'image':('image.png',i),
# 'thumbnails':('tum.png',t)}

from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

# class OperationListView(ListView):
# 	model = Operation

class ContainerDetailView(DetailView):
	model = container

class ContainerListView(ListView):
	model = container
	paginate_by = 30
	template_name = 'gateout.html'

	def get_queryset(self):
		from django.utils import timezone
		import pytz
		query = self.request.GET.get('q')
		if query :
			return container.objects.filter(Q(number__icontains=query)|
				Q(booking__booking__icontains=query)|
				Q(booking__voy__voy__icontains=query)|
				Q(booking__voy__vessel__code__icontains=query)|
				Q(booking__voy__vessel__name__icontains=query)|
				Q(booking__line__icontains=query)|
				Q(plate_id__icontains=query)|
				Q(truck_company__icontains=query)|
				Q(consignee__icontains=query)).order_by('-created_date')
		else:
			to_day = timezone.now().today()
		return container.objects.filter(created_date__year=to_day.year,
										created_date__month=to_day.month,
										created_date__day=to_day.day).order_by('-created_date')

# 

def home(request):
	c = container.objects.all().order_by('-created_date')
	return render(request,
		'gateout.html', {'containers':c})

def daily(request,year,month,day):
	c = container.objects.filter(created_date__year=year,
		created_date__month=month,
		created_date__day=day).order_by('created_date')
	# c = container.objects.all()
	context={
		'object_list' : c,
		'year':year,'month':month,'day':day
		}
	# print(c)
	return render(request,
		'gateout_daily.html',context)

# @api_view(['POST'])
# @csrf_exempt
# def image(request):
# 	# print ('image')
# 	if request.method=='POST':
# 		image = request.FILES['image']
# 		thumbnails = request.FILES['thumbnails']
# 		slug = request.POST.get('slug', '')
# 		c = container.objects.get(slug=slug)
# 		# print(c)
# 		if c :
# 			c_image = container_images.objects.create(container=c,
# 								image=image,
# 								thumbnails_image=thumbnails)
# 			# c_image.image = image
# 			# c_image.thumbnails_image = thumbnails
# 			# c_image.save()
# 		print(slug)
# 		return JsonResponse ({'status':'ok'})


# @api_view(['POST'])
# @csrf_exempt
# def upload(request):
# 	response_msg = ''
# 	if request.method=='POST':
# 		try :
# 			import datetime
# 			data = json.loads(request.body.decode("utf-8"))
# 			# Show all data
# 			for key in data:
# 				print (key,data[key])
# 			# ------------
# 			# Verify Container info
# 			# Create Vessel
# 			vessel_obj,created = vessel.objects.get_or_create(code=data['vessel_code'])
# 			vessel_obj.name = data['vessel_name']
# 			vessel_obj.save()
# 			# Create Voy
# 			voy_obj,created = voy.objects.get_or_create(voy=data['voy'],vessel=vessel_obj)
# 			# Create Booking
# 			booking_obj,created = booking.objects.get_or_create(booking=data['booking'],voy=voy_obj)
# 			booking_obj.line = data['shipping_line']
# 			booking_obj.save()
# 			# Create Container
# 			container_obj,created = container.objects.get_or_create(number=data['container'],booking=booking_obj)
# 			container_obj.order_date = datetime.datetime.strptime(data['order_date'], "%d/%m/%y %H:%M")
# 			container_obj.imo1 = data['imo1']
# 			container_obj.imo2 = data['imo2']
# 			container_obj.move = data['move']
# 			container_obj.temperature = data['temperature']
# 			container_obj.pod = data['pod']
# 			# container_obj.size = data['size']
# 			container_obj.terminal = 'LCB1' if data['plate'][:1]=='B' else 'LCMT'
# 			container_obj.iso = data['iso']
# 			container_obj.plate_id = data['plate']
# 			container_obj.truck_company = data['truck_company']
# 			container_obj.consignee = data['consignee']
# 			container_obj.seal1 = data['seal1']
# 			container_obj.seal2 = data['seal2']
# 			container_obj.weight = float(data['gross_weight'].replace(',',''))
# 			container_obj.exception = data['exception']
# 			container_obj.genset = data['genset']
# 			container_obj.damage = data['damage']
# 			container_obj.remark = '%s %s' % (data['remark1'],data['remark2'])
# 			container_obj.checker = data['checker']
# 			container_obj.check_date = datetime.datetime.strptime(data['check_date'], "%d/%m/%y")
# 			container_obj.save()
# 			response_msg={'msg':'successful',
# 							'successful':True,
# 							'slug': container_obj.slug,
# 							'container': container_obj.number}
# 		except OSError as err:
# 			response_msg={'msg':"OS error: {0}".format(err),
# 							'created':False}
# 		except ValueError:
# 			response_msg={'msg':"Object of type 'type' is not JSON serializable",
# 							'created':False}

# 		except TypeError:
# 			response_msg={'msg':sys.exc_info()[0],
# 							'created':False}
# 		except:
# 			response_msg={'msg':sys.exc_info()[0],
# 							'created':False}

# 	return JsonResponse (response_msg)
