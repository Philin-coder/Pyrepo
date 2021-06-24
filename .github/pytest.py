base = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX', 10:'X',}
str_from_file = '9'
if str_from_file.isdigit():
    digit = int(str_from_file)
    if 0 < digit < 11:
        print (base[digit])
    else:
        print('Число вне диапазона')
else:
    print('Это не число')