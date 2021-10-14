import math
import csv

with open('data.csv',newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0] #starts sorting the data from 0
def mean(data): #finding the mean
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    return mean

squaredlist = []
for number in data: #subtracting the values from the mean and squaring them
    a = int(number) - mean(data)
    a = a**2
    squaredlist.append(a) #adds the values in the list

sum = 0
for i in squaredlist: #adds all the squared values together
    sum = sum+i

result = sum/(len(data) - 1) #divides the sum of the values by number of values - 1
standardDeviation = math.sqrt(result) #takes the square root of the result

print(standardDeviation)