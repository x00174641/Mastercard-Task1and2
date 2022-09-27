# Task 1 - Find the most frequent integer in an array

def most_frequent_integer(array): # create a function with 1 parameter called array
    index = 0
    counter = 0

    for i in range(len(array)): # for loop, looping 12 times as the length of the array has 12 integers
        cur_iteration = array.count(array[i]) # counts how many times the number shows up in the array -> array[0] = 1 counts how many times 1 shows up and sets it to the current iteration variable
        if cur_iteration > counter: # if the current iteration is greater than counter then do the following
            counter = cur_iteration # sets the new most common integer to counter
            index = i # sets the position of the most common integer to the variable index
    return array[index] # returns the most common integer

array = [1,2,3,4,5,5,5,6,7,8,8,8,8,9] # array to be taken to parameter 
print(most_frequent_integer(array)) # call the function with the parameter array

# Task 2 - Reverse a String iteratively and recursively 

def reverse_string_iteratively(string): # function with 1 parameter
    length_of_string = len(string) # length of string and stores it to length_of_string variable
    emp_string = '' # empty string variable
    index = length_of_string - 1 # index for while loop
    while index >= 0: # keep looping until the index is greater or equals to 0
        emp_string += string[index] #appends each letter to the empty string var
        index -= 1 # minus 1 from the index so it can move on to the next letter
    print(emp_string)     # print the reversed string
 
string = "reversethisstring" # string used in paramenter
reverse_string_iteratively(string) # call function with string param

def reverse_string_recursively(string): # function with 1 param
    if string == "": # if string is equal to empty string then return string
        return string
    else: #if not
        return reverse_string_recursively(string[1:]) + string[0] # function is called to slice parts of the string other than the 1st letter and then it adds that to the string

string = "gnirtssihtesrever"
print(reverse_string_recursively(string))
