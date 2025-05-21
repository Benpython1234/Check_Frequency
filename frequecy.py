test_dict = {'Codingal':3,'is':2,'best':2,'for':2,'Coding':1,}

print(" Welcome to the Python Dictionary Explorer! \n")
print("Here's our test dictionary:\n")

for key, value in test_dict.items():
    print(f"{key}: {value}")

VALUE_TO_CHECK = int(input("Enter the Value of what frequency you want: "))

Frequency = 0

for VAL in test_dict.values():
    if VAL == VALUE_TO_CHECK:
        Frequency += 1
    
print(f"The frequency of the value {VALUE_TO_CHECK} is: {Frequency}")