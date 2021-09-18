#TODO: fix me
string_list = [input().split(",") for _ in range(int(input()))]
for _ in range(int(input())):
    string_number, word_number = [int(i) for i in input().split(",")]
    print(string_list[string_number][word_number])
