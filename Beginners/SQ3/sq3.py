# -*- coding: utf-8 -*-
def get_total_sum(s):
    total = 0
    for i in range(s, 0, -1):
        total+=i
    return total


def main():
    input_number = int(input(""))
    get_sum = get_total_sum(input_number)
    print(get_sum)

if __name__ == '__main__':
    main()