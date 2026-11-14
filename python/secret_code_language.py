st = input("Enter a message ")
coding = True 
if(coding):
    if(len(st)>=3):
        r1 = "haodjo"
        r2 = "baigij"
        st = r1 + st[1:15] + st[0] + r2
        print(st)

else:
    pass
