# -*- coding: utf-8 -*-
# Write Python code from here
# -*- coding: utf-8 -*-
# Remove specific special characters without using regex

def remove_special_characters(s):
    # Define the characters you want to remove
    special_chars = ".,!@#$%^&,*()"
    cleaned = ""
    for char in s:
        if char not in special_chars:
            cleaned += char
    return cleaned


def remove_special_characters(s):
    special_chars_list= ".,!@#$%^&,*/()"
    cleaned=""
    for one_by_one in s:
        if one_by_one not in special_chars_list:
            cleaned += one_by_one
    return cleaned

def main():
    input_str = input("")
    result = remove_special_characters(input_str)
    print(result)

if __name__ == "__main__":
    main()
