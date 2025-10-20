def more_than_20(file):
   long_words = []
with open(file,'r') as f:
    for line in f:
        words = line.strip().split()
    for word in words:
        if len(word) > 20:
            long_words.append(word)
return long_words

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
    for char in word:
        if char not in letters:
            return False
return True