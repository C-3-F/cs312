# def generate_extended_alphabet(length):
#     alphabet = [chr(ord('a') + i) for i in range(26)]  # Generate alphabet list
#     sequence = []
#     counter = 0
#     while len(sequence) < length:
#         if counter < 26:  # First, use single letters
#             sequence.append(alphabet[counter])
#         else:  # Then repeat letters, increasing the repetition for each new cycle
#             repeat_times = counter // 26 + 1
#             sequence.extend([alphabet[i] * repeat_times for i in range(26)])
#         counter += 1
#     return sequence[:length]  # Trim the sequence to the exact needed length

# def create_dynamic_2d_array(rows, cols):
#     total_elements = rows * cols
#     sequence = generate_extended_alphabet(total_elements)
#     array = [[sequence[i*cols + j] for j in range(cols)] for i in range(rows)]
#     return array

# # Specify the dimensions
# rows, cols = 10, 10  # Example: 10x10 array. Adjust as needed.

# # Create the 2D array with dynamic dimensions
# arr = create_dynamic_2d_array(rows, cols)

# # Display the array
# for row in arr:
#     print(row)


# # Output:

list = [] 
for i in range(10 + 1):
    list.append([''] * (10 + 1))
for i in range(1,11):
    for j in range(1,11):
        list[i][j] = chr(ord('a') + i -1 ) + chr(ord('a') + j - 1)

# Display the array
for row in list:
    print(row)



band = 3
k = 2 * band + 1
newList = []

for i in range(10 + 1):
    newList.append(['  '] * (k + 1))

# for i in range(10 + 1):
#     for j in range(min(k, i + band)):
#         col = j
#         comp = max(i - band,1) + j
#         if comp < 1:
#             comp = 1
#         if comp > k:
#             comp = k
#         newList[i][col] = list[i][comp]
    
skip = 0
for i in range(1,11):
    index = 1
    if i > 10 - band:
        skip += 1
    for j in range(i - band, i + band + 1):
        if j < 1:
            continue
        if index + skip > k:
            break
        newList[i][index + skip] = list[i][j]
        index += 1
        

print('\n')
print('*********************************')
print('\n')
for row in newList:
    print(row)