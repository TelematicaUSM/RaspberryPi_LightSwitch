from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

import RPi.GPIO as GPIO


def main():
    """Execute the application."""
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(3, GPIO.OUT)

        routes = [('/', ListHandler), ('/onoff', OnOff)]
        app = Application(routes, debug=False)
        app.listen(80)
        IOLoop.instance().start()

    except KeyboardInterrupt:
        exit()

class ListHandler(RequestHandler):
    def get(self):
        """Render the luz.html file."""
        self.render('luz.html')

    def post(self):
        """Change the pin 3 state and reload the page."""
        GPIO.output(3, not GPIO.input(3))
        self.get()


class OnOff(RequestHandler):
    """Allows the user to have a direct access to the relay."""

    def get(self):
        """Show an empty page but changes the relay state."""
        GPIO.output(3, not GPIO.input(3))
        self.write('')

if __name__ == "__main__":
    main()
