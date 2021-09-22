def calc(example):
    return eval(example)
examples = ['5 + 2', '( 5 + 2 ) * 2', '5 + 2 * 2']
for example in examples:
    print(f'{example} = {calc(example)}')
# это нужно изменить