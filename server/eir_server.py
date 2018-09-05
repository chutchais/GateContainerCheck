from flask import Flask
app = Flask(__name__)

def ask_eir(file_name):
    try:
        from playsound import playsound
        playsound(file_name)
    except:
        print ('Error on Asking for EIR function')

import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("8.8.8.8", 80))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

@app.route("/")
def main():
    msg = "Working on " + get_ip()
    return msg

@app.route("/eir")
def eir_sound():
    ask_eir('sounds/eir.wav')
    return "Play EIR Sound"

@app.route("/welcome")
def welcome_sound():
    ask_eir('sounds/welcome.wav')
    return "Play Welcome Sound"

if __name__ == "__main__" :
    app.run()


