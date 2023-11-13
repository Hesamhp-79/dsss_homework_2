import random


def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within the specified range.
    
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
     """
    Generates a random arithmetic operator from '+', '-', or '*'.
    
    """
    return random.choice(['+', '-', '*'])


def perform_arithmetic_operation(number1, number2, operator):
     """
    Performs an arithmetic operation based on the given numbers and operator.

    """
    problem = f"{number1} {operator} {number2}"
    if operator == '+':
        result = number1 + number2
    elif operator == '-': 
        result = number1 - number2
    else: 
        result = number1 * number2
    return problem, result

def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10);
        num2 = generate_random_integer(1, 5);
        operator = generate_random_operator()

        problem, answer = perform_arithmetic_operation(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer= None

        if user_answer is not None:
            if user_answer == answer:
                print("Correct!You got a point.")
                score+=1
            else:
                print(f"wrong answer. The correct answer is {answer}.")
                
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
