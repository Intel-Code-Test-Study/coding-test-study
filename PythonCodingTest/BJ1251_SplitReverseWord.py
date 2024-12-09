'''
K-Programming
1. 단어를 세 부분으로 쪼갠다
2. 세 부분을 각각 역순으로 배열한다
3. 합쳐서 새로운 단어를 만든다.
4. 만들어진 단어 중 사전 순으로 가장 앞서는 단어를 출력한다'''
word = input()
l = len(word)
newword = []
for i in range(0,l):
    for j in range(i+1,l+1):
        if len(word[:i]) >= 1 and len(word[i:j]) >= 1 and len(word[j:]) >= 1:
            first = word[:i]
            second = word[i:j]
            third = word[j:]
            first = first[::-1]
            second = second[::-1]
            third = third[::-1]
            newword.append(first+second+third)
print(*newword)
print(min(newword))