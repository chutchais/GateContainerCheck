from capture_camera import capture_image
import threading
import time
from playsound import playsound


exitFlag = 0

class cameraThread (threading.Thread):
	def __init__(self, threadID, name, ip,user,password,counter):
		threading.Thread.__init__(self)
		self.threadID 	= threadID
		self.name 		= name
		self.ip 		= ip
		self.user 		= user
		self.password 	= password
		self.counter 	= counter
	def run(self):
		print ("Starting capture %s" % self.name)
		captured = capture_image(self.name,self.ip,self.user,self.password)
		captured.capture(self.counter)
		print ("Finished capture %s" % self.name)

class outSound (threading.Thread):
    def __init__(self, threadID, name, file_name):
    		threading.Thread.__init__(self)
    		self.threadID 	= threadID
    		self.name 		= name
    		self.file_name 	= file_name
			
    def run(self):
    		print ("Playing %s" % self.name)
    		ask_eir(self.file_name)
    		print ("Finish play sound %s " % self.name)

def ask_eir(file_name):
	try:
		playsound(file_name)#'sounds/eir.wav'
	except:
		print ('Error on Asking for EIR function')

start = time.time()
# Create new threads
camera1_thread = cameraThread(1, "Camera-1","192.168.103.11","gate","Gateview2018", 1)
camera2_thread = cameraThread(2, "Camera-2","192.168.103.12","gate","Gateview2018", 1)
camera3_thread = cameraThread(3, "Camera-3","192.168.103.13","gate","Gateview2018", 1)

eir_sound_thread = outSound(4, "eir",'sounds/eir.wav')

# Start new Threads
eir_sound_thread.start()
camera1_thread.start()
camera2_thread.start()
camera3_thread.start()
# eir_sound_thread.join()
# camera1_thread.join()
# camera2_thread.join()
# camera3_thread.join()
end = time.time()
print('Exiting Main Thread : %s sec(s)' % (end - start))
