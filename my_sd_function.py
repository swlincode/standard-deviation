'''Standard Deviation Formula:
Reference: https://www.mathsisfun.com/data/standard-deviation-formulas.html
Step 1: Mean of all values (mu).
Step 2: For each number, subtract the mean and square the result.
Step 3: Add up all the values, then divide by how many.
Step 4: Square root.'''

import math, random

class MyMath:
    def __init__(self, values):
        self.values = values  

    def sd_func(self):
        sum_values = 0  # Step 1
        for i in self.values:
            sum_values += i
        number_values = len(self.values)
        mean_values = sum_values / number_values

        sum_count_values = 0
        for j in self.values:  # Step 2
            sum_count_values += (j - mean_values) ** 2
        variance = sum_count_values / number_values  # Step 3
        sd_result = math.sqrt(variance) # Step 4
        return sd_result

random_range_one_five = random.sample(range(1, 5), 3)
random_values = MyMath(random_range_one_five)
print(random_values.values, "\n", random_values.sd_func())