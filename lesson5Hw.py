
#1.輸入學生分數
分數清單=[]
人數=int(input('請問班上有幾人?'))
for 學生 in range(人數):
    問句='請輸入學生'+str(學生+1)+'的分數:'
    分數=int(input(問句))
    分數清單.append(分數)

#2.計算總分、最大最小
sum=0
最高分=(分數清單[0])
最低分=(分數清單[0])
for 分數 in 分數清單:
    sum=sum+分數
    if 最低分>分數:
        最低分=分數
    if 最高分<分數:
        最高分=分數

#3.計算平均
平均=sum/人數

#4.輸出結果
print('總分:',sum)
print('平均:',平均)
print('最高分:',最高分)
print('最低分:',最低分)
    
    
    

    
