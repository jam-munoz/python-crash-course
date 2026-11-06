# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# •Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# •Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# •Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# •Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

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
print("\nI can only invite 2 people for dinner")
while i > 2:
	cancel = people.pop()
	print(f"{cancel}, I'm sorry I can't invite you for dinner")
	i -= 1
while i > 0:
	i -= 1
	print(f"{people[i]}, you're still invited for dinner")
	del people[i]
print(f"List elements: {people}")
