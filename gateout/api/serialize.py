# from rest_framework import serializers

# class GateOut(object):
#     def __init__(self, container):
#         self.container	 	= container
#         self.terminal		= None
#         self.shipping_line	= None
#         self.order_date		= None
#         self.voy_text		= None
#         self.voy 			= None
#         self.imo1			= None
#         self.imo2 			= None
#         self.vessel_name	= None
#         self.vessel_code	= None
#         self.move 			= None
#         self.temperature 	= None
#         self.pod			= None
#         self.cont_type		= None
#         self.date 			= None
#         self.iso 			= None
#         self.plate 			= None
#         self.truck_company 	= None
#         self.consignee		= None
#         self.booking		= None
#         self.seal1			= None
#         self.seal2			= None
#         self.gross_weight	= None
#         self.exception		= None
#         self.genset 		= None
#         self.damage 		= None
#         self.remark1 		= None
#         self.remark2		= None
#         self.checker		= None
#         self.check_date		= None


# class GateOutSerializer(serializers.Serializer):
# 	terminal 		= serializers.CharField(max_length=100)
# 	shipping_line	= serializers.CharField(max_length=20)
# 	order_date 		= serializers.CharField(max_length=20)
# 	container 		= serializers.CharField(max_length=20)
# 	voy_text 		= serializers.CharField(max_length=20)
# 	voy 			= serializers.CharField(max_length=20)
# 	imo1 	 		= serializers.CharField(max_length=20)
# 	imo2 	 		= serializers.CharField(max_length=20)
# 	vessel_name		= serializers.CharField(max_length=50)
# 	vessel_code		= serializers.CharField(max_length=10)
# 	move	 		= serializers.CharField(max_length=20)
# 	temperature		= serializers.CharField(max_length=10)
# 	pod		 		= serializers.CharField(max_length=10)
# 	cont_type	 	= serializers.CharField(max_length=10)
# 	date 	 		= serializers.CharField(max_length=20)
# 	iso		 		= serializers.CharField(max_length=10)
# 	plate	 		= serializers.CharField(max_length=20)
# 	truck_company	= serializers.CharField(max_length=100)
# 	consignee 		= serializers.CharField(max_length=100)
# 	booking 		= serializers.CharField(max_length=50)
# 	seal1 			= serializers.CharField(max_length=50)
# 	seal2	 		= serializers.CharField(max_length=50)
# 	gross_weight	= serializers.CharField(max_length=20)
# 	exception 		= serializers.CharField(max_length=100)
# 	genset 			= serializers.CharField(max_length=50)
# 	damage 			= serializers.CharField(max_length=100)
# 	remark1			= serializers.CharField(max_length=100)
# 	remark2			= serializers.CharField(max_length=100)
# 	checker			= serializers.CharField(max_length=20)
# 	check_date 		= serializers.CharField(max_length=20)

# 	def create(self, validated_data):
# 		return GateOut(**validated_data)

#     # def save(self):
#     #     email = self.validated_data['email']
#     #     message = self.validated_data['message']
#     #     send_email(from=email, message=message)
