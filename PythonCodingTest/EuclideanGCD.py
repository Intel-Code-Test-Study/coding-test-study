import sys 
#sys.stdin.readline()으로 두 수 입력받기
a, b = map(int,sys.stdin.readline().split())

#유클리드 호제법을 적용하기 위해 큰 수와 작은 수 분리
A = max(a,b)
B = min(a,b)

#큰 수를 작은 수로 나눈 후, 나머지가 0이면 GCD, 나미지가 아닐 경우 작은 수를 큰 수에 적용, 나머지를 작은 수에 적용
'''while True:
    A,B = B,A%B
    if B == 0:
        print(A)
        break'''

#EuclideanGCD라는 함수로 정의    
def EuclideanGCD(A,B):
# B != 0(B == true)일 때 돌아간다. 
    while B:
    #나누고 나머지가 있을 때(B!=0일때) 큰 수에 B가 들어가고, 작은 수에 나머지가 들어간다.
        A, B = B, A%B
    # B ==0일때, 나눠떨어질 때의 수가 최대공약수니까 A를 return
    return A
print(EuclideanGCD(A,B))