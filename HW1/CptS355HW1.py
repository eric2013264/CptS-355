def makettable(s1,s2):
    d = {}
    for i in range (0,len(s1)):
        tmp = s1[i]
        d[s1[i]] = s2[i]
        i+=1
    return d
    pass

def trans(ttable,s):
    tmp=''
    for c in s:
        tmp += ttable.get(c,c) #ttable[c] if k in ttable
    return tmp
    pass

# function to test translation code
# return True if successful, False if any test fails
def testtrans():
    ttable = makettable('abc', 'xyz')
    revttable = makettable('xyz', 'abc')
    tests = "Now I know my abc's"
    answer = "Now I know my xyz's"
    if trans(ttable, tests) != answer: return False
    if trans(revttable, trans(ttable, tests)) != "Now I know mb abc's": return False
    if trans(ttable,'') != '': return False
    if trans(makettable('',''), "abc") != 'abc': return False
    return True

testtrans()

def histo(s):
    l = []
    tmp = []
    
    for x in range (1,len(s)):  # Iterates through the string
        for a in range (0,128): # Check for each character
            character = chr(a)  # Char the int incrementor
            if character in s:  # For each character in the string
                if s.count(chr(a)) == x: # If the occurance == 1,2,3...
                    tmp.append((chr(a), s.count(chr(a)))) # Append substring to tmp
                    tmp = sorted(tmp, key=lambda k: k[0], reverse=True) # Sort tmp with decending frequency     
    l = l + tmp                 # Concatenate tmp to list l after each unique occurance
    l = sorted(l, key=lambda k:k[1]) # Now all we have to do is reverse it by occurance
    return l
    pass

def testhisto():
    answer = [('t', 1), ('p', 1), ('n', 1), ('l', 1), ('i', 1), ('d', 1), ('m', 2), ('e', 3)]
    answer2 = [('j', 1), ('h', 1), ('e', 2), (' ', 2), ('o', 4), ('l', 4)]
    if histo("implemented") != answer: return False
    if histo("hello jello oo") != answer2: return False
    return True
    pass
testhisto()

def digraphs(s):
    x = 0
    l = []
    tmp = []
    duplicate = False

    for i in range(0,len(s)-1):      # Iterate string s
        subStr = s[i:i+2]            # Split into substrings
        for j in tmp:                # Check if substring is in the list
            if '/'+subStr+'/' in j: duplicate = True # If it is
        if duplicate == False:       # If it is a duplicate
            for k in range(0, len(s)-1):
                if subStr == s[k:k+2]: x+=1 # Check how many times it has occured
            tmp.append(('/'+subStr+'/', s.count(subStr))) # Append to tmp
            tmp = sorted(tmp, key=lambda k: k[0], reverse=False) # List of similar occurances sorted by reverse alphabetical order
        duplicate = False # Reset default bool value
    
    l = l + tmp  # Concatenate tmp to list l after each unique occurance
    l = sorted(l, key=lambda k:k[1], reverse=True) # Now all we have to do is reverse it by occurance
    return(l)
    pass

def testdigraphs():
    answer = [('/ho/', 3), ('/oh/', 3), ('/ah/', 2), ('/ha/', 2)]
    answer2 = [('/he/', 3), ('/el/', 2), ('/ll/', 2), ('/lo/', 2), ('/eh/', 1), ('/je/', 1), ('/oh/', 1), ('/oj/', 1)]
    if digraphs("hahahohohoh") != answer: return False
    if digraphs("hellojellohehe") != answer2: return False
    return True
    pass

testdigraphs()

