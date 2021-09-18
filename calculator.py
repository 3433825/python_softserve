def calc(input):
    return eval(input)
print(calc('5+2'))
print(calc(' ( 5 + 2 ) * 2'))
print(calc(' 5 + 2 * 2'))

# второй вариант

print(eval(compile("5 + 2", "<string>", "eval")))
print(eval(compile("( 5 + 2 ) * 2", "<string>", "eval")))
print(eval(compile("5 + 2 * 2", "<string>", "eval")))