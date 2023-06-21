scores = [[96, 84, 80], [96, 86, 76], [76, 95, 83], [89, 96, 69], [83, 86, 79], [86, 90, 83]]

sum = 0
avg = 0
cnt = 1
for st in scores:
    sum = st[0] + st[1] + st[2]
    avg = sum/3.0
    print("%d번째 학생의 합계 : %d, 평균 %.2f"%(cnt, sum, avg))
    cnt+=1
