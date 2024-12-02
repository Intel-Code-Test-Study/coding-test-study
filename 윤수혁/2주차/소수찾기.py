# %%
"""
사용자로부터 두 정수를 입력 받고,
두 정수 사이에 존재하는 모든 소수를 찾고,
찾은 소수들을 모두 더한 수가 짝수이면, A로 출력하고, 홀수이면 B이어야 합니다.

만일 입력한 두 수에 소수가 존재하지 않으면 C를 출력해야 합니다.

또한, 입력한 두 수의 순서가 작은 수, 큰 수로 이어지지 않을 수 있습니다.

만약 입력한 두 수가 3자리 이하의 정수가 아니면, 다시 입력하라는 메시지를 출력하는 프로그램을 구현합니다.
"""

# %%
def is_prime(number):
    for i in range(2, number+1):
        if number+1 % i == 0:
            return False
    return True

first_number = int(input("첫번째 숫자를 입력하라"))
second_number = int(input("두번째 숫자를 입력하라"))
prime_list = []

# if (first_number or second_number >= 100) or (first_number or second_number <= 0): X
if first_number >= 100 or second_number >= 100 or first_number <= 0 or second_number <= 0:
    print("0<숫자<100로 다시 입력하라")
    # sys.exit() X

elif first_number == second_number:
    print("서로 다른 두 수를 입력하라")

elif first_number - second_number == 1 or second_number - first_number == 1:
    print("두 수 사이에 수가 없다")

else:
    if first_number > first_number:
        for i in range(second_number, first_number+1):
            if is_prime(i):
                prime_list.append(i)
    else:
        for i in range(first_number, second_number+1):
            if is_prime(i):
                prime_list.append(i)

    sum_prime = sum(prime_list)
    if sum_prime == 0:
        print("C")
    elif sum_prime % 2 == 0:
        print("A")
    else:
        print("B")