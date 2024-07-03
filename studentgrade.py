#student grade management system
#initialize empty dictionary
student_grade={}
#Add student
def add_student(name,grade):
    student_grade[name]=grade
    print(f"add student with {name} and grade {grade}")


#UPDATE STUDENT DATA
def update_student(name,grade):
    if name in student_grade:
        student_grade[name]=grade
        print("update sucessfully")
    else:
        print("not update with")    
#DELETE STUDENT DATA
def delete_student(name):
    if name in student_grade:
        del student_grade[name]        
        print("deleted sucessfully")
    else:
        print("not deleted")  
#view student
def view_student():
    if student_grade:
        for name,grade in student_grade.items():
            print(f"{name}:{grade}")      
    else:
        print("No student found/added")            
#MAIN FUNCTION
def main():
    while True:
        print("\nstudent grade management system")
        print("1.Add student")
        print("2.Update student")
        print("3.Deleted student")
        print("4.View student")
        print("5.Exit")
        choice=input("Enter your choice =")
        if choice=='1':
            name=input("Enter student name =")
            grade=int(input("Enter student grade ="))
            add_student(name,grade)
        elif choice=='2':
            name=input("Enter student name =")
            grade=int(input("Enter student grade ="))
            update_student(name,grade)
        elif choice=='3':
            name=input("Enter student name =")
            grade=int(input("Enter student grade ="))  
            delete_student(name)  
        elif choice=='4':
            view_student() 
        elif choice=='5':
            print("Closing the Program......")
            break
        else:
            print("Invalid choice")    

main()            

                
                
        
    