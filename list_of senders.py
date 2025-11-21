fname = input("Enter file name: ")
fh = open(fname)
count=0
for lines in fh:
   if not lines.startswith("From:"):
       continue
   count+=1
   line_2=lines.split()
   print(line_2[1])
   final_count=(count)

print(f"There were", final_count,"lines in the file with From as the first word")