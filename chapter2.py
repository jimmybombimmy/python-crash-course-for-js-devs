print("Hello Python World")

message = "message: Why do python variables not have const or let?"
print(message)

message = "message: This message has now changed"
print(message)

title_example = "If I do title_example.title(), each word will start with a capital letter\n"
print(title_example.title())

upper_example = ".upper() changes ALL to UPPERCASE"
print(upper_example.upper())

lower_example = ".lower() changes ALL to lowercase\n"
print(lower_example.lower())

firstname = "ada"
lastname = "lovelace"
fullname = f"{firstname} {lastname}"
print("Putting an 'f' before a string explains that you want to use variables inside of it.")
print(f"Example: {fullname.title()}\n")


rstrip_example = "'.rstrip()' removes all spaces from the end of a string.  "
rstrip_example = rstrip_example.rstrip()
print(rstrip_example)

lstrip_example = "   '.lstrip()' removes all spaces from the start of a string."
lstrip_example = lstrip_example.lstrip()
print(lstrip_example)

strip_example = "   '.strip()' removes all spaces from the start and end of a string.  "
strip_example = strip_example.strip()
print(strip_example)

remove_message_prefix = "Message: \n'removeprefix()' removes a specified prefix from the start of your string."
print(remove_message_prefix.removeprefix("Message: "))

remove_message_suffix = "'removesuffix()' removes a specified prefix from the start of your string. MessageCompleted."
print(remove_message_suffix.removesuffix("MessageCompleted."))

# Page 25 has some tests. Here they are:

# 2-3
pm_name = "Eric"
print(f"\n2-3:\nHello, {pm_name}. Would you like to learn some Python today?")

# 2-4
case_name = "eRiC"
print("\n2-4:\nThe name 'eRiC' in cases:")
print(f"\t Uppercase: {case_name.upper()}")
print(f"\t Lowercase: {case_name.lower()}")
print(f"\t Titlecase: {case_name.title()}")

# 2-5 / 2-6
quote = "A person who has never made a mistake, never tried anything new."
famous_person = "Albert Einstein"
print(f'\n2-5/2-6:\n{famous_person} once said "{quote}"')

# 2-7
name_with_whitespace = "\tAlbert Einstein\t"
print(f"\n2-7:\nName with unneeded spaces: {name_with_whitespace}")
print(f"Name without unneeded spaces spaces: {name_with_whitespace.lstrip().rstrip()}")
# just strip() would have worked here

# 2-8
filename = "filename.py"
print(f"\n2-8:\n Removing .py from {filename} using removesuffix: {filename.removesuffix(".py")}")


print("\n\nNUMBERS:\n")

print(f"\n2 ** 3 = {2 ** 3}")

print("\nFloats are used in any calc that uses them by default")
print(f"Division automatically uses them, regardless of whether a decimal is required: 4 / 2 = {4 / 2}")

big_num = 14_000_000
print("\nbig numbers can have underscores in space of commas when creating a variable")
print(f"e.g. 14_000_000 as a var is used as {big_num}")

a, b, c = 1, 2, 3
print(f"\nYou can set many variables in one line like 'a, b, c = 1, 2, 3': {a, b, c}")

DONT_CHANGE_THIS_NUM = 5000
print("\nPython doesn't have constants, but you can show you think something should be unchanging by putting it in all caps")
print(f"DONT_CHANGE_THIS_NUM = {DONT_CHANGE_THIS_NUM} ")