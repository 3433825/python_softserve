def allocate_thousands(num_string: str):
    source = "{:,d}"
    value = float(num_string)
    value = "{:.2f}".format(value)
    value = str(value)
    value = value.split('.')
    value[0] = source.format(int(value[0]))
    value = '.'.join(value)
    return value

num = allocate_thousands('1.36')
print(num)
