import re

with open('in.txt', 'r') as f_in, open('out.txt', 'w') as f_out:
    items = list(map(int, re.findall(r'-?\d+', f_in.read())))
    f_out.write(str(sum(items) / len(items)))
