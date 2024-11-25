"""
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

이렇게 만들어라
"""

# %%
# # 잘못된 코드
# output_list = []

# def rsad(filter_list):
#     for i in range(len(filter_list)):
#         if type(i) == 'int':
#             output_list.append(i)

# filter_list = list(input())
# print(output_list)

# %%
# test_list = [1, 'a', 2, 'b']

# # 방법 1: range(len())을 사용할 경우
# for i in range(len(test_list)):  # i는 0,1,2,3
#     print(f"i = {i}")

# print("---")

# # 방법 2: 리스트를 직접 순회할 경우
# for i in test_list:  # i는 1,'a',2,'b'
#     print(f"i = {i}")

# %%
def filtering(filtered_list):
    output_list = []
    for i in filtered_list:
        try:
            num = int(i)
            if num not in output_list:  # 중복 체크
                output_list.append(num)
        except ValueError:
            continue
    return output_list

filtered_list = list(input())  # "12ab" -> ['1', '2', 'a', 'b']
result = filtering(filtered_list)  # -> [1, 2]
print(result)