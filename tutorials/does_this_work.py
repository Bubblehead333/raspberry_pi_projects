num = int(input("Please enter a number"))

num = num * 2

print(num)

if num < 3:
	print("You entered 1!")
else:
	print("Boo disqualified, not cool")
	
	
class Pokemon(object):
	
	# Defines a Pokemons class, and outputs their attributes
	#
	#
	
	def __init__(self, name, type1):
		self.name = name
		self.type1 = type1
		
	def output(self):
		if name == "Pikachu":
			print("pika pika")
		else:
			print("I do not recognise this Pokemon")
		
		if type1 == 1:
			return "Normal"
		elif type1 == 2:
			return "Fire"
		else:
			return "cantbebotered"
				
Pikachu = Pokemon("Pikachu", 2)

print(Pikachu.output)
		
