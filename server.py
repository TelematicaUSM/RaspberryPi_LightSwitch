from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

#GPIO Setup
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
#Setup pin 3 as GPIO out to control relay module
GPIO.setup(3,GPIO.OUT)

#define main loop
def main():
    try:
        #Defining routes that can be accessed and their handlers
        rutas = [('/', ListHandler),('/onoff',OnOff)]
        app = Application(rutas, debug=False)
        #app will listen on port 80
        app.listen(80)
        #Starting the server
        IOLoop.current().start()

    except KeyboardInterrupt:
        exit()

class ListHandler(RequestHandler):
    def get(self):
        #Renders the luz.html file
        self.render('luz.html')

    def post(self):
        #On post, change the pin 3 state and reload the page
        GPIO.output(3,not GPIO.input(3))
        self.get()

class OnOff(RequestHandler):
    #This class allows the users to have a direct access to the relay.
    #It shows an empty page but changes the relay state
    def get(self):
        GPIO.output(3,not GPIO.input(3))
        self.write('')

if __name__ == "__main__":
    main()
