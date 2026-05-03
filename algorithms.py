def brute_force(text, pattern):
    n= len(text)
    m= len(pattern)

    comparisons = 0
    matches = []
    
    if m == 0:
        return matches,comparisons
    
    # Not need look at the all text
    for i in range(n-m+1):
        j=0

        # comparison letter by letter
        # if it is match look other letter and other letter etc..
        while j<m:
            comparisons +=1

            if text[i+j] != pattern[j]:
                break

            j +=1

        if j == m: # if all matches then add index to matches list
            matches.append(i)

        
    return matches,comparisons

def build_shift_table (pattern):
    
    # How much amount shift

    shift_table = {}
    m = len(pattern)

    # shift amount
    for i in range (m-1):
        shift_table[pattern[i]] = m-1-i

    return shift_table

def horspool(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    comparisons =0

    if m == 0:
        return matches, comparisons
    
    #create shift table for pattern
    shift_table = build_shift_table(pattern)

    i = m-1  # horspool right to left so we look at the last char

    while i<n:
        k = 0

        while k<m:
            comparisons +=1

            if text[i-k] != pattern [m-1-k]:
                break
        
            k +=1

        if k == m:
            matches.append(i-m+1)
        
        # For shifting look at the last character that caused mismatch
        last_char_in_text = text[i]

        # if it is in table get that value but it is not get value m (length of pattern)
        shift_amount = shift_table.get(last_char_in_text, m)

        i += shift_amount
    
    return matches,comparisons

# Boyer-Moore
def bad_table(pattern): # Like Horspool

    bad_symbol_table = {}
    m =len(pattern)

    # save index that been rightmost
    for i in range(m):
        bad_symbol_table[pattern[i]] =i

    return bad_symbol_table


# if it is match then look at the repeated part in text and jump
def good_suffix_table(pattern):

    m = len(pattern)
    good_suffix = [0] * (m+1)
    
    # For finding repeated series -- Which part repeat which index
    border_pos = [0] * (m+1)

    i = m
    j = m + 1
    border_pos[i] = j

# Finding repeated part and calculate jump value
    while i>0:
        #
        while j<=m and pattern[i-1] != pattern[j-1]: # if it is different so ok you can jump
            if good_suffix[j] == 0:
                good_suffix[j] = j-i   #jump j-i
            
            j = border_pos[j]
        i -=1
        j -=1
        border_pos[i] =j

    j = border_pos[0]

    # align the pattern head and match part 
    for i in range(m+1):
        if good_suffix[i] == 0:
            good_suffix[i] =j
        if i == j:
            j=border_pos[j]

    return good_suffix


def boyer_moore(text,pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0
    matches = []

    if m == 0:
        return matches,comparisons
    
    #Create table
    bad_symbol_table = bad_table(pattern)
    good_symbol_table = good_suffix_table(pattern)

    print(f"\n[{pattern}] - Bad Symbol Table : {bad_symbol_table}")
    print(f"\n[{pattern}] - Good Suffix Table : {good_symbol_table}")
    
    # pattern will be alignment according to start index s
    s = 0

    while s<= n-m:
        j = m-1 # right to left

        while j>=0:
            comparisons +=1
            if pattern[j] != text[s+j]:
                break
            j -=1
        
        if j<0 :
            matches.append(s)
            s += good_symbol_table[0]
        
        else:
            #bad_table calc
            bad_char = text[s+j]
            bad_char_pos = bad_symbol_table.get(bad_char, -1)

            bad_char_shift = max(1,j-bad_char_pos)

            #good table calc
            good_suffix_shift = good_symbol_table[j+1]

            #final jump
            s += max(bad_char_shift,good_suffix_shift)
    

    return matches,comparisons
