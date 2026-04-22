# Chapter 7 - User inputs and while loops

answer = input("QUESTION: `input(MESSAGE)` can be used to allow a user to input an answer? ").lower()
if answer == "y" or answer == "yes":
  print("You're right. It can!")
elif answer == "n" or answer == "no":
  print("Well you're wrong. It can!")
else:
  print("I don't know what you're talking about but it can!")

print()
num_response = input("Give me a number so I can prove that `int()` will turn it into an integer. ")
num_inted = int(num_response)
print(f'Your number + 10 = {num_inted + 10}')

print("\nIntroducing while loops in...")
current_num = 5
while current_num > 0:
  print(current_num)
  current_num -= 1
print("Introduced!")

print("\nFlags can be used to ensure some logic runs as long as it's True")
active = True
while active:
  inp = input("Type 'q' or 'quit' to quite this loop... ").lower()
  if inp == 'q' or inp == 'quit':
    active = False
    print("The `active` flag was set to false and we exited the program!")

print("\n`break` exists to exit loops too")
active = True
while active:
  inp = input("Type something here. I'll exit if you don't... ")
  if inp == "":
    break
print("Exited")

print("Bonus: `continue` also exists to skip to the next iteration of the loop")
print("Like break, this is a fairly obvious one I've used before in JS. No need for an example.")