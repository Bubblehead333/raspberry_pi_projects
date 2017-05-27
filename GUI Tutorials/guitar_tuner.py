# Guitar Tuner v 1.0

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
	pass






app = App(title="Guitar Tuner", width=300, height=300, layout="grid")

# Title
main_title = Text(app, text="Guitar Tuner", font="Verdana", size=20, grid=[0,0], color="purple")


# Preset Tunings
tuning_presets = Combo(app, options=["Standard Tuning", "Drop D", "Custom"], grid=[1,0], align="left")


# Update Selections
update = PushButton(app, command=update, text="Update", grid=[0,1], align="right")

# 1st String
first_string = Combo(app, options=["C2", "D2", "E2", "F2", "G2", "A2", "B2", "C3"], grid=[2,0], selected="E2", align="left")
first_play = PushButton(app, command=play1, text="Play", grid=[2,1], align="right")


# 2nd String
second_string = Combo(app, options=["F2", "G2", "A2", "B2", "C3", "D3", "E3", "F3"], grid=[3,0], selected="A2", align="left")


# 3rd String
third_string = Combo(app, options=["B2", "C3", "D3", "E3", "F3", "G3", "A3", "B3"], grid=[4,0], selected="D3", align="left")


# 4th String
fourth_string = Combo(app, options=["E2", "F2", "G3", "A3", "B3", "C4", "D4", "E4"], grid=[5,0], selected="G3", align="left")


# 5th String
fifth_string = Combo(app, options=["G3", "A3", "B3", "C4", "D4", "E4", "F4", "G4"], grid=[6,0], selected="B3", align="left")


# 6th String
sixth_string = Combo(app, options=["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"], grid=[7,0], selected="E4", align="left")




app.display()
print(tuning_presets)
