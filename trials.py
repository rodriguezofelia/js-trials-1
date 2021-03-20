"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

# print(output_all_items([1, 'hello', True]))


def get_all_evens(nums):
    even_nums =[]

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)

    return even_nums

# print(get_all_evens([7, 8, 10, 1, 2, 2]))

def get_odd_indices(items):
    
    result = []

    for i in range(len(items)):
        if i % 2 == 0:
            result.append(items[i])

    return result

print(get_odd_indices([1, 'hello', True, 500]))

def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f'{i}. {item}')

        i += 1
# print_as_numbered_list(([1, 'hello', True]))

def get_range(start, stop):
    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums

# print(get_range(0, 5))

def censor_vowels(word):
    chars = []
    
    for letter in word:
        if letter in word:
            if letter in 'aeiou':
                chars.append('*')

        chars.append(letter)
    return ''.join(chars)

print(censor_vowels('hello world'))

def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camel_case)
    
def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

def truncate(string):
    result = []

    for char in string: 
        if result.length == 0 or char != result[-1]:
            result.append(char)
    
    return ''.join(result)


def has_balanced_parens(string):
    parens = 0
    for char in string:
        if char == '(':
            parens += 1
        elif char == ')':
            parens -= 1

            if parens < 0:
                return False

    return parens < 0

def compress(string):
    compressed = []
    curr_char = ''
    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if char_count > 1:
                compressed.append(str(char_count))
            
            curr_char = char
            char_count = 0
        
        char_count += 1
    
    compress.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))
    
    return compressed.join('')
