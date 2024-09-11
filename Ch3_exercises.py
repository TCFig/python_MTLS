# Examples 
def removing_trailing_space(s):
    i = len(s)
    while i > 0 and s[i-1] == ' ':
        i -= 1
    return s[0:i]

print(removing_trailing_space("4"))

# Exercise 3
print(f'\nExercise 3\n')

def vowels(s):
    vs = "AEIOUYaeiouy"
    out = ""

    for c in s:
        if c in vs:
            out += c
    return out

print(vowels("Hey Handers!"))

# Exercise 4
print(f'\nExercise 4\n')

def consoants(s):
    vs = "AEIOUYaeiouy"
    out = ""

    for c in s:
        if c not in vs:
            out += c
    return out

print(consoants("Hey Handers!"))

def vowels_or_consonants(s, voc = 'v'):
    vs = "AEIOUYaeiouy"
    out = ""

    if voc != 'v' and voc != 'c':
        print("illegal argument to save")
        # Here we should raise error. More about error control later
        return

    else:
        for c in s:
            if voc == 'v' and c in vs:
                 out += c
            elif voc == 'c' and c not in vs:
                out +=c
        return out
        
print(vowels_or_consonants("Hey Handers"))
print(vowels_or_consonants("Hey Handers", voc='c'))

# Exercise 5
print(f'\nExercise 5\n')

def split(s,sep = " "):
    res = []
    term = ""
    for c in s:
        if c in sep: 
            # This function only works if the there is a space after the word (That's why we need the condition below)
               # need to had condition that states that if term != "", don't append it to the res
            res.append(term)
            term = ""
        else:
            if c != " " : 
                term += c
    
    #if term != "":   # Condition states that if the "term" has characters it should append to res
     #   res.append(term)
    
    return res

# New function

def split(s,sep = " "):
    res = []
    term = ""
    for c in s:
        if c in sep and term != "": 
            # if the c is a sep and term is not empty, the term should be appended to the res
            res.append(term)
            term = ""
        else:
            # if the previous condition was not met, and if c is not a sep, than we start to create a new term by combining the c
            if c != sep : 
                term += c
    
    return res

print(split("Hello   world     I am   your    creator     "))

# Exercise 6
print(f'\nExercise 6\n')

# Test the following code. Does it work as expected? Why not? How can you fix this?

list1 = [1,2,3]
list2 = list1
list2.reverse()
print(list1)

# It's not working as expected because we only reversed list2 not list. However list also appears reversed.
# This happens because lists are mutable. One way to solve the problem is by creating a copy of the original list.

list1 = [1,2,3]
list2 = list1.copy()
list2.reverse()
print(list1)
print(list2)

# Exercise 7 
print(f'\nExercise 7\n')

mylist = ["Ho", "ho", "ho!"]

while mylist:
    x = mylist.pop()
    print(x)

print(mylist)

# Rewrite the code so that the list mylist is not empty at the end

mylist = ["Ho", "ho", "ho!"]
mylist2 = mylist.copy()

while mylist2:
    x = mylist2.pop()
    print(x)

print(mylist)

# Without using copy

mylist = ["Ho", "ho", "ho!"]
rcounter = len(mylist)

while rcounter > 0:
    x = mylist[rcounter-1]
    print(x)
    rcounter -= 1

print(mylist)

# Exercise 8
print(f'\nExercise 8\n')

# Write continue, break and pass in the while loop to see what happens

n = 10
while n > 0:
    n -= 1
    if n == 7:
        continue
    print(n)

# if n == 7 it continues the while loop. (no changes in the outcome)

n = 10
while n > 0:
    n -= 1
    if n == 7:
        break
    print(n)

# stops the while loop when n == 7 therefore it only prints 8 and 9

n = 10
while n > 0:
    n -= 1
    if n == 7:
        pass
    print(n)

# pass does nothing, it's just used as placeholder when you start to outline the structure of your code but haven't filled in the details yet.    

# Exercise 9
print(f'\nExercise 9\n')

# Write a while loop that reads in numbers from the user and saves them in a list. 
# It should continue to read in until the user enters 0; then the program should end the loop and print out the list.

out = []
answer = True # Required to define answer and start the while loop (if you wrote 0 or False it would have stoped the loop write away)

print('Feed me all the numbers human *O*')
while answer != 0:
    answer = int(input(f'Feed number: '))
    # The input always has to be before the conditional statement. Otherwise the answer would be stuck in the condition and never go outside to be acessed by the while loop
    if answer == 0:
        print('By feeding the mosnter a 0 you made him sad and he ran away')
    else:
        out.append(answer)
        print(f'Give me another number *O*: ')

print(f"You were able to feed the monster {len(out)} numbers before he ran away, which were {out}")

# Exercise 10
print(f'\nExercise 10\n')

def naiveGCD(n1,n2):
    """Calculate the GCD by testing all the numbers between 1 and min(a,b)"""
    small = min(n1,n2)
    
    for i in range(small, 0, -1):
        if (n1 % i == 0) and (n2 % i == 0):
            return i
    
print(naiveGCD(12,15))

# Exercise 11
print(f'\nExercise 11\n')


def passcode():
    
    """Function reads 4 digits (1-9), inputed by the user and evaluates if it's the correct code to unlock a door"""
    
    # start to define the pin in blank so that while loop can start.
    pin = ""

    # While the pin is not the correct one the loop will keep on working
    while pin != "3107":

        # This first while function asks the user for 4 digits between 1 and 9 (if they are not it sends an error).
        # The fucntion starts to combine the digits into a new pin until the user inputed 4 numbers (when count is 4)           
        count = 0
        while count < 4:
            num = input(f'Input number for pin: ')
            if int(num) < 0 or int(num) > 10: 
                (print(f'\nError: Type a number between 1 and 9.\n'))
            else:
                pin += num
                count += 1

        # the 4 digit pin created in the step above is then evaluated to see if it's the correct pin. 
        # If True, the door unlocks.  
        if pin == "3107":
            print(f'Door Unlocked!')
    
        # If False it start a new while loop.
        else:
            print(f'Pin is incorrect! Try again.')
            pin = ""  # If the pin is incorrect it resets so the user can input 4 new digits




# function asks for input number from user (one at a time) and the number needs to be between 1-9 (if not, send error)
# While loop that counts until 4 inputs from the user
# put numbers together and test if its the correct code
# If it's the correct code print "Door unlocked!" and return True
# Else ask for the pin again.