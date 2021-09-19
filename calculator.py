def calc(input):
    return eval(input)
inputs = ['5 + 2', '( 5 + 2 ) * 2', '5 + 2 * 2']
for input in inputs:
    print(f'{input} = {calc(input)}')
