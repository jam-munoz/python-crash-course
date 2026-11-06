# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# 	Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# 	call to the end of your program informing people that you found a bigger
# 	dinner table.
# 	Use insert() to add one new guest to the beginning of your list.
# 	Use insert() to add one new guest to the middle of your list.
# 	Use append() to add one new guest to the end of your list.
# 	Print a new set of invitation messages, one for each person in your list.

people = ["Alice", "Bob", "Charlie"]
print(f"{people[0]}, I would like you to come to dinner")
print(f"{people[1]}, I would like you to come to dinner")
print(f"{people[2]}, I would like you to come to dinner")
print(f"{people}, I found a bigger table\n")
people.insert(0, "Dan")
people.insert(len(people) // 2, "Eric")
people.append("Mary")
i = 0
while i < len(people):
	print(f"{people[i]}, I would like you to come to dinner")
	i += 1
