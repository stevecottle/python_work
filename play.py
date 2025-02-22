#Random string generator

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

password = generate_password()
print(password)


# SC play / codewars practice:

numbers = []

for number in range(1,20):
    number_plus_one = number + 1
    numbers.append(number_plus_one)
print(numbers)

digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)
print(digits)

"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3
"""

def high_and_low_numbers(numbers):
    split_numbers = numbers.split()
    integer_number = []

    for number in split_numbers:
        integer_number.append(int(number))

    highest = max(integer_number)
    lowest = min(integer_number)

    return f"{highest} {lowest}"


print(high_and_low_numbers("1 2 3 4 5"))
print(high_and_low_numbers("1 2 -3 4 5"))



"""
Given an array of integers your solution should find the smallest integer.

For example:

Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
"""

def find_smallest_int(arr):

    smallest = min(arr)

    return smallest



print(find_smallest_int([78, 56, 232, 12, 11, 43]))
print(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
print(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)


"""
Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".

A few examples:(Input1, Input2, Input3 --> Output)

5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5
"""

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    else:
        return None

"""
Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.

"""
def get_count(sentence):

    vowels = "aeiou"
    counter = 0

    for character in sentence:
        if character in vowels:
            counter += 1 
    return counter

print(get_count("abracadabra"))


"""
Create a method to see whether the string is ALL CAPS.

Examples (input -> output)
"c" -> False
"C" -> True
"hello I AM DONALD" -> False
"HELLO I AM DONALD" -> True
"ACSKLDFJSgSKLDFJSKLDFJ" -> False
"ACSKLDFJSGSKLDFJSKLDFJ" -> True
"""

def function_name(sentence):

    for letter in sentence:
        if letter != letter.upper():
            return False
    return True

print(function_name("ACSKLDFJSgSKLDFJSKLDFJ"))



"""
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""

def disemvowel(string_):
    vowels = "aeiou"

    for letters in string_:
        if letters == vowels:
            del vowels
    return letters

print(disemvowel("bananau"))

""" ^^This isn't storing the letters anywhere"""

"""
Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
"""

def disemvowel(string_):
    vowels = "aeiou"
    no_vowels = ""

    for letter in string_:
        if letter not in vowels:
            no_vowels += letter
    return no_vowels

print(disemvowel("bananau"))


"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.
"""

# ^^ Parking this one


"""
Description:
In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""
def filter_list(l):
    new_list = []

    for item in l:
        if type(item) == int:
            new_list.append(item)

    return new_list


print(filter_list([1, 2, 'a', 'b', 'c']))



"""
Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples (input --> output):
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""
"""

"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""
#vvvvvvvvvvvvvvvvvvvvv Workings:

# Make integer into list of digits
def decending_order(num):
    digits = []
    
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits

print(decending_order(6133932482))


# Sort into an order
digits = [2, 8, 4, 2, 3, 9, 3, 3, 1, 6]
digits.sort()

print(digits)

# reverse the order
digits = [1, 2, 2, 3, 3, 3, 4, 6, 8, 9]
digits.sort(reverse = True)

print(digits)

# Make the individual integers one number
digits = [9, 8, 6, 4, 3, 3, 3, 2, 2, 1]

bucket = 0
for digit in digits:
    bucket = bucket * 10 + digit
print(bucket)


# vvvvvvvvvvvvvvvvv Final

def descending_order(num):
# Make integer into list of digits:
    digits = [] # Create list to contain the digits
    
    while num > 0: # While the input number (num eg 12345) is greater than 0 ...
        digits.append(num % 10) # '%' will divide num by 10 and generate a remainder (eg 1234 r5). The remainder will be the last digit of the num (eg 5). Then we add (append) this to the list 'digits'.
        num //= 10 # We now need to get to 4, and therefore remove 5. 12345 / 10 = 1234.5 ... use // to remove the decimal: 12345 // 10 = 1234

# Sort into order and reverse order:
    digits.sort(reverse = True) # .sort() will sort the digits into lowest -> highest, (reverse = True) makes digits highest -> lowest

# Make the individual integers one number:
    bucket = 0 # This sores the number as we build it
    for digit in digits: # Loop through each digit in the digits list
        bucket = bucket * 10 + digit # This takes the bucket number, * it by 10, then add the first digit in the digit list (0 * 10 + 5 = 5, 5 * 10 + 4 = 54, 54 * 10 + 3 = 543 etc) to finally give 54321
    return bucket # Once the loop has finnished the final bucket of numbers is returned 


