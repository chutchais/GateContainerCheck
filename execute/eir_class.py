import sys,getopt

class eir:
	def __init__(self, filename):
		self.filename = filename
		self.container1_exist = False
		self.container2_exist = False
		self.container3_exist = False
		self.container4_exist = False
		self.MTY_exist =False
		self.container_line_number = 0

	# @staticmethod	

	def get_layout_count(self,layout):
		return len(layout)


	def get_line_text(self,layout,line_number):
		i=1
		for lt_obj in layout:
			if isinstance(lt_obj, LTTextBox) :
				if i==line_number :
					# print('--in function--%s' % i)
					x=lt_obj.get_text()
					return x.strip()
				i=i+1
		return ''

	def get_line_string(self,line_no,start_pos):
		return self.text_content[line_no].strip()

	def get_line_string_raw(self,line_no,start_pos):
		return self.text_content[line_no]

	def getInfo(self):
		with open(self.filename) as file:
			x = [l.strip() for l in file]

		line_offset = 0

		for ix,l in enumerate(x):
			line_data = l.split('    ')

			if ix ==  2:
				if len(line_data[0].strip()) == 0 :
					line_offset = 2
			# get Company info
			if ix == line_offset+2:
				print (line_data)
				company = line_data[0].strip()
				# print (company)
			# get Date,Line,Container
			if ix == line_offset+4:
				print (line_data)
				order_date= line_data[0].strip()
				line= line_data[2].strip()
				container= line_data[7].strip()
				# print (order_date,line,container)
			# get vessel code/voy
			if ix == line_offset+6:
				print (line_data)
				tmp_text = line_data[0].strip()
				voy_arry = tmp_text.split(' ')

				imo1=''
				if len(voy_arry) == 0:
					voy = tmp_text

				if len(voy_arry) >0:
					vessel_code_voy_text = voy_arry[len(voy_arry)-1].strip()
					vessel_code = vessel_code_voy_text.split('/')[0]
					voy = vessel_code_voy_text.split('/')[1]
					imo1 = tmp_text.replace(vessel_code_voy_text,'')

			# get Vessel Name,Move, date
			if ix == line_offset+7:
				print ('IX %s :%s' %(ix,line_data))
				move = line_data[4].strip()
				if move =='':
					move = line_data[3].strip()
				if move =='':
					move = line_data[2].strip()
				vessel_name= line_data[0].strip()
				imo2=''
				if len(vessel_name.split('/'))>1:
					# print('Mix')
					tmp_imo = vessel_name.split('/')[0].strip()
					tmp_vessel_name = vessel_name.split('/')[1].strip()

					tmp_vessel_arry = tmp_vessel_name.split(' ')

					tmp_imo = '%s / %s' % (tmp_imo,tmp_vessel_arry[0].strip())
					tmp_vessel_name = tmp_vessel_name.replace(tmp_vessel_arry[0].strip(),'')

					vessel_name = tmp_vessel_name.strip()
					imo2 = tmp_imo.strip()
					# print (tmp_imo,tmp_vessel_name)
					move = line_data[3].strip() #'DRY,2DG'
					if move =='':
						move = line_data[2].strip()#1 DG



				
				date = line_data[len(line_data)-1].strip()
				# print(vessel_name,move,date)
			# Type ,ISO ,POD
			if ix == line_offset+9:
				print(line_data)
				temperature=''
				if len(line_data) == 10: #Reefer
					temperature = line_data[0].strip()
					type_text = line_data[2].strip()
					iso = line_data[5].strip()
					pod = line_data[9].strip()

				if len(line_data) == 8: #Dry
					type_text = line_data[0].strip()
					iso = line_data[3].strip()
					pod = line_data[7].strip()

				# print (type_text,iso,pod)

			# PlateID,Truck company,booking
			if ix == line_offset+11:
				print (line_data)
				plate_text = line_data[0].strip()
				truck_company = line_data[2].strip()
				booking = line_data[len(line_data)-1].strip()
				

			# Gross weight,Seal
			if ix == line_offset+13:
				print(line_data)
				gross_weight = line_data[0].strip()
				seal1 = line_data[2].strip()
				# print (gross_weight,seal)

			if ix == line_offset+14:
				print(line_data)
				seal2 = line_data[0].strip()

			# Damage, remark
			if ix == line_offset+17:
				print (line_data)
				damage=''
				remark=''
				if len(line_data) == 1: #Refee
					remark = line_data[0].strip()
				if len(line_data) == 8: #Dry
					damage = line_data[0].strip()
					remark = line_data[7].strip()

			if ix == line_offset+18:
				print (line_data)
				damage2=''
				remark2=''
				if len(line_data) == 1: #Refee
					remark2 = line_data[0].strip()
				if len(line_data) == 8: #Dry
					damage2 = line_data[0].strip()
					remark2 = line_data[7].strip()
				# print (damage,remark)
			if ix == line_offset+29:
				print (line_data)
				checker = line_data[0].strip()
				check_date = line_data[4].strip()
				# print (damage,remark)


		
		data= {
			"terminal" : company,
			"order_date":order_date,
			"shipping_line":line,
			"container":container,
			"voy_text":vessel_code_voy_text,
			"voy":voy,
			"imo1":imo1,
			"imo2":imo2,
			"vessel_name": vessel_name,
			"vessel_code": vessel_code,
			"move":move,
			"temperature":temperature,
			"pod":pod,
			"type":type_text,
			"date":date,
			"iso":iso,
			"plate":plate_text,
			"truck_company":truck_company,
			"consignee":'',
			"booking":booking,
			"seal1":seal1,
			"seal2":seal2,
			"gross_weight":gross_weight,
			"exception":'',
			"genset":'',
			"damage":damage,
			"remark1":remark,
			"remark2":remark2,
			"checker":checker,
			"check_date":check_date
		}
		# print(data)
		return data



	

	


	

