"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Get the area code


def area_code(phone):
    chars = list(phone)
    end = 0
    for c in chars:
        if c == ')':
            break
        end += 1
    return phone[0:end + 1]


# Find the numbers call by people in Bangalore
call_by_bang_set = set()
for call in calls:
    if call[0][:5] == '(080)':
        codes = ''
        if call[1][:2] == '(0':
            codes = area_code(call[1])
        elif(call[1][int(len(call[1]) / 2)] == ' ' and
             (call[1][0] == '7' or call[1][0] == '8' or call[1][0] == '9')):
            codes = call[1][:4]
        if codes != '':
            call_by_bang_set.add(codes)
            
call_by_bang_set = sorted(call_by_bang_set)
print('The numbers called by people in Bangalore have codes:')
for call in call_by_bang_set:
    print(call)


# Calculat how many calls is local (from Bangalore and to Bangalore)
call_by_bang_cnt = 0
call_to_bang_cnt = 0
for call in calls:
    if call[0][:5] == '(080)':
        call_by_bang_cnt += 1
        if call[1][:5] == '(080)':
            call_to_bang_cnt += 1

print(
    '{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(
        call_to_bang_cnt * 100 / call_by_bang_cnt))
"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
