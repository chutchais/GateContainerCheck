from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect


from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404
import sys
from django.db.models import Q,F
import json
from django.contrib.auth.models import User
from django.views import View
from gateout.models import vessel,voy,booking,container,container_images

@api_view(['POST','GET'])
@csrf_exempt
def hello_world(request):
	if request.method=='POST':
		print('POST')
	if request.method=='GET':
		print('GET')
	return JsonResponse({"message": "Hello, world!"})


@api_view(['POST'])
@csrf_exempt
def upload(request):
	response_msg = ''
	if request.method=='POST':
		try :
			import datetime

			data = json.loads(request.body.decode("utf-8"))
			# Show all data
			for key in data:
				print (key,data[key])
			# return JsonResponse ({'error':'sds'})
			# ------------
			# Verify Container info
			# Create Vessel
			vessel_obj,created = vessel.objects.get_or_create(code=data['vessel_code'])
			vessel_obj.name = data['vessel_name']
			vessel_obj.save()
			# Create Voy
			voy_obj,created = voy.objects.get_or_create(voy=data['voy'],vessel=vessel_obj)
			# Create Booking
			booking_obj,created = booking.objects.get_or_create(booking=data['booking'],voy=voy_obj)
			booking_obj.line = data['shipping_line']
			booking_obj.save()
			# Create Container
			container_obj,created = container.objects.get_or_create(number=data['container'],booking=booking_obj)
			container_obj.order_date = datetime.datetime.strptime(data['order_date'], "%d/%m/%y %H:%M")
			container_obj.imo1 = data['imo1']
			container_obj.imo2 = data['imo2']
			container_obj.move = data['move']
			container_obj.temperature = data['temperature']
			container_obj.pod = data['pod']
			# container_obj.size = data['size']
			container_obj.terminal = 'LCB1' if data['plate'][:1]=='B' else 'LCMT'
			container_obj.iso = data['iso']
			container_obj.plate_id = data['plate']
			container_obj.truck_company = data['truck_company']
			container_obj.consignee = data['consignee']
			container_obj.seal1 = data['seal1']
			container_obj.seal2 = data['seal2']
			container_obj.weight = float(data['gross_weight'].replace(',',''))
			container_obj.exception = data['exception']
			container_obj.genset = data['genset']
			container_obj.damage = data['damage']
			container_obj.remark = '%s %s' % (data['remark1'],data['remark2'])
			container_obj.checker = data['checker']
			container_obj.check_date = datetime.datetime.strptime(data['check_date'], "%d/%m/%y")
			container_obj.save()
			response_msg={'msg':'successful',
							'successful':True,
							'slug': container_obj.slug,
							'container': container_obj.number}
		except OSError as err:
			response_msg={'msg':"OS error: {0}".format(err),
							'created':False}
		except ValueError:
			response_msg={'msg':"Object of type 'type' is not JSON serializable",
							'created':False}

		except TypeError:
			response_msg={'msg':sys.exc_info()[0],
							'created':False}
		except:
			response_msg={'msg':sys.exc_info()[0],
							'created':False}

	return JsonResponse (response_msg)


@api_view(['POST'])
@csrf_exempt
def image(request):
	# print ('image')
	if request.method=='POST':
		image = request.FILES['image']
		thumbnails = request.FILES['thumbnails']
		slug = request.POST.get('slug', '')
		c = container.objects.get(slug=slug)
		# print(c)
		if c :
			c_image = container_images.objects.create(container=c,
								image=image,
								thumbnails_image=thumbnails)
			# c_image.image = image
			# c_image.thumbnails_image = thumbnails
			# c_image.save()
		print(slug)
		return JsonResponse ({'status':'ok'})