# 1. Write a Python script to sort (ascending and descending) a dictionary by value.

sample_dict={'a': 23, 'b': 45, 'c': 10, 'd': 5}

asc_sort=sorted(sample_dict.items(),key=lambda x:x[1])
desc_sort=sorted(sample_dict.items(),key=lambda x:x[1],reverse=True)

print(f"Ascending sorted dict {dict(asc_sort)}")
print(f"Descending sorted dict {dict(desc_sort)}")