from title_yoga import introduction
print(introduction)

print("Welcome to Virtual Yoga Class")
input("Choose your exercise level. Are you beginner, intermediate or advanced?\n")
input("Would you like to exercises - flow or relaxation?\n")

ex_for_beginner=["Trikonasana", "Bhujangasana", "Janu Sirsasana", "Ardha Matsyendrasana","Adho Mukha Svanasana", "Balasana", "Pascimottanasana", "Vrksasana","Ustrasana", "Viparita Karani Mudra", "Virabhadrasana II", "Virasana", "Upavistha", "Baddha konasana"]
ex_for_intermediate=["Bakasana","Urdhva Dhanurasana","Ardha chandrasana", "Natarajasana"]
ex_for_advanced=["Sirszasana","Hanumanasana","Sirsasana II","Pincha Mayurasana","Eka Pada Rajakapotasana"]

import random 

advanced_class=[]
advanced_class += random.choices(ex_for_beginner, k=3)
advanced_class += random.choices(ex_for_intermediate,k=2)
advanced_class += random.choices(ex_for_advanced,k=3)

print(', '.join(advanced_class))

intermediate_class=[]
intermediate_class += random.choices(ex_for_beginner, k=5)
intermediate_class += random.choices(ex_for_intermediate,k=4)

print(', '.join(intermediate_class))