print(decending_order(123456789))


"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
"""
print("Square Every Digit:\n")

num = 567144
print(f"This is num: {num}")


digits = []

if num == 0:
    digits.append(0)

while num > 0:
    digits.append(num % 10)
    num //= 10

print(f"This is digits {digits}")

digits.reverse()

print(f"This is digits reversed {digits}")

bucket = ""

for digit in digits:
    squared = digit * digit
    bucket += str(squared)

print(f"This is bucket {bucket}")

final_number = int(bucket)

print(f"This is final_number {final_number}")

"""
Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. 
For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.

"Hi!"     ---> "Hi!"
"Hi!!!"   ---> "Hi!"
"!Hi"     ---> "Hi!"
"!Hi!"    ---> "Hi!"
"Hi! Hi!" ---> "Hi Hi!"
"Hi"      ---> "Hi!"
"""

st = "Hi!"
print(st)

st = st.replace("!", "")
print(st)

st = st + "!"
print(st)


"""
Usually when you buy something, you're asked whether your credit card number, 
phone number or answer to your most secret question is still correct. 
However, since someone could look over your shoulder, 
you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.
"""
print(f"\nMasked numbers:")

characters = "23456789234567890wert7"
print(f"Original characters: {characters}")
characters = characters[::-1]
print(f"String reversed: {characters}")
reversed_masked = characters[:4] + "#" * (len(characters)-4)
print(f"Reversed masked: {reversed_masked}")
reversed_masked = reversed_masked[::-1]
print(f"Reversed (again) masked: {reversed_masked}")


characters = "23456789234567890wert7"
characters = characters[::-1]
reversed_masked = characters[:4] + "#" * (len(characters)-4)
reversed_masked = reversed_masked[::-1]


"""
Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"
"""
str_ = 'john McClane'

split_str = str_.split()

print(split_str)

split_str.reverse()
print(split_str)

final_string = ' '.join(split_str)
print(final_string)

"""
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') // returns true
solution('abc', 'd') // returns false
"""
"""
v1:
def solution(text, ending):
    if text[-1] == ending[-1] and text[-2] == ending[-2]:
                return True
            else:
                return False

print(solution( "ails",    "fails" ))

#^^ This won't work becasue it's only comparing the last two from the string. It needs to take all letters from 'ending'


print(solution( "samurai", "ai" ))

"""

"""
v2:

text = "ails"
ending = "fails"
text_reversed = text[::-1]
ending_reversed = ending[::-1]

if len(ending_reversed) > len(text_reversed):
    print(false)
    if ending_reversed == text_reversed * (len(ending_reversed)):
        print (true)
    else:
        print(false)

"""


# Final working:

def solution(text, ending):
    return text.endswith(ending)

print(solution("ails", "fails"))


"""

You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"

"""
print(f"\nMiddle characters:")


def get_middle(s):

    middle_character = s[len(s)//2]
    left_middle_character = s[(len(s)//2)-1]
    right_middle_character = s[(len(s)//2)]

    if len(s) % 2 != 0:
        return middle_character
    else:
        return (f"{left_middle_character}{right_middle_character}")


print(get_middle("seqt"))



"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

"""
print(f"\nShortest word:")

def find_short(s):


    split_string = s.split()
    word_length_list = []


    for words in split_string:
        word_lengths = len(words)
        word_length_list.append(word_lengths)
    return min(word_length_list)



print(find_short("bitcoin take over the world maybe who knows perhaps"))


"""
def LongestWord(sen):
    split_sen = sen.split()
    word_lenth_list = []
    
    for words in split_sen:
      word_lenth = len(words)
      word_lenth_list.append(word_length)

    return word_lenth

print(LongestWord("fun&!! time"))
"""

print(f"\nReturn longest word:")


def LongestWord(sen):
    split_input = sen.split()
    alpha_only = re.sub(r'[^A-Za-z0-9 ]+', "", split_input)
    """filtered = filter(str.isalpha,split_input)
    final_filtered = "".join(filtered)"""

    return alpha_only



print(LongestWord("fun&!!"))









