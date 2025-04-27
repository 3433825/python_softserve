def calc(expression: str) -> float:
    # Видаляємо пробіли з виразу
    expression = expression.replace(" ", "")

    # Перетворюємо інфіксний вираз у постфіксний (RPN)
    def infix_to_postfix(expr: str) -> list:
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}  # Пріоритет операторів
        stack = []  # Стек для операторів і дужок
        output = []  # Список для постфіксного виразу

        i = 0
        while i < len(expr):
            char = expr[i]

            # Якщо символ — число (може бути багатозначним)
            if char.isdigit() or (char == "-" and (i == 0 or expr[i - 1] in "(+-*/")):
                num = char
                j = i + 1
                while j < len(expr) and (expr[j].isdigit() or expr[j] == "."):
                    num += expr[j]
                    j += 1
                output.append(float(num))
                i = j - 1

            # Якщо символ — відкриваюча дужка
            elif char == "(":
                stack.append(char)

            # Якщо символ — закриваюча дужка
            elif char == ")":
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                stack.pop()  # Видаляємо "("

            # Якщо символ — оператор
            elif char in "+-*/":
                while (stack and stack[-1] != "(" and
                       precedence.get(stack[-1], 0) >= precedence[char]):
                    output.append(stack.pop())
                stack.append(char)

            i += 1

        # Додаємо залишки зі стека в результат
        while stack:
            output.append(stack.pop())

        return output

    # Обчислюємо постфіксний вираз
    def evaluate_postfix(postfix: list) -> float:
        stack = []

        for token in postfix:
            if isinstance(token, float):  # Якщо токен — число
                stack.append(token)
            else:  # Якщо токен — оператор
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    if b == 0:
                        raise ValueError("Ділення на нуль")
                    stack.append(a / b)

        return stack[0]

    # Виконуємо перетворення і обчислення
    postfix = infix_to_postfix(expression)
    result = evaluate_postfix(postfix)
    return result if result.is_integer() else result


# Тести
if __name__ == "__main__":
    print(calc("5 + 2"))  # 7
    print(calc("(5 + 2) * 2"))  # 14
    print(calc("5 + 2 * 2"))  # 9
    print(calc("3*(3 + 2)"))