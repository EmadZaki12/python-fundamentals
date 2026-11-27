# Student Records Manager
students = [ ("Emad", 20 ,    [ ("python" ,90 ) , ("sql" , 80), ("java",95)  ] ),
             ("Saif" , 21 ,    [ ("python", 75 ) , ("sql" , 46), ("math",60)  ] ),
             ("Tasneem" , 18 , [ ("python", 75 ) , ("sql" , 75), ("java",90)  ] ),
             ("Youssef" , 17 , [ ("python", 45 ) , ("sql" , 65), ("C++",98)   ] ), 
             ("Mahmoud" , 23 , [ ("python", 89 ) , ("sql" , 75), ("java",96)  ] ),               
            ]

def menu():
    print( "1. Display Students ")
    print( "2. Add New Student ")
    print( "3. Calculate Averages ")
    print( "4. Show Top Student and Lowest Student ")
    print( "5. Show Successful Students ")
    print( "6. Search Student ")
    print( "7. Show Unique Subjects ")
    print( "8. Exit ")

     


# display_students(students)
def display_students( student_list ):
    for student in student_list :
         name , age , grade = student
         print(f"Name : {name} | Age : {age} ")
         for subject , score  in grade:            
            print(f"Subjects : {subject} | score : {score}" )
            
         print("__________________")



# Calculate Averages
def calculate_avg(student_list):
    highest_average = 0
    lowest_average = float("inf")
    top_student = ""
    lowest_student = ""

    for student in student_list:
        name, age, grade = student
        total_score = 0

        for subject, score in grade:
            total_score += score

        avg_score = total_score / len(grade)
        print(f"{name}: {avg_score:.2f}")

        if avg_score > highest_average:
            highest_average = avg_score
            top_student = name
        if avg_score < lowest_average:
            lowest_average = avg_score
            lowest_student = name

    return top_student, highest_average, lowest_student, lowest_average

 

# map() and Lambda
map_students = list(map(lambda student:student[0], students))

Avg_grades = lambda student: sum(score for subject, score in student[2]) / len(student[2])
averages = list(map(Avg_grades, students))


# Search Student
def search_student(student_list):
    search_name = input("Enter the name of the student to search: ")
    for student in student_list:
        if student[0] == search_name:
            return student  
    return None


# Add Student
def add_student( student_list):  
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = []
    while True:
        subject = input("Enter subject (or 'done' to finish): ")
        if subject == 'done':
            break
        score = int(input("Enter score: "))
        grade.append((subject, score))
    student_list.append((name, age, grade))    
    print(f"Student {name} added successfully!")



while True :
    menu()
    option = int(input("Enter your option : "))

    if option == 1 :
        display_students(students)
    
    elif option == 2 :
            add_student(students)
    
    elif option == 3 :
            calculate_avg(students)

    elif option == 4 :
          top_student, highest_Average ,lowest_student , lowest_Average = calculate_avg(students)
          print(f"Top student is {top_student} with an average score of {highest_Average:.2f}")
          print(f"Lowest student is {lowest_student} with an average score of {lowest_Average:.2f}")

    
    elif option == 5 :
         successful_student = list(filter(lambda student: Avg_grades(student) >= 60, students))
         print(f"Successful students: {[student[0] for student in successful_student]}")

    elif option == 6 :
          result = search_student(students)

          if result is not None:
                print(result)
          else:
                print("Student not found.")   
    
    elif option == 7 :
          Unique_Subjects = set()
          for student in students:
            for subject, score in student[2]:
                Unique_Subjects.add(subject)
          print(f"Unique subjects: {Unique_Subjects}")    
    
    elif option == 8 :
         break      
    
    else :
         print("Invalid option")