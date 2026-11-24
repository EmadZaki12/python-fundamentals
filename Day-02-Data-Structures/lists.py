# collections = single data structure that can hold multiple items. In Python, there are several built-in data structures, including lists, tuples, sets, and dictionaries. Each of these data structures has its own characteristics and use cases.
# list = [] orderd and changeable , Allows duplicate members. 
# set = {} unordered and unchangeable , No duplicate members but can be modified(add/remove).
# tuple = () ordered and unchangeable , Allows duplicate members and faster.

# Lists
fruitus = ["apple", "banana", "orange", "mango"]
print(fruitus) , print(type(fruitus)) , print(len(fruitus)) , print(fruitus[0]) , 
print(fruitus[-1]) , print(fruitus[:3]) , print(fruitus[:2]) , print(fruitus[2:]) ,
print(fruitus[-3:-1]) , print ("apple" in fruitus) , 
print ("grape: in fruitus? ", "grape" in fruitus) ,
for fruit in fruitus:
    print(fruit)
fruitus[1]= "pieapple"
fruitus.append("kiwi")
fruitus.remove("orange")
fruitus.insert(1, "grape")
print(fruitus.index("mango"))
print(fruitus)
fruitus.sort()
print(fruitus)
fruitus.reverse()
print(fruitus)

numbers = [15, 3, 8, 20, 1, 12]
numbers.sort()
print(numbers)
print(max(numbers))
print(min(numbers))
laregest = numbers[5]
print("The largest number is:", laregest)
minimum = numbers[0]    
print("The minimum number is:", minimum)
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("The largest number is:", largest)

minimum = numbers[0]
for num in numbers:
    if num < minimum:
        miinmum = num
print("The minimum number is:", minimum)
numbers.append(30)
print("After appending 30:", numbers)
numbers.remove(3)
print("After removing 3:", numbers)
numbers.sort(reverse=True)
print(numbers)


# Sets
fruits = {"banana" , "apple" , "kiwi" , "pineapple" }
print (fruits)
print(len(fruits))
fruits.add("orange")
print(fruits)
print ("orange" in fruits)
fruits.remove("apple")
print(fruits)
fruits.pop
print(fruits)
fruits.update({"apple , mango"})
fruits.discard("kiwi")
print(fruits)

students_python = {"Emad", "Ahmed", "Omar", "Ali"}
students_sql = {"Emad", "Mona", "Ali", "Sara"}

print("All students:", students_python.union(students_sql))

print("Both courses:", students_python.intersection(students_sql))

print("Python only:", students_python.difference(students_sql))

print("Only one course:", students_python.symmetric_difference(students_sql))


# Tupls
student = ("Emad", 20, "CIC", "Computer Science")

print(student)
print(type(student))
print(len(student))

print(student[0])
print(student[-1])
print(student[1:3])

print(student.count("CIC"))
print(student.index(20))

name, age, university, major = student

print(name)
print(age)
print(university)
print(major)