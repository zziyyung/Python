#6.8 평균점수 구하기
#a,b,c,d=map(int,input().split())
#print((a+b+c+d)//4)

#7.5 날짜와 시간 출력하기 *
# year,month,day,hour,minute,second=input().split()
# print(year,month,day,sep="-",end='T')
# print(hour,minute,second,sep=":")

#8.5 합격 여부 출력하기
#a,b,c,d=map(int,input().split())
#if a>=90 and b>80 and c>85 and d>=80:
#    print("True")
#else:
#    print(False)

#9.4 여러 줄로 된 문자열 출력
s='''\'Python\' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.'''
print(s)

#10.5 range로 튜플 만들기 *
#n=int(input())
#a=[]
#for i in range(-10,10,n):
#    a.append(i)
#    b=tuple(a)
#print(b)

## range()를 꼭 for과 함께 써야한다는 생각은 넣어둬!

n=int(input())
b=tuple(range(-10,10,n))
# 튜플의 사용
print(b)