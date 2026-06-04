def sum_of_array(arr):
  total = 0  # Initialize a variable to store the sum
  for element in arr:
    total += element  # Add each element to the total
  return total
array = [1, 2, 3]
result = sum_of_array(array)
print("Sum of the array:", result)
