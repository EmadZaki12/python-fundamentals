# =========================
# 1. Basic Functions
# =========================
def fullname (firstname , lastname):
    firstname = firstname.capitalize()
    lastname = lastname.lower()
    return firstname + " " + lastname

firstname = str (input("Enter ur first name "))
lastname  = str (input("Enter ur last name"))

print(fullname(firstname,lastname))

def add (x ,y):
    return x + y
def multiply (x , y):
    return x*y
def sub (x,y):
    return x-y
def divide (x,y):
    if(y==0):
        return ("return "Please enter a non-zero value for y")
    else:
        return x/y

    
x = float(input("enter x num"))
y = float(input("enter y num"))

print (add(x,y))
print(multiply(x,y))
print(sub(x,y))
print(divide(x,y))


def employee(name, salary, department="IT"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Department: {department}")
    print("-" * 20) 


# Positional Arguments 
employee("Emad", 15000, "HR")

# Keyword Arguments 
employee(department="Marketing", name="Sara", salary=12000)

employee("Ahmed", 18000)

def display_name (*args):
    for arg in args:
        print(arg, end=" ")
display_name("DR.","Emad", "Tarek" , "Mohamed")


# =========================
# 2. *args and **kwargs
# =========================

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")



# =========================
# 3. Lambda Functions
# =========================

add = lambda x, y: x + y
print(add(10, 5))

squeard = lambda x : x*x
print(squeard(8))

return_num = lambda x , y : x if(x>y) else y    
print(return_num(10,20))

return_nums = lambda x : True if(x>0) else False
print(return_nums(5))
print(return_nums(-3))


# =========================
# 4. Map and Filter
# =========================
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)

nums = [1, 2, 3, 4, 5]
cubed_nums = list(map(lambda x:x**3 , nums))
print(cubed_nums)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

nums = [12, 5, 20, 3, 15, 8, 30, 7]
bigThann10 = list(filter(lambda x : x>10 , nums))
print(bigThann10)
