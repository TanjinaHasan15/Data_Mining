'''
Create a class Student to store marks of students in different subjects.

Take a list of student marks (for example: [56, 72, 89, 45, 90, 67, 38]).

Divide the marks into two lists:

Pass list (marks ≥ 50)

Fail list (marks < 50)

For each list, calculate:

Highest score

Lowest score

Average score

Store the results in a dictionary with keys "Pass" and "Fail".

Display the dictionary neatly.
'''

# student marks
marks_list = [56, 72, 89, 45, 90, 67, 38]

# Separate marks --> Pass and Fail lists
pass_list = list()
fail_list = list()

for mark in marks_list:
    if mark >= 50:
        pass_list.append(mark)
    else:
        fail_list.append(mark)

# Class to calculate statistics
class Student:
    def __init__(self, data):
        self.data = data

    def highest(self):
        return max(self.data) if self.data else 0

    def lowest(self):
        return min(self.data) if self.data else 0

    def average(self):
        return sum(self.data)/len(self.data) if self.data else 0

    def display(self):
        print(f"Data: {self.data}")
        print(f"Highest: {self.highest()}")
        print(f"Lowest: {self.lowest()}")
        print(f"Average: {self.average():.2f}")

# Create objects for Pass and Fail lists
Pass_stat = Student(pass_list)
Fail_stat = Student(fail_list)

# Display results for both groups
print("Pass List Statistics:")
Pass_stat.display()

print("\nFail List Statistics:")
Fail_stat.display()

# Store in dictionary
result = {
    "Pass": {
        "Highest": Pass_stat.highest(),
        "Lowest": Pass_stat.lowest(),
        "Average": round(Pass_stat.average(), 2)
    },
    "Fail": {
        "Highest": Fail_stat.highest(),
        "Lowest": Fail_stat.lowest(),
        "Average": round(Fail_stat.average(), 2)
    }
}

# Display dictionary 
print("\nFinal Results Dictionary:")
print(result)
