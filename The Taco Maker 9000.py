### taco generator stuff
### taco salad generator stuff also
### include translations n stuff
### make real tacos 

import random
import time

shells = [
		"Hard Shell, ",
		"Soft Shell, "
]

meat = [
		"Shredded Pork, ",
		"Beef, ",
		"Chicken, ",
		"Grilled Steak, ",
		"Fish, "
]

beans = [
		"Black Beans, ",
		"Pinto Beans, "
]

veggies = [
		"Shreded Lettuce, ",
		"Tomatoes, ",
		"Red Bell Peppers, ",
		"Green Bell Peppers, ",
		"Yellow Bell Peppers, ",
		"Banana Peppers, ",
		"Jalapeños Peppers, ",
		"Cilantro, ",
		"Onions, "
]

toppings = [
		"Guacamole",
		"Pico De Gallo",
		"Sour Cream",
		"Shredded Cheese"
]


taco_graphic = r'''
-----------╭╯╭╯╭╯-------------  _____                 _____                   _             _ 
----/▔▔▔▔▔▔▔▔▔\▔\--- |_   _|               |_   _|                 | |           | |
---/      --╭╮--╭╮--   \╮ \---   | | __ _  ___ ___     | |_   _  ___  ___  __| | __ _ _   _| |
---▏    ..________.. ▕╮▕---   | |/ _` |/ __/ _ \    | | | | |/ _ \/ __|/ _` |/ _` | | | | |
---▏                 ▕╮▕---   | | (_| | (_| (_) |   | | |_| |  __/\__ \ (_| | (_| | |_| |_|
---▏    .. \____╱ .. ▕╮▕---   \_/\__,_|\___\___/    \_/\__,_|\___||___/\__,_|\__,_|\__, (_)
---\____________________\/----                                                        __/ |  
							                             |___/       
       
'''

print(taco_graphic)
print("Hola! ") 
print("(Hello!) ")
input("\nContinue... ")

print("\nTienes hambre? ")
print("(Ya hungry?) ")
input("\nContinue... ")

print("\n¿Quieres un taco? ")
print("(Want a Taco?) ")
input("\nContinue... ")

print("\nEste magico script hara un taco para usted, ")
print("No realmente, pero usted entiende. ")
print("(This magical script will make a taco for you, ) ")
print("(not really, but you understand.) ")
input("\nContinue... ")

print("\nHACIENDO")
time.sleep(1)
print("TACO")
time.sleep(0.5)
print("beep")
time.sleep(0.5)
print("boop")
time.sleep(0.5)
print("\nUsted tendra un(You'll have a ) " + random.choice(shells) + "con(with ) " + random.choice(meat) + random.choice(beans) + random.choice(veggies) + random.choice(veggies) + random.choice(veggies) + "y(and ) " + random.choice(toppings) + "." )

while True:
	want_another = input("\nEse le debería sostener. ¿Quieres otro? (si or no) \nThat should hold you. Want another? (yes or no) ")
	if want_another == 'si':
		print("\n¡Bien! ¡Otro! \nAlright! Another! ")
		time.sleep(1)
		print("\nHACIENDO")
		time.sleep(1)
		print("OTRO")
		time.sleep(0.5)
		print("beep")
		time.sleep(0.5)
		print("boop\n")
		time.sleep(0.5)
		print("\nUsted tendra un(You'll have a ) " + random.choice(shells) + "con(with ) " + random.choice(meat) + random.choice(beans) + random.choice(veggies) + random.choice(veggies) + random.choice(veggies) + "y(and ) " + random.choice(toppings) + "." )
	if want_another == 'no':
		print("\nBien, gracias por usar el Taco Maker 9000! \n(Alright, thank you for using the Taco Maker 9000!) ")
		time.sleep(1)
		print("GRACIAS!")
		time.sleep(0.5)
		print("beep")
		time.sleep(0.5)
		print("boop")
		time.sleep(0.5)
		input("\nDisfruta de tu taco. \n(Enjoy your taco.) ")
		exit(0)
