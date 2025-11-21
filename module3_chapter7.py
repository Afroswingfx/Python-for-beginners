fname = input("Enter file name: ")
fh = open(fname)
count=0
tot_x=0
for line in fh:
    if  not line.startswith("X-DSPAM-Confidence:"):
       continue
    # fname = input("Enter file name: ")
    # fh = open(fname)
    # lv=0
    # count=0
    # tot_x=0
    # for line in fh:
    #     if  not line.startswith("X-DSPAM-Confidence:"):
    #        continue
    #     print((line).rstrip())
    #
    #     count=count+1
    #     ipos=line.find(":")
    #     print(ipos)
    #     value=line[ipos+2:]
    #     value_2=float(value)
    #     tot_x=tot_x+value_2
    #     average=tot_x/count
    #     print(count)
    #     print(tot_x)
    #     print(average)
    # print("Done")

    count=count+1
    ipos=line.find(":")
    # print(ipos)
    value=line[ipos+2:]
    value_2=float(value)
    tot_x=tot_x+value_2
    average=tot_x/count
    # print(count)
    # print(tot_x)
    # print(average)
print(f"Average spam confidence: {average}")

