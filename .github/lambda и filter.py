def generate_list_with_numbers_from_string():
    return sorted(list(map(int, input().split())))
 
def generate_list_with_numbers_gt_5():
    return sorted(filter(lambda x: x > 5, list(map(int, input().split()))), reverse=True)
 
 
if __name__ == '__main__':
    assert generate_list_with_numbers_from_string() == [3, 5, 8, 10, 20]
    assert generate_list_with_numbers_gt_5() == [20, 10, 8]