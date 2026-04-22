# Chapter 5 - If Statements

if "string" == "string": 
  print("if statements are good")
elif "nocall" == "nocall":
  print("this won't print")
else: 
  print("if statements are bad")

print("yes" == "yes")
print("Upper" != "upper")

print("\n'&&' is 'and' in Python")
age_0 = 21
age_1 = 17
print(age_0 >= 18 and age_1 >= 18)

print("'||' is 'or' in Python")
print(age_0 >= 18 or age_1 >= 18)

print("\nstr in/not in [arr]:")
pizza_toppings = ["mushrooms", "pepperoni", "olives"]
print("mushrooms" in pizza_toppings)
print("pineapples" not in pizza_toppings)

print("\nBe aware that 'True' or 'False' has a starting capital letter:")
t = True
f = False
print(f"{t},{f}")

print()
print("Empty arrays do not trigger as true in if statements")
pizza_toppings2 = []
if pizza_toppings2:
  print("Some fine toppings there boy")
else:
  print("Why do you not want pizza toppings?")