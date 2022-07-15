

from title_yoga import introduction
print(introduction)


def calculator_bmi():
  height = float(input("enter your height in m: "))
  weight = float(input("enter your weight in kg "))

  bmi = round(weight / height ** 2)

  if bmi < 18.5:
    return print(f"Your BMI is {bmi}, you are underweight.")
  elif bmi < 25:
    return print(f"Your BMI is {bmi}, you have a normal weight.")
  elif bmi < 30:
    return print(f"Your BMI is {bmi}, you are slightly overweight.")
  elif bmi < 35:
    return f"Your BMI is {bmi}, you are obese."
  else:
    return f"Your BMI is {bmi}, you are clinically obese."

calculator_bmi()






#examples of exercices
ex_for_beginner=["Trikonasana", "Bhujangasana", "Janu Sirsasana", "Ardha Matsyendrasana","Adho Mukha Svanasana", "Balasana", "Pascimottanasana", "Vrksasana","Ustrasana", "Viparita Karani Mudra", "Virabhadrasana II", "Virasana", "Upavistha", "Baddha konasana"]
ex_for_intermediate=["Bakasana","Urdhva Dhanurasana","Ardha chandrasana", "Natarajasana"]
ex_for_advanced=["Sirszasana","Hanumanasana","Sirsasana II","Pincha Mayurasana","Eka Pada Rajakapotasana"]

print("Welcome to Virtual Yoga Class")

import random

#mix of positions
advanced_class=[]
advanced_class += random.choices(ex_for_beginner, k=3)
advanced_class += random.choices(ex_for_intermediate, k=2)
advanced_class += random.choices(ex_for_advanced, k=3)

intermediate_class=[]
intermediate_class += random.choices(ex_for_beginner, k=5)
intermediate_class += random.choices(ex_for_intermediate, k=3)

def level():
  while True:
    level = input("\nChoose your exercise level. Are you beginner, intermediate or advanced?\n").lower()
    if level == "advanced":
      print(', '.join(advanced_class))
      break
    elif level == "intermediate":
      print(', '.join(intermediate_class))
      break
    elif level == "beginner":
      print(', '.join(random.choices(ex_for_beginner, k=8)))
      break
    else:
      print("\nThat is incorrect, please try again.\n")


def type_exercises():
  while True:
    type = input("\nWould you like to exercises - flow or relaxation?\n").lower()
    if type == "flow":
      print("Stay in position for 30s")
      break
    elif type == "relaxation":
      print("Stay in position for 2 min")
      break
    else:
      print("\nThat is incorrect, please try again.\n")

type_exercises()
level()


from yoga_dictionary import dictionary

description = input("\nWhich of these position you're not familiar with?\n")
print(dictionary[description])


while True:
  continue_ex = input("\nWould you like to continue trening? Yes or No \n").lower()
  if continue_ex== "yes":
    type_exercises()
    level()
  else:
    print("The last position for You is Savasana, please stay for 5 minutes and thank yourself for the practice. ")
    break

