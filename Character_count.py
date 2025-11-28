from shlex import split

file=input("Enter name of file")
f_name=open(file)
lst=dict()
lines=split(f_name)
# print(lines)
for word in lines:
    if word in lst:
        lst[word]=lst[word]+1
    else:
        lst[word]=1
    # print(lst)
for word in sorted(lst,reverse=True):
    print(word,lst[word])