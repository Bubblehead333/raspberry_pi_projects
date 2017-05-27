# GUI Tutorial
# Reference: www.raspberrypi.org/learning/getting-started-wth-guis/worksheet2/

from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

# Functions
def do_booking():
	info("Booking", "Thankyou for booking")
	print(film_choice.get() )
	print(vip_seat.get_value() )
	print(row_choice.get() )
	
	
	
# Creates our window for our app. This time a size as been defined, as has the layout.
# This grid layout with allow us to position things on our app using co-ordinates
app = App(title="My second GUI app", width=300, height=200, layout="grid")

# Text
film_description = Text(app, text="Which film?", grid=[0,0], align="left")

# Creates a combo with three possible selections
film_choice = Combo(app, options=["Star Wars", "Indiana Jones", "Batman"], grid=[0,1], align="left")

# ext
vip_text = Text(app, text="Seat Type: ", grid=[1,0], align="left")

# Checkbox
vip_seat = CheckBox(app, text="VIP seat?", grid=[1,1], align="left")

# More Text
row_text = Text(app, text="Row Choice: ", grid=[2,0], align="left")

# Button group widget, displays toggle buttons as defined
row_choice = ButtonGroup(app, options=[ ["Front", "F"], ["Middle", "M"],["Back", "B"] ], selected="M", horizontal=True, grid=[2,1], align="left")

# Push button
book_seats = PushButton(app, command=do_booking, text="Book seat", grid=[3,1], align="left")

app.display()
