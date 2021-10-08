def add_item(itemName, itemCost):
    global count, b
    items.append(itemName + ' - ' + str(itemCost))
    count += itemCost
    b = True


def print_receipt():
    global count, numeration, items
    global b
    if b:
        if len(items) > 0:
            print('Чек {}. Всего предметов: {}'.format(numeration, len(items)))
        for element in items:
            print(element)
        print('Итого:', count)
        print('-----')
        count = 0
        numeration += 1
        items.clear()
    b = False
