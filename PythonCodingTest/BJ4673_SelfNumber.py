n = input()
def Function_d(n):
    
    sum = 0
    for i in n:
        sum += int(i)
    sum = sum + int(n)
    return sum
print(Function_d(n))