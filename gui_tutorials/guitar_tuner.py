# Guitar Tuner v 1.0
# 
# Basic UI
# pyQT something to look at for a better interface?

from guizero import App, Combo, Text, CheckBox, ButtonGroup, PushButton, info

# Functions
def update():
	tuning_selection = tuning_presets.get()
	print(tuning_selection)
	if tuning_selection == "Standard Tuning":
		first_string.set("E2")
		second_string.set("A2")
		third_string.set("D3")
		fourth_string.set("G3")
		fifth_string.set("B3")
		sixth_string.set("E4")
	elif tuning_selection == "Drop D":
		first_string.set("D2")
		second_string.set("A2")
		third_string.set("D3")
		fourth_string.set("G3")
		fifth_string.set("B3")
		sixth_string.set("E4")
		
def play1():
	print("Plays audio file: ")
	note = first_string.get()
	print(note)
	
def play2():
	print("Plays audio file: ")
	note = second_string.get()
	print(note)
	
def play3():
	print("Plays audio file: ")
	note = third_string.get()
	print(note)
	
def play4():
	print("Plays audio file: ")
	note = fourth_string.get()
	print(note)
	
def play5():
	print("Plays audio file: ")
	note = fifth_string.get()
	print(note)
	
def play6():
	print("Plays audio file: ")
	note = sixth_string.get()
	print(note)



app = App(title="Guitar Tuner", width=350, height=350, layout="grid")

# Title
main_title = Text(app, text="Guitar Tuner", font="Verdana", size=20, grid=[0,0], color="purple")


# Preset Tunings
tuning_presets = Combo(app, options=["Standard Tuning", "Drop D", "Custom"], grid=[1,0], align="left")


# Update Selections
update = PushButton(app, command=update, text="Update", grid=[0,1], align="right")

# 1st StringDFDFDFDFDF
first_string = Combo(app, options=["C2", "D2", "E2", "F2", "G2", "A2", "B2", "C3"], grid=[2,0], selected="E2", alignSDSD="left")
first_play = PushButton(app, command=play1, text="Play", grid=[2,1], align="right")


# 2nd String
second_string = Combo(app, options=["F2", "G2", "A2", "B2", "C3", "D3", "E3", "F3"], grid=[3,0], selected="A2", align="left")
second_play = PushButton(app, command=play2, text="Play", grid=[3,1], align="right")


# 3rd String
third_string = Combo(app, options=["B2", "C3", "D3", "E3", "F3", "G3", "A3", "B3"], grid=[4,0], selected="D3", align="left")
third_play = PushButton(app, command=play3, text="Play", grid=[4,1], align="right")


# 4th String
fourth_string = Combo(app, options=["E2", "F2", "G3", "A3", "B3", "C4", "D4", "E4"], grid=[5,0], selected="G3", align="left")
fourth_play = PushButton(app, command=play4, text="Play", grid=[5,1], align="right")


# 5th String
fifth_string = Combo(app, options=["G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4"], grid=[6,0], selected="B3", align="left")
fifth_play = PushButton(app, command=play5, text="Play", grid=[6,1], align="right")


# 6th String
sixth_string = Combo(app, options=["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"], grid=[7,0], selected="E4", align="left")
sixth_play = PushButton(app, command=play6, text="Play", grid=[7,1], align="right")




app.display()
