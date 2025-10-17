words_file=open('CROSSWD.txt','r')

print(type(words_file))

# print([x for x in dir(words_file) if '_' != x[0]])
while True:
    print(words_file.readline())
    for line in words_file:
        print(line.strip)
       #word.append(line)
# print(words)
# data=[1,3,2,8,6,5,10]

# print((2*x for x in data if x % 2 == 0))





def more_than_20(file):
    words = []
    data = open(file,'r')
words = [x.strip()for x in data if len(x.strip) > 20
         return words

print(more_than_20("CROSSWRD,txt")