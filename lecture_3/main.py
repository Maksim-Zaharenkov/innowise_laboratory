from typing import Union

#check the raise
def add_student(students_list:list[dict[str, Union[str, list[int]]]]) -> list[dict[str, Union[str, list[int]]]]:
    input_student_name = input("Enter student name: ")

    for student_info in students_list:
        if input_student_name == student_info['name']:
            raise Exception("This name is already exist! Try input another name.")
        
    students_list.append({'name' : input_student_name, 'grades' : []})
    return students_list
    

def add_a_grade_for_a_student(students_list:list[dict[str, Union[str, list[int]]]]) -> list[dict[str, Union[str, list[int]]]]:
    if not students_list:
        print("There are no one student in the list.")
        return students_list
    input_student_name = input("Enter student name: ")

    for student_info in students_list:
        if input_student_name == student_info['name']:
            while True:
                input_data = input("Enter a grade (or 'done' to finish): ")
                if input_data == 'stop':
                    return students_list
                else:
                    try:
                        grade = int(input_data)
                        student_info['grade'].append(grade)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
    return students_list

def show_report(students_list:list[dict[str, Union[str, list[int]]]]):
    print("--- Student Report ---")
    if not students_list:
        print("There are no one student in the list.")
    else:
        list_of_average_grades = list_of_average_grades(students_list)
        filtered_not_none_list_of_average_grades = [grade for grade in list_of_average_grades is not None]
        if not filtered_not_none_list_of_average_grades:
            print("Students haven't got any grades.")
        else:
            i = 0
            while i < len(students_list):
                print(f"{students_list[i].get('name')}'s average grade is {list_of_average_grades[i]}.")
            print("--------------------------")
            print(f"Max Average: {max(filtered_not_none_list_of_average_grades)}")
            print(f"Min Average: {min(filtered_not_none_list_of_average_grades)}")
            print(f"Overall Average: {sum(filtered_not_none_list_of_average_grades) / len(filtered_not_none_list_of_average_grades)}")  

def find_top_performer():
    pass

def list_of_average_grades(students_list:list[dict[str, Union[str, list[int]]]]) -> list[float]:
    list_of_average_grades:list[float] = []
    for student_info in students_list:
        try:
            average_grade = sum(student_info['grades']) / len(student_info['grades'])
            list_of_average_grades.append(average_grade)
        except ZeroDivisionError:
            list_of_average_grades.append(None)
    return list_of_average_grades

def main():
    print("--- Student Grade Analyzer ---")
    print("1. Add a new student\n"
          "2. Add grades for a student\n"
          "3. Generate a full report\n"
          "4. Find the top student\n"
          "5. Exit programm")
    students_list:list[dict[str, Union[str, list[int]]]] = []
    while True:
        command = input("Enter your choice: ")
        match command:
            case 1:
                add_student(students_list)
            case 2:
                add_a_grade_for_a_student(students_list)
            case 3:
                show_report(students_list)
            case 4:
                pass
            case 5:
                print("Exiting program.")
                break

if __name__ == "__main__":
    main()