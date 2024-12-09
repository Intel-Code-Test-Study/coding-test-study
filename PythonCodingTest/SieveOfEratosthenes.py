#1부터 100만까지 소수 구하기
num = 1000000 

#1부터 100만까지 일단 모두 소수로 정의, 인덱스와 실제 숫자를 일치시켜야하기 때문에 n+1까지
prime = [True] * (num + 1)

 #0과 1은 소수가 아님
prime[0], prime[1] = False, False
for i in range(2,num+1): #2부터 100만까지 돌리기
    if prime[i]: #if prime[i]가 소수일때, 라는 의미
        
        #i*2부터 i의 배수를 순회, 최초의 i는 소수이다.
        for j in range(i*2,num+1,i):
            prime[j] = False #i의 배수는 소수가 아니므로 False

#몇 개 인지 세보자
result = 0
for i in range(num+1):
    if prime[i]:
        result += 1

print(result)
