import re

txtfile = open('regex_sum_318087.txt')
result_list = list()
for line in txtfile:
    line = line.rstrip()
    str_res = re.findall('[0-9]+', line)
    if len(str_res) < 1:
        continue
    result_list.extend(str_res)
print sum(map(int, result_list))
