i = input("문자열 입력")
new = ''
now = i[0]
count = 0

for j in i:
    if j==now:
        count+=1
    else:
        new += now+str(count)
        now = j
        count=1
        
new += now+str(count)
print(new)
