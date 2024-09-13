# Exercise 1
print(f'\nExercise 1\n')

a = ['a','b','c']
b = [1,2,3]

# Write a loop that creates the dic {'a': 1, 'b': 2, 'c': 3}

dict1 = {}
count = 0

while len(dict1) != len(a):         # The while loop will iterate until there are no more keys in a.
    dict1[a[count]] = b[count]      # Assig key a to value b
    count +=1                       # Increase counter after each iteration

print(dict1)

# Exercise 2
print(f'\nExercise 2\n')

# Write code that takes all pairs (x,y) of numbers between 2 and 20 such that x != y and prints out their greatest common divisor (GCD).

print('x', 'y', 'GCD', sep='\t')        # header

for x in range(2,21):                   # Use a nested loop to create the pairs
    print(f'=================')
          
    for y in range(2,21):
        
        if x == y:                      # if x and y are the same ignore the iteration
            continue
        else:
            a = max(x,y)                # else do the GCD function
            b = min(x,y)
            r = a % b
            
            while r != 0:
                a = b
                b = r
                r = a % b
            
            print(x, y, b, sep='\t')    # print the row with the values

# Exercise 3
print(f'\nExercise 3\n')

print('x', 'y', 'GCD', sep='\t')        # header

for x in range(2,21):                   # Use a nested loop to create the pairs
    print(f'=================')
    
    for y in range(x+1,21):             # make y start at x+1, since we don't want to repeat lines, we eliminate the row where x == y, and make x always be smaller than y
        
        a = max(x,y)                    # apply the GCD function
        b = min(x,y)
        r = a % b
        while r != 0:
            a = b
            b = r
            r = a % b
        
        print(x, y, b, sep='\t')    # print the row with the values

# Exercise 4
print(f'\nExercise 4\n')

# Create the dictionary vowels where each vowel has a value associated to it

vslist = list("AEIOUYaeiouy")
count = 0
vs = {}

for v in vslist:
    vs[v] = count
    count +=1

print(vs)

# Rewrite the vowels function, so that instead it replaces the vowels with the corresponding value

def vowels(s):
    out = ""

    for c in s:
        if c in vs.keys():
            out += str(vs[c])
        else:
            out += c
    return out

vowels("Hey Mr. Handers!")

# Exercise 5
print(f'\nExercise 5\n')

# Use the structure of the split function (used in previous exercise of chapter 3) to create a new function that:
# 1. Takes a string 
# 2. Associates each word with a number representing where the word appears the last time in the string. 
# 3. Use a dictionary!

def last_seen(s,sep = " "):
    """Function takes a string and associates each word with a number representing where the word appears the last time in the string."""
    out = {}
    term = ""
    count = 0 # to associate a number to the word

    # form the words and append them to the dictionary with the associated number
    for c in s:
        if c in sep and term != "": 
            # if the c is a sep and term is not empty, the term should be added to the dictionary and the count should be associated to it
            out[term] = count
            count += 1
            term = "" 
        else:
            # if the previous condition was not met, and if c is not a sep, than we start to create a new term by combining the c
            if c != sep : 
                term += c
    
    # add the final word unless it is empty 
    if term != "":
        out[term] = count
        count += 1
    
    return out

print(last_seen("hej du hej du hej du"))

# Exercise 6
print(f'\nExercise 6\n')

# change the last_seen() function so that it outputs dictionary with numbers as keys and words as values

def last_seen1(s,sep = " "):
    """Function takes a string and associates each word with a number representing where the word appears the last time in the string."""
    out = {}
    term = ""
    count = 0 # to associate a number to the word
    # form the words and append them to the dictionary with the associated number
    for c in s:
        if c in sep and term != "": 
            # if the c is a sep and term is not empty, the term should be added to the dictionary and the count should be associated to it
            out[count] = term
            count += 1
            term = "" 
        else:
            # if the previous condition was not met, and if c is not a sep, than we start to create a new term by combining the c
            if c != sep : 
                term += c
    # add the final word unless it is empty 
    if term != "":
        out[count] = term
        count += 1
    return out

print(last_seen1("hej du hej du hej du"))

# Exercise 7
print(f'\nExercise 7\n')

# change the last_seen() function so that it outputs dictionary with all the positions for each word

def last_seen2(s,sep = " "):
    """Function takes a string and associates each word with a number representing where the word appears the last time in the string."""
    out = {}
    term = ""
    count = 0 # to associate a number to the word
    
    # form the words and append them to the dictionary with the associated number
    for c in s:
        
        if c in sep and term != "": 
            # if the c is a sep and term is not empty, the term should be added to the dictionary and the count should be associated to it
            # if the term is already present in the dictionary just append the new value 
            
            if term not in out.keys():
                out[term] = str(count)
                count += 1
                term = ""
            else:
                out[term] += " " + str(count)
                count += 1
                term = ""
        
        else:
            # if the previous condition was not met, and if c is not a sep, than we start to create a new term by combining the c
            if c != sep: 
                term += c
    
    # add the final word unless it is empty 
    if term != "":
        if term not in out.keys():
            out[term] = str(count)
            count += 1
            term = ""
        else:
            out[term] += " " + str(count)
            count += 1
            term = ""
    
    return out

print(last_seen2("hej du hej du hej du"))

# apply the function to a text to determine position of words

with open('example.txt', 'r') as text:
    print(last_seen2(text.read()))

print(f'Finito')