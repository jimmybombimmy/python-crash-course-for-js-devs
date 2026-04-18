# Chapter 3 - Introducing Lists

sentence = ["this", "is", "a", "list"]
sentence[0] = sentence[0].title()
print(sentence)
print(sentence[-1].upper())

print()
sentence.append("and an array???")
sentence.insert(2, "both")
print(sentence)

print()
del sentence[2]
popped_item = sentence.pop()
print(sentence)
print(f"I saved my popped item '{popped_item}' as a variable")

print()
sentence.remove("is")
sentence.insert(3, "a")
a_string = "a"
sentence.remove(a_string) # only removes the first instance of "a". Loop to remove all
print(sentence)

print()
sort_sentence = ["sort", "puts", "in", "alphabetical", "order"]
print(sort_sentence)
sort_sentence.sort()
print(sort_sentence)
sort_sentence.sort(reverse=True)
print(sort_sentence)

print()
sort_sentence[0] += "ed"
sort_sentence.insert(0, "temporarily")
print(sorted(sort_sentence))
print(sort_sentence)

print()
sort_sentence2 = ["Sorting", "is", "different", "alphabetically"]
print(sorted(sort_sentence2))

print()
reverse_sentence = ["service", "is", "selling"]
print(reverse_sentence)
reverse_sentence.reverse()
print(reverse_sentence)

reverse_sentence_length = len(reverse_sentence)
print(f"The last sentence has a length of {reverse_sentence_length} - using len()")