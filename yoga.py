from title_yoga.py import introduction

print("Welcome to Virtual Yoga Class")
input("Choose your exercise level. Are you beginner, intermediate or advanced?\n")
input("Would you like to exercises - flow or relaxation?\n")

ex_for_beginner=["Trikonasana", "Bhujangasana", "Janu Sirsasana", "Ardha Matsyendrasana","Adho Mukha Svanasana", "Balasana", "Pascimottanasana", "Vrksasana","Ustrasana", "Viparita Karani Mudra", "Virabhadrasana II", "Virasana", "Upavistha", "Baddha konasana"]
ex_for_intermediate=["Bakasana","Urdhva Dhanurasana","Ardha chandrasana", "Natarajasana"]
ex_for_advanced=["Sirszasana","Hanumanasana","Sirsasana II","Pincha Mayurasana","Eka Pada Rajakapotasana"]

import random 
ex=random.choices(ex_for_beginner, k=10)
print(ex)
