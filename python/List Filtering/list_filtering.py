def filter_list(l):
    return [i for i in l if type(i) == int]
  
# Test Cases
print(filter_list([1,2,'a','b'])) # [1,2]
print(filter_list([1,'a','b',0,15])) # [1,0,15]
