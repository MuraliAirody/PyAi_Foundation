import ast
import sys

def evaluate_answer(user_code):
    """
    Evaluate the user-provided code safely and return (True, result) if valid,
    otherwise return (False, error_message). Only a restricted set of nodes,
    functions, and attributes are allowed.
    """
    try:
        tree = ast.parse(user_code, mode='exec')
    except Exception as e:
        return False, f"Syntax Error: {e}"

    allowed_nodes = (
        ast.Module, ast.Expr, ast.Assign,
        ast.Name, ast.Constant, ast.Num, ast.Str,
        ast.BinOp, ast.UnaryOp, ast.UAdd, ast.USub,
        ast.BoolOp, ast.Compare, ast.Call, ast.Attribute,
        ast.List, ast.Tuple,
        ast.Load, ast.Store,
        ast.Add, ast.Sub, ast.Mult, ast.Div,
        ast.FloorDiv, ast.Mod, ast.Pow, ast.LShift, ast.RShift,
        ast.BitAnd, ast.BitOr, ast.BitXor, ast.Invert,
        ast.Not, ast.And, ast.Or, ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE,
        ast.Is, ast.IsNot
    )
    allowed_call_funcs = {'int', 'float', 'complex', 'bool', 'type', 'isinstance', 'abs'}
    allowed_attr = {'real', 'imag'}

    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            return False, f"Disallowed code: {type(node).__name__}"
        if isinstance(node, ast.Call):
            func = node.func
            if isinstance(func, ast.Name):
                if func.id not in allowed_call_funcs:
                    return False, f"Use of function '{func.id}' is not allowed."
            else:
                return False, "Only direct calls to allowed functions are permitted."
        if isinstance(node, ast.Attribute):
            if node.attr not in allowed_attr:
                return False, f"Attribute '{node.attr}' is not allowed."

    safe_env = {"__builtins__": None}
    safe_env.update({
        'int': int, 'float': float, 'complex': complex,
        'bool': bool, 'type': type, 'isinstance': isinstance,
        'abs': abs
    })

    try:
        exec(user_code, safe_env)
    except Exception as e:
        return False, f"Error in code execution: {e}"
    if 'result' not in safe_env:
        return False, "The variable 'result' was not set."
    return True, safe_env['result']

def run_quiz(questions, topic_name):
    """
    Present questions to the user. Repeat each question until they answer correctly.
    Displays the output of the user's code on each attempt.
    Users can type 'exit' at any time to quit the program.
    """
    print(f"\nStarting quiz on {topic_name} type. There are {len(questions)} questions.")
    # Allow user to exit before starting
    resp = input("Press Enter to start... (type 'exit' to quit)")
    if isinstance(resp, str) and resp.strip().lower() == 'exit':
        print("Exiting. Goodbye!")
        sys.exit()
    correct_count = 0

    for i, q in enumerate(questions, start=1):
        # Repeat the question until correct
        while True:
            print(f"\nQuestion {i}: {q['prompt']}")
            print("Enter your code below (press Enter on empty line to finish):")
            lines = []
            while True:
                try:
                    line = input()
                except EOFError:
                    line = ''
                # Allow user to exit at any point during code entry
                line_stripped = line.strip()
                if line_stripped.lower() == "exit":
                    print("Exiting. Goodbye!")
                    sys.exit()
                if line_stripped == "":
                    break
                lines.append(line)
            user_code = "\n".join(lines)

            success, response = evaluate_answer(user_code)
            # Show output if code executed successfully
            if success:
                user_result = response
                print(f"Your code output: {user_result!r}")
                expected = q['expected']
                # Compare results
                correct = False
                if expected is None:
                    correct = (user_result is None)
                elif isinstance(expected, float):
                    try:
                        correct = abs(user_result - expected) < 1e-9
                    except Exception:
                        correct = False
                else:
                    correct = (user_result == expected)

                if correct:
                    print("Correct!")
                    correct_count += 1
                    break  # Move on to the next question
                else:
                    print(f"Incorrect. Expected {expected!r}, got {user_result!r}.")
                    print("Please try again.")
                    continue
            else:
                # If code failed to execute or used disallowed constructs, show the error
                print("Incorrect.", response)
                print("Please try again.")
                continue  # Ask the same question again

    print(f"\nTopic '{topic_name}' completed. You answered all questions correctly after multiple attempts.")
    score_percent = correct_count * 100 / len(questions)
    print(f"Your score: {correct_count}/{len(questions)} ({score_percent:.1f}%).")
    if score_percent >= 90:
        print("Excellent work!")
    elif score_percent >= 70:
        print("Good job! Keep practicing to improve further.")
    elif score_percent >= 50:
        print("Not bad, but there's room for improvement.")
    else:
        print("Keep practicing and you'll get better!")
    resp_end = input("Press Enter to return to the main menu... (type 'exit' to quit)")
    if isinstance(resp_end, str) and resp_end.strip().lower() == 'exit':
        print("Exiting. Goodbye!")
        sys.exit()

