# Dictionaries

print("Basically objects")
print("But without dot notation & keys have to be quoted")
alien = {'colour': "blue", 'points': 5}

print(f"\nThe alien is {alien['colour']}")
alien['eyes'] = 4
print(f"The alien has {alien['eyes']} eyes")
del alien['points']
print(alien)

print("\nIf you don't want an error to crash your code when retrieving an value, you can use `dict.get(key, error_message?)`")
point_value = alien.get('points', 'Points value does not exist')
point_value_one_arg = alien.get('points')
print(point_value)
print(point_value_one_arg)

print("\nfor in loops exist in Python - as long as you go through the `items()` (keys):")
for k, v in alien.items():
  print(f"key: {k}, value: {v}")

print("\nOr you could just get `keys()`:")
for k in alien.keys():
  print(f"key = {k}")
print("Oh wait. `keys()` is just the default behaviour anyway. Who needs it!:")
for k in alien:
  print(f"key = {k}")

print("\nAnd `values()` gets the values:")
for v in alien.values():
  print(f"value = {v}")

print("\n`set()` can be used to create a list:")
alien_keys = set(alien.keys())
print(alien_keys)

print("\nHere's how to make a lot of aliens!")
aliens = []
for alien_number in range(30):
  new_alien = {'colour': 'green', 'eyes': 2}
  aliens.append(new_alien)
for alien in aliens[:5]:
  print(alien) # notice how this overwrites the old alien

print(alien) # For some reason, this only changes the last value, which is a ref to the 5th val
alien['colour'] = 'red'
for alien in aliens[:10]:
  print(alien) 

print(f"total number of aliens: {len(aliens)}")

print("\nBtw, you can store List or Dictionaries and nest them as values")
print("You should be able to figure out how to do this")

