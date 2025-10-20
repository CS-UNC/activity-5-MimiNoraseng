def more_than_20(file):
    word = []
    data = open(file,'r')
    for word in data:
        if len(words.strip()) > 20:
            words.append(words.strip())
words = [x.strip()for x in data if len(x.strip()) > 20] 
return words
# print(more_than_20("CROSSWRD.txt"))

def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

def uses_only(word,letters):
    for x in word:
        if x not in letters:
            return False
return True

def all_uses_only(file,letters):