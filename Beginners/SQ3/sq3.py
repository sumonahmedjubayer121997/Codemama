# -*- coding: utf-8 -*-
# def get_total_sum(s):
#     total = 0
#     for i in range(s, 0, -1):
#         total+=i
#     return total

# def get_total_sum(s):
#     number_value = int(s)
#     total = 0
#     for i in range(1,number_value+1):
#         total += i 
#     return total


def get_total_sum(s):
    get_num = int(s)
    total = 0
    while get_num>0:
        total += get_num
        get_num-=1 #also can do get_num-=1 also can do get_num = get_num-1
    return total

    

def main():
    try:
        input_number = input("")
        get_sum = get_total_sum(input_number)
        print(get_sum)
    except ValueError:
        print("Invalid input. Please enter an integer.")

    

if __name__ == '__main__':
    main()