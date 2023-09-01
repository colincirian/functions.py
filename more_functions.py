#question 1
def contains_string(main_str, sub_str):
    return sub_str in main_str

main_str = "Hello World"
sub_str1 = "Hello"
sub_str2 = "Bye"

result1 = contains_string( main_str, sub_str1)
result2 = contains_string( main_str, sub_str2)

print(result1)
print(result2)

#question 2



#question 3
def rev_str():
    my_string = "Hello, my name is Colin."
    my_string = my_string[:: -1]
    return my_string

new_string = rev_str()
print(new_string)

#question 4 
def cap_words():
    my_list = ["monkeys", "pandas", "bears", "lions"]
    new_list = [word.upper() for word in my_list]
    return new_list

result = cap_words()
print(result)


def words_rev():
    sentence = "Colin is the best in the world."
    new_sentence = sentence[:: -1]
    return new_sentence

result = words_rev()
print(result)


def words_rev():
    string = "Hello, I currently weigh 165lbs."
    string_reversed = string[:: -1]
    return string_reversed

new_string = words_rev()
print(new_string)

def capitalize():
    sentence1 = "Hello, my name is world."
    cap_sentence1 = sentence1.upper()
    return cap_sentence1

result = capitalize()
print(result)

def cap_str():
    my_string = "hello, what is your name?"
    cap_my_string = my_string.upper()
    return cap_my_string

result = cap_str()
print(result)

def greet(name, num):
    print("Hello world! My name is", name)
    print("How are you sir?")
    print("I am", num)

greet('Colin', 22) 

def sum(n1, n2):
    result = n1 + n2
    return(result)

number1 = 13829087341278931
number2 = 14971234891273122

result = sum(number1, number2)

print("The result is:", result)

marks = [23, 122, 4, 6564, 2454, 0, 5]
length = len(marks)
print(length)

def find_avg_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    avg_marks = sum_of_marks / total_subjects
    return avg_marks

marks = [1, 2, 3, 4, 5, 6, 7]
avg_marks = find_avg_marks(marks)
print('Your average marks is:', avg_marks)