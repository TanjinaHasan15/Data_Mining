given_list = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9]

odd_list = list()
even_list = list()

for number in given_list:
    if number%2==0:
        even_list.append(number)
    else:
        odd_list.append(number)

# print(even_list)
# print(odd_list)

class Stat:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data)/len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        if len(sorted_data)%2==1:
            return sorted_data[len(sorted_data)//2]
        else:
            return (sorted_data[len(sorted_data)//2] + sorted_data[len(sorted_data)//2 - 1])/2

    def mode(self):
        frequency = dict()

        for number in self.data:
            # frequency = {2:1, 4:1,}
            if number not in frequency.keys():
                frequency[number] = 1
            else:
                frequency[number] += 1

        max_frequency = 0

        for number in frequency.keys():
            if frequency[number] > max_frequency:
                max_frequency = frequency[number]
                mode_value = number

        return mode_value

    def display(self):
        print(f"Data: {self.data}")
        print(f"Mean: {self.mean()}")
        print(f"Mode: {self.mode()}")
        print(f"Median: {self.median()}")

Odd_stat = Stat(odd_list)
Even_stat = Stat(even_list)

Odd_stat.display()
Even_stat.display()