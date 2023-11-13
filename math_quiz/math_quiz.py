import random

def generate_random_number(min_value, max_value):
    """
    Generate a random integer between min_value and max_value.

    Args:
    min_value (int): Minimum value of the range.
    max_value (int): Maximum value of the range.

    Returns:
    int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def choose_random_operator():
    """
    Choose a random arithmetic operator from '+', '-', or '*'.

    Returns:
    str: A random arithmetic operator.
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(num1, num2, operator):
    """
    Create a math problem and calculate its answer.

    Args:
    num1 (int): The first number.
    num2 (int): The second number.
    operator (str): The arithmetic operator.

    Returns:
    tuple: A tuple containing the math problem as a string and its answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_number(1, 10)
        num2 = generate_random_number(1, 10)  # Fixed the range to be integers
        operator = choose_random_operator()

        problem, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
