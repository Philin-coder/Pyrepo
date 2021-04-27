st = '''\
fish-krasnoborodko - Cat
fish-krasnoborodko - Cat
the hare - Fox
chicken in sauce - Fox
fish-krasnoborodko - Cat
young cockerel - Fox
red-chinned fish - Fox
tripe in Parmesan sauce - Cat
three crusts of bread - Pinocchio
half a nut - Pinocchio'''
d = {}
for line in st.splitlines():
    food, eater = line.split(' - ')
    d.setdefault(eater, set()).add(food)
for k, v in d.items():
    print(f'{k}:', ', '.join(v))
