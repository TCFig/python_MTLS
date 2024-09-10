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
