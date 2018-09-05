from rest_framework import viewsets,filters
from rest_framework import status, viewsets
# from rest_framework.decorators import action,detail_route
from rest_framework.response import Response


from machine.models import Machine
from machine.api.serializers import MachineSerializer

class MachineViewSet(viewsets.ModelViewSet):
	queryset = Machine.objects.all()
	serializer_class = MachineSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter)
	search_fields = ('name','ip','machine_type', 'description')
