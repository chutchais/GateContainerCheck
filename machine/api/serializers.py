from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from machine.models import Machine

class MachineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Machine
		fields = ['name','machine_type','ip','description',
				'created_date','last_loggin_date','url']




