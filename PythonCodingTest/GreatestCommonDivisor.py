import sys 
#sys.stdin.readline()으로 두 수 입력받기
a, b = map(int,sys.stdin.readline().split())

#최대 공약수는 작은 수를 기준으로 하기 때문에 두 수 중 작은 수 설정
n = a if a <= b else b

#최대 공약수는 두 수가 가지는 공통 약수중 가장 큰 수. 따라서 n부터 오고 역순이기 때문에 -1 설정
for i in range(n,0,-1):
    if a % i == 0 and b % i ==0:
        print(i)
        break
