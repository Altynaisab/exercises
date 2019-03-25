types_of_people = 10 #amount of types of people
x = f"There are {types_of_people} types of people." #variable for types_of_people

binary = "binary"#variable if know binary
do_not = "don't"#variable of people, that dont know binary
y = f"Those who know {binary} and those who {do_not}."#variable of this text, that gonna be printing

print(x)#printing the x format
print(y)#printing y format
#here could be print('x + y')
print(f"I said: {x}")#print text + x format
print(f"I also said: '{y}'")#print text + y format
#print(f"I said: {x}" + f"I also said: '{y}'")
hilarious = False #for hilarious will be false
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))#print joke_evaluation and after false

w = "This is the left side of..."#variable of this text
e = "a string with a right side."#variable
print(w + e)
