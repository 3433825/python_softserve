﻿def calc(input):
    return eval(input)


print(calc('5+2'))
print(calc(' ( 5 + 2 ) * 2'))
print(calc(' 5 + 2 * 2'))

# второй вариант

code1 = compile("5 + 2", "<string>", "eval")
code2 = compile("( 5 + 2 ) * 2", "<string>", "eval")
code3 = compile("5 + 2 * 2", "<string>", "eval")

print(eval(code1))
