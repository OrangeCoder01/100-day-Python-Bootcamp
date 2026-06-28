st = input("Enter String: ")

# Code War Challenge {Suzuki needs help lining up his students!}

st = st + " " 
# string parsing - space detection method must anticipate a space at the end of string, otherwise the last name won't be enlisted

list_length = len(st)
singular_char = 0
singular_name = []
name_list = []
new_name_flag = False

j = -1

for char in st:
    singular_char = ord(char)

    if singular_char == 32: # Space detection
        new_name_flag = True
        j += 1
    else:
        singular_name.append(singular_char)

    if new_name_flag:
        i = 0
        name_list.append("")

        while i < len(singular_name): 
            name_list[j] = name_list[j] + chr(singular_name[i])
            i += 1
        
        singular_name.clear()

        new_name_flag = False


print("The clear list of name: ", name_list[0 : len(name_list)])

# Since the list of names are filtered, now there are cascaded methods for sorting names

# Sorting (1): Length sorting by size

name_length_each = []
stored_name_length_each = []
sorted_name_length_each = []

original_indices_map = []
sorted_name_indx = []

max_len = 0
step = -1

for i in range(0, len(name_list), 1): # Extracting the lengths and produce indices
    name_length_each.append(len(name_list[i]))
    stored_name_length_each.append(len(name_list[i]))
    original_indices_map.append(i)

for compared_current_position_indx in range(0, len(name_list), 1): # The variable naming is confusing but crucial for clarifications in the nested loops
    sorted_name_indx.append(0)
    sorted_name_length_each.append(0)

    max_len = 0
    step += 1

    max_indx = compared_current_position_indx

    for comparing_to_position_indx in range(0 + step, len(name_list), 1): # step fixes the comparision of previously sorted elements

        if name_length_each[comparing_to_position_indx] > max_len:

            max_len = name_length_each[comparing_to_position_indx]
            max_indx = comparing_to_position_indx

    original_unchanged_indx = original_indices_map[max_indx] # assign the value of the index with the stored original index's index
    # Swapping with value
    temp = name_length_each[compared_current_position_indx] # 3rd party swapper agent (stores values before swapping)
    name_length_each[compared_current_position_indx] = name_length_each[max_indx] # Swapping
    name_length_each[max_indx] = temp # assign the replaced element into the position of the replacing elements's position

    # Swapping with indices
    temp_idx = original_indices_map[compared_current_position_indx]
    original_indices_map[compared_current_position_indx] = original_indices_map[max_indx]
    original_indices_map[max_indx] = temp_idx

    # Assigning to sorted values and indices arrays
    sorted_name_indx[compared_current_position_indx] = original_unchanged_indx
    sorted_name_length_each[compared_current_position_indx] = max_len


print("The original lengths are:", stored_name_length_each[0 : len(stored_name_length_each)])
print("The sorted lengths:", sorted_name_length_each[0 : len(sorted_name_length_each)])
print("The sorted indices:", sorted_name_indx[0 : len(sorted_name_indx)])


# Now take the array of indices and substitute in the array of string names:
sorted_name_list = [""]*len(name_list)

for i in range(0, len(name_list), 1):
    sorted_name_list[i] = name_list[sorted_name_indx[i]]

print("The sorted Names sorted by length are:", sorted_name_list[0 : len(sorted_name_list)])


# Sorting (2) ASCII sorting
max_name_length = sorted_name_length_each[0]

# Transforming into string Matrix 
# The rows are the name, the columns are the letters

num_rows, num_columns = len(sorted_name_list), max_name_length

print(f"There are {num_rows} numbers of rows and {num_columns} number of Columns!")

# populate the matrix with characters
name_letter_matrix = []

for i in range(num_rows):
    row = []
    for char in sorted_name_list[i]:
        row.append(char)

    name_letter_matrix.append(row)

for i in range(num_rows):
    if i == 0:
        print("Character Matrix: ")
    print(name_letter_matrix[i])

# transforming the characters to ASCII again
name_ascii_matrix = []

for row_name in range(num_rows):
    name_ascii_row = []
    col_char = -1
    counter_for_zero_avoidance = 0

    for char in sorted_name_list[row_name]:
        if counter_for_zero_avoidance < len(sorted_name_list[row_name]):
            col_char += 1
            name_ascii_row.append(ord(name_letter_matrix[row_name][col_char]))
            counter_for_zero_avoidance +=1

    name_ascii_matrix.append(name_ascii_row)


for i in range(num_rows):
    if i == 0:
        print("ASCII Value Matrix: ")
    print(name_ascii_matrix[i])

# index Matrix for the names with equivalent lengths

indices_matrix = []

for i in range(num_rows):
    current_length = sorted_name_length_each[i]
    j = -1
    row_index = []
    for char in sorted_name_length_each:
        j += 1
        if current_length == sorted_name_length_each[j]:
            row_index.append(j)

    if row_index not in indices_matrix:   # Removes redundancy
        indices_matrix.append(row_index)

for i in range(len(indices_matrix)):
    if i == 0:
        print("Indices of equivalent name lengths in ASCII Value Matrix: ")
    print(indices_matrix[i])

# Sorting the similar arrays of identical number of length size

sorted_name_ascii_matrix = []

for i in range(len(name_ascii_matrix)):
    row = []
    for int in name_ascii_matrix[i]:
        row.append(int)

    sorted_name_ascii_matrix.append(row)


for group in range(len(indices_matrix)):
    current_group_indices = indices_matrix[group]
    group_size = len(current_group_indices)
    
    for pass_num in range(group_size):
        for element_idx in range(0, group_size - pass_num - 1):

            global_idx1 = current_group_indices[element_idx]
            global_idx2 = current_group_indices[element_idx + 1]
            
            row1 = sorted_name_ascii_matrix[global_idx1]
            row2 = sorted_name_ascii_matrix[global_idx2]
            
            should_swap = False
            min_length = len(row1)
            
            for char_pos in range(min_length):
                if row1[char_pos] < row2[char_pos]:
                    should_swap = True
                    break
                elif row1[char_pos] > row2[char_pos]:
                    break

            if should_swap:
                temp_row = sorted_name_ascii_matrix[global_idx1]
                sorted_name_ascii_matrix[global_idx1] = sorted_name_ascii_matrix[global_idx2]
                sorted_name_ascii_matrix[global_idx2] = temp_row


for i in range(len(name_ascii_matrix)):
    if i == 0:
        print("Sorted ASCII Value Matrix: ")
    print(sorted_name_ascii_matrix[i])
    
# Convert them back to characters
sorted_name_char_matrix = []

for i in range(len(sorted_name_ascii_matrix)):
    row = []
    for item in sorted_name_ascii_matrix[i]:
        row.append(chr(item))
        
    sorted_name_char_matrix.append(row)
    

for i in range(len(sorted_name_ascii_matrix)):
    if i == 0:
        print("The sorted character Matrix: ")
    print(sorted_name_char_matrix[i])
    
# Concatenating into string
sorted_name_string_matrix = []

for i in range(len(sorted_name_char_matrix)):
    name_string = ""
    j = 0
    for char in sorted_name_char_matrix[i]:
        name_string = name_string + sorted_name_char_matrix[i][j]
        j += 1

    sorted_name_string_matrix.append(name_string)
    
for i in range(len(sorted_name_string_matrix)):
    if i == 0:
        print("The Final list:")
        
    print(sorted_name_string_matrix[i])
    
 