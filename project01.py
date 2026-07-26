print("What's your name?")
name = input()

print(f"How old are you {name}?")
age = int(input())

print(f"How much do you weigh {name}?")
weight = int(input())

print(f"How tall are you {name}?")
height = int(input())

print(f"Hello {name}!")
print(f"Age: {age} years old")
print(f"Height: {height} cm")
print(f"Weight: {weight} kg")

gain = 10

print(f"Next year you will be {age + 1} years old.")
print(f"If you gain {gain} kg this year, you will be {weight + gain} kg next year.")
print("Thank you for using my first Python program!")