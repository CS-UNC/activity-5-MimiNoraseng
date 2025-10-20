def more_than_20(file):
    word = []
    data = open(file,'r')
 #for word in data:
#   if len(word.strip()) > 20:
#       word = [x.strip()] for x in data if len(x.strip)
return words


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