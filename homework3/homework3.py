#3.1 Say Goodbye
def say_goodbye(name):
    print("Goodbye, " + name)

#3.2 Area of a Circle
def area_circle(radius):
    pi = 3.14
    area = pi * (radius ** 2) 
    print("area is", area)

#4.1 Subtract, Multiply and Divide
def subtract(a, b):
    return a - b

def multiply(c, d):
    return c * d

def divide(e, f):
    return e/f

#5.1 What to wear
def temp_range(readings):
    low_temp = min(readings)
    high_temp = max(readings)
    return (low_temp, high_temp)

#5.2 Weekend Check
def is_weekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False

#5.3 Fuel Efficiency
def efficiency(distance, fuel):
    if fuel == 0:
        return 0
    mpg = distance / fuel
    return mpg

#5.4: Data Encryption
def secret_code(number):
    last_digit = number % 10
    remaining = number // 10
    multiplier = 1
    while multiplier <= remaining:
        multiplier = multiplier * 10
    return (last_digit * multiplier) + remaining

#6.1: Oski Stealing
def power(x, y):
    result = 1
    for i in range(y):
        result = result * x
    return result

#6.2: Min & Max
#6.2.1 For Loops
def find_min_for(numbers):
    low = numbers[0]
    for n in numbers:
        if n < low:
            low = n
    return low

def find_max_for(numbers):
    high = numbers[0]
    for n in numbers:
        if n > high:
            high = n
    return high

#6.2.2 While Loops
def find_min_while(numbers):
    low = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] < low:
            low = numbers[i]
        i = i + 1
    return low

def find_max_while(numbers):
    high = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] > high:
            high = numbers[i]
        i = i + 1
    return high

#6.3 Calculating the Sum
def sum(number):
    total = 0
    while number > 0:
        digit = number % 10
        total = total + digit
        number = number // 10
    return total

#7.1 FAVORITE FUNCTION: Lick Observatory Efficiency
# Comparison between two cars, where Car A: 50 miles, 2 gallons used
car_a_efficiency = efficiency(50, 2)
print("Car A MPG:", car_a_efficiency)

# Car B: 50 miles, 3 gallons used
car_b_efficiency = efficiency(50, 3)
print("Car B MPG:", car_b_efficiency)

# Output will show which car is higher
if car_a_efficiency > car_b_efficiency:
    print("Car A is more efficient.")
elif car_b_efficiency > car_a_efficiency:
    print("Car B is more efficient.")
else:
    print("Both cars have the same efficiency.")

print("--- FINAL PROOF ---")
print("Secret Code (1234):", secret_code(1234))
print("Sum of digits (123):", sum(123))