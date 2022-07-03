print("Welcome to Virtual Yoga Class")
input("Choose your exercise level. Are you beginner, intermediate or advanced?\n")
input("Would you like to exercises - flow, back pain or relaxation?\n")
exercise=["Trikonasana", "Bhujangasana", "Janu Sirsasana", "Ardha Matsyendrasana","Adho Mukha Svanasana", "Balasana", "Pascimottanasana", "Vrksasana","Ustrasana", "Viparita Karani Mudra", "Virabhadrasana II", "Virasana", "Upavistha", "Baddha konasana"]

import random 
ex=random.choices(exercise, k=10)
print(ex)
