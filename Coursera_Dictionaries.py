file_name=input("Enter the name of the file")
f_name=open(file_name)
# words=split(f_name)
counts=dict()
for lines in f_name:
    if not lines.startswith ("From "):
        continue
    # print(lines)
    words=lines.split()
    sender=words[1]
    counts[sender]=counts.get(sender,0)+1

bigcount=None
bigword=None
for word,count in counts.items():
    if bigcount is None or count> bigcount:
        bigword=word
        bigcount=count
print(bigword,bigcount)