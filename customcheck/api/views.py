from django.db.models import Q

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from .serialize import (ContainerSerializer,RejectSerializer)
from customcheck.models import container,reject



class ContainerListAPIView(ListAPIView):
	queryset=container.objects.all()
	serializer_class=ContainerSerializer
	filter_backends=[SearchFilter,OrderingFilter]
	search_fields =['container']
	def get_queryset(self,*args,**kwargs):
		# queryset_list=Comment.objects.filter(user=self.request.user)
		queryset_list = container.objects.all()
		from_date = self.request.GET.get("f")
		to_date = self.request.GET.get("t")
		print ('From : %s  -- To : %s ' % (from_date,to_date))
		queryset_list = container.objects.filter(
				Q(created_date__range=[from_date,to_date]))
		return queryset_list

class RejectListAPIView(ListAPIView):
	queryset=reject.objects.all()
	serializer_class=RejectSerializer
	filter_backends=[SearchFilter,OrderingFilter]
	search_fields =['container']
	def get_queryset(self,*args,**kwargs):
		# queryset_list=Comment.objects.filter(user=self.request.user)
		queryset_list = reject.objects.all()
		from_date = self.request.GET.get("f")
		to_date = self.request.GET.get("t")
		print ('From : %s  -- To : %s ' % (from_date,to_date))
		queryset_list = reject.objects.filter(
				Q(created_date__range=[from_date,to_date]))
		return queryset_list
	# filter_backends=[SearchFilter,OrderingFilter],
	# search_fields =['content','user__first_name']
	# pagination_class = PostPageNumberPagination

# class VoyDetailAPIView(RetrieveAPIView):
# 	queryset=Voy.objects.all()
# 	serializer_class=VoyDetailSerializer
# 	lookup_field='slug'
# 	# print ("vessel details")