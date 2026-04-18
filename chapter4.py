# - Working With Lists

people = ["Jim", "Abs", "Forloopia"]
for person in people:
  print(person)
print()

print("range(start, stop):")
for value in range(1, 5):
  print(value) 

print("range(stop):")
for value in range(5):
  print(value)

print("range(start, stop, step):")
for value in range(1, 5, 2):
  print(value) 

print("\nmin, max, sum")
r = range(1, 5)
print(min(r))
print(max(r))
print(sum(r))

print("\nList comprehensions:")
squares = [value ** 2 for value in r]
print(squares)

print("\nSome exercises:")
print("4-3:")
for value in range(1, 20):
  print(value)

print("\n4-5:")
mil = range(1, 1_000_001)
print(min(mil))
print(max(mil))
print(sum(mil))

print("\n4-6:")
for value in range(1, 20, 2):
  print(value)

print("\n4-7:")
for value in range(0, 31, 3):
  print(value)

print("\n4-9:")
cubes = [value**3 for value in range(11)]
print(cubes)

print()
print("slicing is cool")
print(people[1:2])
print(people[:2])
print(people[2:])
print(people[:-1])
print(people[::2]) # 3rd optional arg is range

print("You can also loop through slices")
for person in people[:2]:
  print(person)

print("slicing can be used to make a true copy: `people_copy = people[:]`")
people_copy = people[:]

print()
print("Tuples are lists that cannot change - be warned of of errors")
print("- Just swap [] for ()")
tuple_example = ("Jim", "Abs")
print("- tuples with One value still need a comma (unsure why you'd use this anyway)")
tuple_one_example = ("oneval",)
print("- You can't change values in a tuple but you can overwrite the whole object")
tuple_one_example = ("newval",)


print()
print("Python styling rules (as per Python Enhancement Proposal):")
print("- 4 space indents are preferred")  
print("- Make sure that your IDE processes the tab button as four separate spaces and not an actual tab") 
print("- Line length should be no longer than 80 chars (with comments maxing at 72 chars)")
