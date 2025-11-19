def main():
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    current_age = 2025 - birth_year
    hobbies: list[str] = []
    while True:
        next_input = input("Enter a favorite hobby or type 'stop' to finish: ")
        if next_input == "stop":
            pass
        else:
            hobbies.append(next_input)


def generate_profile(age: int) -> str:
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"