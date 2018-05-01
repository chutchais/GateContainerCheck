# Command to run 
# python eir_print.py -i D:\gateout -t D:\gateout\template\EIR_LCMT.xlsx

import argparse
import os.path
import os
import tempfile
import shutil
import atexit
from datetime import datetime
from time import sleep
import itertools, sys
import time
import threading
from sys import stdin
import glob
import win32print

from eir_xlsx import eir_print
from face_detect import face_detection




url = 'http://127.0.0.1:8000'

class readable_dir(argparse.Action):
    def __call__(self,parser, namespace, values, option_string=None):
        prospective_dir=values
        if not os.path.isdir(prospective_dir):
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a valid path".format(prospective_dir))
        if os.access(prospective_dir, os.R_OK):
            setattr(namespace,self.dest,prospective_dir)
        else:
            raise argparse.ArgumentTypeError("readable_dir:{0} is not a readable dir".format(prospective_dir))


def makeDirectory():
    # print ('make dir')
    # output for today directory
    target_dir =directory + "\\" + "{:%Y-%m-%d}".format(datetime.now())
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    success_dir = target_dir +"\\success"
    error_dir = target_dir +"\\error"
    if not os.path.exists(success_dir):
        os.makedirs(success_dir)
    if not os.path.exists(error_dir):
        os.makedirs(error_dir)
    return (success_dir,error_dir)


def run():
    # import urllib3
    # http = urllib3.PoolManager()
    # print ('Intial HTTP successful')
    while True:
        eirs = glob.glob(working_dir + '\\*.*')
        if len(eirs)>0:
            target_dir =makeDirectory()
            filename=  eirs[0]
            head, tail = os.path.split(eirs[0])
            print ('Found EIR file : %s ' % filename)
            x = eir_print(filename,template_file,target_dir[0],setting_data,printer)
            # print(x.json)

            # Capture Image and do Face Detection
            # Delete Main and Thumbnail image file.
            
            captured = face_detection()
            captured.capture(50)
            # ------------

            # Once face captured then Print EIR
            result = x.print()
            # Move file to output folder 
            target_file = target_dir[0] +'\\' + tail
            shutil.move(eirs[0],target_file )



            #Upload to Database (Data)
            if result :
                
                print ('---Start to send data---')
                # print(x.json)
                # sys.exit()
                r = upload_container('api/gateout/data',x.json)
                # sys.exit()
                if r['successful']:
                    upload_image('api/gateout/image',r['container'],r['slug'],'main_image.jpg','thumbnail_image.jpg')

        else:
            print ('Not found EIR file : %s' % datetime.now() )

        sleep(3)    


if __name__ == "__main__":
    # TEmporary Directory
    ldir = tempfile.mkdtemp()
    atexit.register(lambda dir=ldir: shutil.rmtree(ldir))

    parser = argparse.ArgumentParser()

    parser.add_argument('-p','--printer', default='',
                        help="Print to printer")

    parser.add_argument('-i', '--input_directory', action=readable_dir, default=ldir)
    parser.add_argument('-b', '--base_directory', action=readable_dir,default='')
    parser.add_argument('-t', '--template_file',default='eir_template.xlsx', help="EIR Template file")
    args = parser.parse_args()
    
    # fSrcExist=args.master

    # print ('Real path file %s' % os.path.dirname(os.path.abspath(__file__)))

    printer=args.printer
    if printer =='':
        printer = win32print.GetDefaultPrinter()

    import json
    based_dir = args.base_directory 
    if based_dir =='' :
        fname = os.path.dirname(os.path.abspath(__file__))  + "\eir_setting.json"
    else :
        fname = based_dir + "\eir_setting.json"

    # print ("Configuration file on : %s" % fname)

    if os.path.isfile(fname) :
        x = open(fname).read()
        j = json.loads(x)

    # print ('********************************************************************')
    print ('******************* Auto EIR Start***********************************')
    print ('Configuration path: %s' % fname)
    print ('Template EIR file : %s' % args.template_file)
    print ('Working Directory : %s' % args.input_directory)
    print ('Printer : %s' % printer)
    print ('********************************************************************')

    # make output in working directory
    success_dir=""
    error_dir = ""
    working_dir = args.input_directory
    template_file = args.template_file
    setting_data = j
    # print (printer)
    directory= working_dir +"\output"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # --------------------------------

    spinner = itertools.cycle(['-', '/', '|', '\\'])


def upload_container(service,data):
    import urllib3
    http = urllib3.PoolManager()
    import json
    # import requests
    os.environ['NO_PROXY'] = url
    headers = {'Content-type': 'application/json'}
    # headers = urllib3.util.make_headers(basic_auth='admin:lcb12017',content_type='application/json')
    url_service = url + '/' + service 
    print (data)
    r = http.request('POST', url_service,headers=headers,body=json.dumps(data))
    print (r.data)
    return json.loads(r.data.decode('utf-8'))

def upload_image(service,container_number,container_slug,image1,image2):
    import os
    import requests
    print ('Upload files to Web service')
    os.environ['NO_PROXY'] = url
    url_service = url + '/' + service 
    fimg = open(image1, 'rb')
    fthum = open(image2, 'rb')
    files = {'image':('%s.png' % container_number ,fimg),
            'thumbnails':('%s_thumbnail.png' % container_number ,fthum)}
    data = {'slug':container_slug}
    try:
      r = requests.post(url_service,files=files,data=data)
      # print (r.text)
    finally:
      fimg.close()
      fthum.close()
    # r = requests.post(urls,files=files,data={'slug':'sdsdsd'})

    # files = {'image':('image.png',i),
    # 'thumbnails':('tum.png',t)}
    return json.loads(r.text)

run()
