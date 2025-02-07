import sys
import random


def lucky_one_true(input_dict):
    lucky_one = random.choice(list(key for key in friends.keys()))
    print(f"\n{lucky_one} is the lucky one")
    split_amount = round(total_bill / (count - 1), 2)
    return {key: (split_amount if key != lucky_one else 0) for (key, value) in input_dict.items()}


def lucky_one_false(input_dict):
    print("\nNo one is going to be lucky")
    split_amount = round(total_bill / count, 2)
    return {key: split_amount for (key, value) in input_dict.items()}


count = int(input("Enter the number of friends joining (including you):\n"))

if count <= 0:
    print("\nNo one is joining for the party")
    sys.exit()

friends = dict()
print("\nEnter the name of every friend (including you), each on a new line:")

for i in range(count):
    friends[input()] = 0

total_bill = int(input("\nEnter the total bill value:\n"))

lucky_one_active = input("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:\n")

if lucky_one_active == "Yes":
    print(f"\n{lucky_one_true(friends)}")
else:
    print(f"\n{lucky_one_false(friends)}")