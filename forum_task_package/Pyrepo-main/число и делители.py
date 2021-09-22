# include <iostream>
# using namespace std;
# int number_of_divisors(int x){
#     int count = 0;
#     for (int i = 1; i <= x / 2; i++) // число 1 - тоже делитель
#         if (x%i == 0)
#             ++count;
#     return ++count; // увеличиваем количество делителей еще на один, т.к. число - делитель самого себя.
# }
# int main()
# {
#     int a,b;
#     cin >> a >> b;
#     for (int i = a; i <= b; i++)
#         cout << i <<" "<<number_of_divisors(i) << endl;
#     system("pause");
#     return 0;
# }
def numebr_of_devizions(x):
    count = 0
    for i in range(1, x / 2):
        if x % 2 == 0:
            count = count + 1
    print(count)
    return count
