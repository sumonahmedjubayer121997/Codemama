def remove_special_char(s):
    get_number = ""
    for char in s:
        if char.isdigit():
            get_number += char       
    return get_number

            


def main():
    input_str = input("")
    number = remove_special_char(input_str)
    if number:
        print(number)
    else:
        print("Number not found")

if __name__ == '__main__':
    main()
