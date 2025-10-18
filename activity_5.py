words_file=open('CROSSWD.txt','r')

print(type(words_file))
words = []
for line in words_file:
    print(line)
    words.append(line)

print(words)
print([x for x in dir(words_file)])if '_' != x[0])
data = [1,3,2,8,5,6,10]

print(2*x for x in data if x % 2 == 0)

def more_than_20(file):
    words = []
    data = open(file,'r')
    for word in data:
        if len(words.strip()) > 20:
            words.append(words.strip())
words = [x.strip()for x in data if len(x.strip()) > 20]
return words


print(more_than_20("CROSSWRD.txt"))