food = ["1:Appam", "2:Noodle", "3:Roti", "4:Dosa"]
print(food)
"""choice=int(input("Enter your choice"))
if choice == 1:
    print("Your choice is" + food[0])
elif choice ==2:
    print("Your choice is" + food[1])
elif choice == 3:
    print("Your choice is" + food[2])
elif choice == 4:
    print("Your choice is" + food[3])
else:
    print("Invalid option")"""
choice = input("Enter your choice")
for item in food:
    if choice == item:
        print("Your choice is" + choice)
        break
else:
    print("Invalid choice")
        