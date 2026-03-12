# --- DEBUGGING EXAMPLES ---
# 1. I encountered this error: IndexError: list index out of range. 
# I originally wrote: print(foods[5]) to get the last item. 
# I forgot that Python is 0-indexed, so the 5th item is at index 4.

# 2. I encountered this error: TypeError: unsupported operand type(s) for +: 'int' and 'str'
# This happened when trying to sum the 5x5 list containing "?" strings. 
# I fixed it by adding a condition to only add items if they are not equal to "?".

# 3. I encountered this error: SyntaxError: invalid syntax
# I originally forgot the colon (:) at the end of my 'for' loop statement.
# I fixed it by adding the colon to correctly define the block.

# --- 3.1 LIST OPERATIONS ---
foods = ["Pizza", "Sushi", "Tacos", "Pasta", "Burgers"]
print(foods[1]) # Print second food
print(foods[-1]) # Print last food using negative indexing
foods.append("Ice Cream") # Add to end
foods.insert(0, "apple") # Insert at start
del foods[2] # Remove third item
print(len(foods)) # Print length

for food in foods:
    print(food.upper()) # Print each in uppercase

first_and_last = [foods[0], foods[-1]] # Slicing for first and last

if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

# --- 3.2 SLICING AND STRIDING ---
numbers = list(range(21)) # 0 to 20 inclusive

def get_first_15(lst):
    return lst[:15]

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    return lst[::-1][::3]

# Chaining the functions
step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
print("Slicing Result:", step3)

# --- 3.3 NESTED LISTS ---
nested_numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(nested_numbers[2]) # Print third row
print(nested_numbers[1][1]) # Print second item, second row
nested_numbers.append([10, 11, 12]) # Add new row

def sum_nested(lst):
    total = 0
    for row in lst:
        total += sum(row)
    return total

# --- 3.4 CREATE A 5x5 LIST ---
def create_5x5():
    grid = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(num)
            num += 1
        grid.append(row)
    return grid

my_5x5 = create_5x5()

def replace_multiples_of_3(grid):
    for r in range(5):
        for c in range(5):
            if grid[r][c] % 3 == 0:
                grid[r][c] = "?"
    return grid

updated_5x5 = replace_multiples_of_3(my_5x5)

def sum_filtered_grid(grid):
    total = 0
    for row in grid:
        for item in row:
            if item != "?":
                total += item
    return total

# --- 4.1 DICTIONARY OPERATIONS ---
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
if "Mariam" in ages:
    del ages["Mariam"]

for name, age in ages.items():
    print(f"{name}: {age}")

# --- 5.2 CALLING A FAVORITE FUNCTION ---
print("Total sum of non-placeholder values:", sum_filtered_grid(updated_5x5))