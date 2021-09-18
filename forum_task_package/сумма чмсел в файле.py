def sum_ints_in_file(file_name):
    with open(file_name, 'r') as fp:
        return sum(map(int, fp.read().split()))


print(sum_ints_in_file('file.txt'))
if __name__ == '__main__':
    sum_ints_in_file(file_name='1.txt')
