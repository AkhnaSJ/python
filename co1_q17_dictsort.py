dictionary = {5: "ball", 8: "pink", 2: "banana", 6: "bee", 1: "toy", 3: "sky"}

print("Ascending: ",dict(sorted(dictionary.items())))
print("Descending: ",dict(sorted(dictionary.items(), reverse = True)))