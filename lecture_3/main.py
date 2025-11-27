"""
This module contains student grade analyzer program.
It is 5 options in program.
"""
from typing import Dict, List, Union

def add_student(
    students_list:List[Dict[str,Union[str, List[int]]]]
) -> list[dict[str, Union[str, list[int]]]]:
    """
This method add a student in student list if the input name is not exist.
Else method indicate that the student already exist.
"""
    input_student_name = input("Enter student name: ").capitalize()
    #if student name invalide, indicate this
    if not input_student_name.replace(' ', '').isalpha():
        print("Invalid input. The name must consist of words wich is consists of letters.")
        return students_list
    #if student exist, indicate this
    for student_info in students_list:
        if input_student_name == student_info['name']:
            print("This student is already exist.")
            return students_list
    #add a new student
    students_list.append({'name' : input_student_name, 'grades' : []})
    return students_list

def add_a_grade_for_a_student(
    students_list:List[Dict[str, Union[str, List[int]]]]
) -> list[dict[str, Union[str, list[int]]]]:
    """
This method add a grades in student grades list if the input name of student is exist.
Else method indicate that the student not exist.
Method can check the validity of the enterd data.
"""
    #if student list is empty, indicate this
    if not students_list:
        print("There are no one student in the list.")
        return students_list
    #if student list is not empty, change student's grades
    input_student_name = input("Enter student name: ").capitalize()

    for student_info in students_list:
        if input_student_name == student_info['name']:
            while True:
                input_data = input("Enter a grade (or 'done' to finish): ")
                if input_data == 'done':
                    return students_list
                else:
                    try:
                        grade = int(input_data)
                        #check the grade
                        if 0 <= grade <= 100:
                            student_info['grades'].append(grade)
                        else:
                            print("Invalid input. Please enter a number between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
    print("This name of student is not found.")
    return students_list

def show_report(
    students_list:List[Dict[str, Union[str, List[int]]]]
) -> None:
    """
This method do report of student average grades.
It use another function for calculating average grades.
"""
    print("--- Student Report ---")
    if not students_list:
        print("There are no one student in the list.")
    else:
        average_grades = list_of_average_grades(students_list)
        not_none_average_grades = [grade for grade in average_grades if grade is not None]
        if not not_none_average_grades:
            print("Students haven't got any grades.")
        else:
            i = 0
            while i < len(students_list):
                if average_grades[i] is None:
                    print(f"{students_list[i].get('name')}'s average grade is N/A.")
                else:
                    print(f"{students_list[i].get('name')}'s average grade is {average_grades[i]}.")
                i += 1
            print("--------------------------")
            print(f"Max Average: {max(not_none_average_grades)}")
            print(f"Min Average: {min(not_none_average_grades)}")
            print("Overall Average:", end=" ")
            print(f"{round(sum(not_none_average_grades)/ len(not_none_average_grades), 1)}")

def list_of_average_grades(
    students_list:List[Dict[str, Union[str, List[int]]]]
) -> list[float]:
    """
This method calculating average grades.
"""
    average_grades:list[float] = []
    for student_info in students_list:
        try:
            average_grade = round(sum(student_info['grades']) / len(student_info['grades']), 1)
            average_grades.append(average_grade)
        except ZeroDivisionError:
            average_grades.append(None)
    return average_grades

def top_performer(
    students_list:List[Dict[str, Union[str, List[int]]]]
) -> None:
    """
This method calculating average grades.
And search max average grade and student with this grade.
Then it output this data into the screen.
"""
    #if student list is empty, indicate this, else search student with max average grade
    if not students_list:
        print("There are no one student in the list.")
    else:
        student_with_max_average_grade = max(students_list,
                        key=lambda student: sum(student['grades'])
                        /len(student['grades']) if student['grades'] else 0)
        if student_with_max_average_grade['grades']:
            max_average_grade = round(sum(
                student_with_max_average_grade['grades'])/len(
                    student_with_max_average_grade['grades']), 1)
            print("The student with the highest average is" , end=" " )
            print(f"{student_with_max_average_grade['name']}", end=" " )
            print(f"with a grade of {max_average_grade}.")
        else:
            print("Students haven't got any grades.")

def main():
    """
This main method which is cantains infinity loop with 5 options.
"""
    students_list:List[Dict[str, Union[str, List[int]]]] = []
    while True:
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student\n"
              "2. Add grades for a student\n"
              "3. Generate a full report\n"
              "4. Find the top student\n"
              "5. Exit programm")
        command = input("Enter your choice: ")
        match command:
            case '1':
                students_list = add_student(students_list)
            case '2':
                students_list = add_a_grade_for_a_student(students_list)
            case '3':
                show_report(students_list)
            case '4':
                top_performer(students_list)
            case '5':
                print("Exiting program.")
                break
            case _:
                print("Invalid input.", end=" ")
                print("Please write the number of command from the list of commands.")

if __name__ == "__main__":
    main()
