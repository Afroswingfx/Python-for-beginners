from shlex import split
file=input("Name of the file\n")
f_name=open(file)
counts=dict()
words=split(f_name)
# print(words)
for word in words:
    counts[word]=counts.get(word,0)+1
    # print(counts)

bigword=None
bigcount=None
for word,count in counts.items():
    # print(word,count)
    if bigcount is None or bigcount<count:
        bigcount=count
        bigword=word
print(bigword,bigcount)
