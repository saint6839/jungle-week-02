import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

def func(a,b):
    if b==1:
        return a%c
    temp = func(a, b//2)  # 절반값 기록하기

    #짝수라면 x*x
    if b%2==0:
        return temp *temp % c
    #홀수라면 x*x*a
    else:
        return temp *temp * a % c
    
print(func(a,b))