# let's build a program to measure our weight on different

#  planets and moons in our solar system
name= input("Name?\n")

print("okay " + name + ", are you planing to travel to a different planet, well you should probably know your how much you weigh there first")

weight = int(input("what is your weight in kgs?\n"))

Planets = "mercury, venus, mars, jupiter, saturn "

print("Which planet are you traveling to? Here are the options: \n" + Planets)

choice = input()

mercury_weight= round((weight/9.81)*3.7)

venus_weight= round((weight/9.81)*8.87)

mars_weight= round((weight/9.81)*3.711)

jupiter_weight= round((weight/9.81)*24.79)

saturn_weight= round((weight/9.81)*10.44)

if choice == "mercury":
 
    print(f"your weight on  {choice} is {mercury_weight}")

if choice == "venus":
 
    print(f"your weight on  {choice} is {venus_weight}")

if choice == "mars":
 
    print(f"your weight on  {choice} is {mars_weight}")

if choice == "jupiter":
 
    print(f"your weight on  {choice} is {jupiter_weight}") 

if choice == "saturn":
 
    print(f"your weight on  {choice} is {saturn_weight}")  

print("cool " + name + ", we are preparing your rocket to " + choice +" , pack up your things we are leaving soon")