def main():
    """
    Defines the question sets and menu logic, and starts the quiz based on user input.
    Allows the user to exit at any time by typing 'exit'.
    """
    integer_questions = [
        {"prompt": "Assign the integer 10 to variable 'result'.", "expected": 10},
        {"prompt": "Add 5 and 7 and store the sum in 'result'.", "expected": 12},
        {"prompt": "Subtract 8 from 15 and store the difference in 'result'.", "expected": 7},
        {"prompt": "Multiply 6 by 7 and store the product in 'result'.", "expected": 42},
        {"prompt": "Perform integer division of 20 by 5 using '//' and store the result in 'result'.", "expected": 4},
        {"prompt": "Compute the integer division of 9 by 2 using '//' and store the result in 'result'.", "expected": 4},
        {"prompt": "Compute 2 to the power of 4 (2**4) and store the result in 'result'.", "expected": 16},
        {"prompt": "Compute 7 modulo 3 (7 % 3) and store the result in 'result'.", "expected": 1},
        {"prompt": "Compute -3 modulo 5 (-3 % 5) and store the result in 'result'.", "expected": 2},
        {"prompt": "Compute (5 + 3) * 2 and store the result in 'result'.", "expected": 16},
        {"prompt": "Compute 10 - (2 + 3) and store the result in 'result'.", "expected": 5},
        {"prompt": "Check if 5 is greater than 3 and store the boolean result in 'result'.", "expected": True},
        {"prompt": "Check if 5 is less than 2 and store the boolean result in 'result'.", "expected": False},
        {"prompt": "Check if 5 is equal to 5 and store the boolean result in 'result'.", "expected": True},
        {"prompt": "Check if 6 is not equal to 7 and store the boolean result in 'result'.", "expected": True},
        {"prompt": "Compute the absolute value of -15 and store it in 'result'.", "expected": 15},
        {"prompt": "Convert the string '123' to an integer and store it in 'result'.", "expected": 123},
        {"prompt": "What is the type of 123? Store the result (type) in 'result'.", "expected": int},
        {"prompt": "Compute 123 + 456 and store the result in 'result'.", "expected": 579},
        {"prompt": "Compute 123 * 2 and store the result in 'result'.", "expected": 246},
        {"prompt": "Compute -5 * 4 and store the result in 'result'.", "expected": -20},
        {"prompt": "Compute 7 - 12 and store the result in 'result'.", "expected": -5},
        {"prompt": "Compute the bitwise AND of 6 and 3 and store the result in 'result'.", "expected": 2},
        {"prompt": "Compute the bitwise OR of 6 and 3 and store the result in 'result'.", "expected": 7},
        {"prompt": "Compute 1 shifted left by 3 (1 << 3) and store the result in 'result'.", "expected": 8}
    ]

    float_questions = [
        {"prompt": "Assign the float 10.5 to variable 'result'.", "expected": 10.5},
        {"prompt": "Add 2.5 and 4.5 and store the sum in 'result'.", "expected": 7.0},
        {"prompt": "Subtract 5.5 from 10.0 and store the result in 'result'.", "expected": 4.5},
        {"prompt": "Multiply 2.5 by 4 and store the result in 'result'.", "expected": 10.0},
        {"prompt": "Divide 9.0 by 2.0 using '/' and store the result in 'result'.", "expected": 4.5},
        {"prompt": "Divide 9.0 by 2.0 using '//' (floor division) and store the result in 'result'.", "expected": 4.0},
        {"prompt": "Compute 2.5 to the power of 2 (2.5**2) and store the result in 'result'.", "expected": 6.25},
        {"prompt": "Multiply 2 by 3.5 and store the result in 'result'.", "expected": 7.0},
        {"prompt": "Compute 7.5 modulo 2 (7.5 % 2) and store the result in 'result'.", "expected": 1.5},
        {"prompt": "Convert the integer 7 to a float and store it in 'result'.", "expected": 7.0},
        {"prompt": "Convert the string '3.14' to a float and store it in 'result'.", "expected": 3.14},
        {"prompt": "What is the type of 3.14? Store the result (type) in 'result'.", "expected": float},
        {"prompt": "Check if 3.0 is an instance of float and store the result in 'result'.", "expected": True},
        {"prompt": "Check if 3 is an instance of float and store the result in 'result'.", "expected": False},
        {"prompt": "Compute 0.1 + 0.2 == 0.3 and store the boolean result in 'result'.", "expected": False},
        {"prompt": "Compute 0.1 + 0.2 and store the result in 'result'.", "expected": 0.30000000000000004},
        {"prompt": "Convert 0.0 to a boolean using bool() and store the result in 'result'.", "expected": False},
        {"prompt": "Convert 0.1 to a boolean using bool() and store the result in 'result'.", "expected": True},
        {"prompt": "Compute 3 / 2 and store the result in 'result'.", "expected": 1.5},
        {"prompt": "Compute 5.5 // 2 and store the result in 'result'.", "expected": 2.0},
        {"prompt": "Compute 7 / 2.5 and store the result in 'result'.", "expected": 2.8},
        {"prompt": "Compute 0.25 * 4 and store the result in 'result'.", "expected": 1.0},
        {"prompt": "Compute 4.5 - 1.5 and store the result in 'result'.", "expected": 3.0},
        {"prompt": "Compute 9.99 + 0.01 and store the result in 'result'.", "expected": 10.0},
        {"prompt": "What is the type of 2.0? Store the result (type) in 'result'.", "expected": float}
    ]

    complex_questions = [
        {"prompt": "Assign the complex number 3+4j to variable 'result'.", "expected": 3+4j},
        {"prompt": "Add (1+2j) and (3+4j) and store the result in 'result'.", "expected": 4+6j},
        {"prompt": "Subtract (5+6j) minus (2+3j) and store the result in 'result'.", "expected": 3+3j},
        {"prompt": "Multiply (1+2j) by (3+4j) and store the result in 'result'.", "expected": -5+10j},
        {"prompt": "Divide (3+2j) by (1+0j) and store the result in 'result'.", "expected": 3+2j},
        {"prompt": "Assign 2+0j to variable 'result'.", "expected": 2+0j},
        {"prompt": "Create a complex number using complex(5, 6) and store it in 'result'.", "expected": 5+6j},
        {"prompt": "Get the real part of (5+6j) and store it in 'result'.", "expected": 5},
        {"prompt": "Get the imaginary part of (7+8j) and store it in 'result'.", "expected": 8},
        {"prompt": "Check if (3+4j) is an instance of complex and store the result in 'result'.", "expected": True},
        {"prompt": "Convert the integer 3 to a complex and store it in 'result'.", "expected": 3+0j},
        {"prompt": "Convert the float 3.5 to a complex and store it in 'result'.", "expected": 3.5+0j},
        {"prompt": "Multiply (2+3j) by (2-3j) and store the result in 'result'.", "expected": 13+0j},
        {"prompt": "Compute the absolute value of 3+4j (abs(3+4j)) and store it in 'result'.", "expected": 5.0},
        {"prompt": "What is the type of (1+2j)? Store the result (type) in 'result'.", "expected": complex},
        {"prompt": "Add 1 and 2j and store the result in 'result'.", "expected": 1+2j},
        {"prompt": "Multiply complex(0, 1) by complex(0, 1) and store the result in 'result'.", "expected": -1+0j},
        {"prompt": "Divide (4+2j) by 2 and store the result in 'result'.", "expected": 2+1j},
        {"prompt": "Check if (5+0j) is an instance of complex and store the result in 'result'.", "expected": True},
        {"prompt": "Compute (1+2j) ** 2 and store the result in 'result'.", "expected": -3+4j},
        {"prompt": "Get the real part of (2+3j)*(4+5j) and store it in 'result'.", "expected": -7},
        {"prompt": "Compute (2+3j) * (4-5j) and store the result in 'result'.", "expected": 23+2j},
        {"prompt": "Get the imaginary part of (2+3j)*(4+5j) and store it in 'result'.", "expected": 22},
        {"prompt": "Use complex('2+3j') to create a complex number and store it in 'result'.", "expected": 2+3j},
        {"prompt": "Check if the type of (3+4j) is complex and store the result in 'result'.", "expected": True}
    ]

    boolean_questions = [
        {"prompt": "Assign True to variable 'result'.", "expected": True},
        {"prompt": "Assign False to variable 'result'.", "expected": False},
        {"prompt": "Compute 'not True' and store the result in 'result'.", "expected": False},
        {"prompt": "Compute 'not False' and store the result in 'result'.", "expected": True},
        {"prompt": "Compute 'True and False' and store the result in 'result'.", "expected": False},
        {"prompt": "Compute 'True or False' and store the result in 'result'.", "expected": True},
        {"prompt": "Check if 3 > 2 and store the result in 'result'.", "expected": True},
        {"prompt": "Check if 3 < 2 and store the result in 'result'.", "expected": False},
        {"prompt": "Check if 3 == 3 and store the result in 'result'.", "expected": True},
        {"prompt": "Check if 3 != 4 and store the result in 'result'.", "expected": True},
        {"prompt": "Check if 5 >= 5 and store the result in 'result'.", "expected": True},
        {"prompt": "Check if 5 <= 4 and store the result in 'result'.", "expected": False},
        {"prompt": "Check if True is an instance of bool and store the result in 'result'.", "expected": True},
        {"prompt": "Check if False is an instance of bool and store the result in 'result'.", "expected": True},
        {"prompt": "Check if 1 is an instance of bool and store the result in 'result'.", "expected": False},
        {"prompt": "Compute (1 < 2) and (3 > 2) and store the result in 'result'.", "expected": True},
        {"prompt": "Compute (1 < 2) or (3 < 2) and store the result in 'result'.", "expected": True},
        {"prompt": "Compute not (1 == 1) and store the result in 'result'.", "expected": False},
        {"prompt": "Convert 0 to boolean (bool(0)) and store the result in 'result'.", "expected": False},
        {"prompt": "Convert 1 to boolean (bool(1)) and store the result in 'result'.", "expected": True},
        {"prompt": "Convert an empty list to boolean (bool([])) and store the result in 'result'.", "expected": False},
        {"prompt": "Convert a non-empty list [0] to boolean (bool([0])) and store the result in 'result'.", "expected": True},
        {"prompt": "Compute (5 > 3) and (2 < 1) and store the result in 'result'.", "expected": False},
        {"prompt": "Compute (5 > 3) or (2 < 1) and store the result in 'result'.", "expected": True},
        {"prompt": "Compute (not True) == False and store the result in 'result'.", "expected": True},
        {"prompt": "Convert an empty string to boolean (bool('')) and store the result in 'result'.", "expected": False}
    ]

    none_questions = [
        {"prompt": "Assign None to variable 'result'.", "expected": None},
        {"prompt": "Check if None is None and store the result in 'result'.", "expected": True},
        {"prompt": "Check if None == None and store the result in 'result'.", "expected": True},
        {"prompt": "Check if None is not None and store the result in 'result'.", "expected": False},
        {"prompt": "Check if None == 0 and store the result in 'result'.", "expected": False},
        {"prompt": "Convert None to boolean (bool(None)) and store the result in 'result'.", "expected": False},
        {"prompt": "Check if bool(None) is an instance of bool and store the result in 'result'.", "expected": True},
        {"prompt": "What is the type of None? Store the result (type) in 'result'.", "expected": type(None)},
        {"prompt": "Compute (None is None) and (None == None) and store the result in 'result'.", "expected": True},
        {"prompt": "Check if None == [] and store the result in 'result'.", "expected": False},
        {"prompt": "Check if None == False and store the result in 'result'.", "expected": False},
        {"prompt": "Check if None == '' (empty string) and store the result in 'result'.", "expected": False},
        {"prompt": "Check if None != None and store the result in 'result'.", "expected": False},
        {"prompt": "Check if (None is None) == True and store the result in 'result'.", "expected": True},
        {"prompt": "Check if 5 is None and store the result in 'result'.", "expected": False},
        {"prompt": "Check if 0 is None and store the result in 'result'.", "expected": False},
        {"prompt": "Check if '' is None and store the result in 'result'.", "expected": False},
        {"prompt": "Compute None or True and store the result in 'result'.", "expected": True},
        {"prompt": "Compute None and True and store the result in 'result'.", "expected": None},
        {"prompt": "Compute True and None and store the result in 'result'.", "expected": None},
        {"prompt": "Compute False or None and store the result in 'result'.", "expected": None},
        {"prompt": "Compute True or None and store the result in 'result'.", "expected": True},
        {"prompt": "Check if None is an instance of NoneType and store the result in 'result'.", "expected": True},
        {"prompt": "Compute not None and store the result in 'result'.", "expected": True},
        {"prompt": "Compute None or False and store the result in 'result'.", "expected": False}
    ]

    topics = {
        '1': ('Integer', integer_questions),
        '2': ('Float', float_questions),
        '3': ('Complex', complex_questions),
        '4': ('Boolean', boolean_questions),
        '5': ('NoneType', none_questions)
    }

    while True:
        print("\nSelect a topic to practice:")
        print("1. Integer")
        print("2. Float")
        print("3. Complex")
        print("4. Boolean")
        print("5. NoneType")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        # Allow user to exit by typing 'exit' instead of selecting 6
        if isinstance(choice, str) and choice.lower() == 'exit':
            print("Exiting. Goodbye!")
            break
        if choice == '6':
            print("Exiting. Goodbye!")
            break
        if choice in topics:
            topic_name, questions = topics[choice]
            run_quiz(questions, topic_name)
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    print("Welcome to the Python Data Types Practice Quiz!")
    main()

