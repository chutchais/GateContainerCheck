import sys,getopt
import xlsxwriter
import openpyxl
from openpyxl import load_workbook
from eir_class import eir

import tempfile
import win32api
import win32print
import os
import re

class eir_print:
	def __init__(self, filename,templatefile,targetDir,setting,printer=''):
		self.filename = filename
		self.template_file = templatefile
		self.targetDir = targetDir
		self.printer = printer
		self.setting = setting
		self.json = ''

	def print(self):

		only_filename = os.path.split(self.filename)[1]
		head,tail = os.path.splitext(self.filename)
		eir_obj = eir(self.filename)
		data = eir_obj.getInfo()
		self.json = data

		# print(data)
		print ('Template file %s' % self.template_file)

		import win32com.client as win32
		excel = win32.gencache.EnsureDispatch('Excel.Application')
		wb = excel.Workbooks.Open(self.template_file)
		sheet = wb.Worksheets("EIR")
		for key in self.setting:
			col_range = self.setting[key]
			sheet.Range(col_range).Value = data[key]
			print (key,col_range,data[key])

		# xfile = load_workbook(self.template_file)
		# sheet = xfile.get_sheet_by_name('EIR')
		# Insert image
		# png_logo_name = r'LCB1.png'
		# png_iso_name = r'ISO.png'
		# logo_png = openpyxl.drawing.image.Image(png_logo_name)
		# iso_png = openpyxl.drawing.image.Image(png_iso_name)
		# sheet.add_image(logo_png, 'E1')
		# sheet.add_image(iso_png, 'L1')

		# for key in self.setting:
		# 	col_range = self.setting[key]
		# 	sheet[col_range] = data[key]
		# 	print (key,col_range)

		


		targetFile = self.targetDir + '\\' + os.path.split(self.filename)[1].replace('.','') +'.xlsx'
		# Check File existing
		if os.path.exists(targetFile):
			os.remove(targetFile)

		print ('Target file %s' % targetFile)
		# xfile.save(targetFile)
		# xfile.close()
		sheet.SaveAs(targetFile)
		# sheet.Close(True)
		excel.Quit()
		# excel.Application.Quit()


		default_printer =  win32print.GetDefaultPrinter()
		if self.printer == '' :
			curr_printer = default_printer
		else:
			curr_printer=self.printer
			win32print.SetDefaultPrinter(curr_printer)
		

		win32api.ShellExecute (
					  0,
					  "print",
					  targetFile,
					  #
					  # If this is None, the default printer will
					  # be used anyway.
					  #
					  '/d:"%s"' % curr_printer,
					  ".",
					  0
					)

		win32print.SetDefaultPrinter(default_printer) #set default back to original

		print ('Print successful!!')
		return True

# if __name__ == "__main__":
#     sys.exit(main(sys.argv[1:]))

