''' Given an array of strings, return all groups of strings that are anagrams.'''
def Anagrams(words,n):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    '''
    
    #code here
    d={}
    for i in words:
        x=''.join(sorted(list(i)))
        if x in d:
            d[x].append(i)
        else:
            d[x]=[i]

    return sorted(d.values())
  
