def read_file_line_by_line(file_name: str):
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            print(line)


def read_whole_file(file_name: str):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(lines)


read_file_line_by_line('../Data/source.txt')

read_whole_file('../Data/source.txt')