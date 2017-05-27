# GUI Tutorial
# Reference: www.raspberrypi.org/learning/getting-started-wth-guis/worksheet/

from guizero import App, Text, TextBox, PushButton, Slider, Picture

# Functions
def say_my_name():
	welcome_message.set( my_name.get() )
	
def change_text_size(slider_value):
	welcome_message.font_size(slider_value)

# Sets app window title
app = App(title="Hello World")

# creates a text box in the window
welcome_message = Text(app, text="Welcome to my application", size=20, font="Verdana", color="purple")

# Creates a text box field in which text can be entered
my_name = TextBox(app, width=100)

# Creates a push button
update_text = PushButton(app, command=say_my_name, text="Display my name")

# Creates a slider
text_size = Slider(app, command=change_text_size, start=10, end=80)

# Adds a picture to the window (this would work if i could find a suitable gif)
my_car = Picture(app, image="car.gif")


app.display()

