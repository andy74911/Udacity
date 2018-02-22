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

text_by_phones = set()
text_to_phones = set()

for text in texts:    
    text_by_phones.add(text[0])    
    text_to_phones.add(text[1])

call_by_phone = set()
call_to_phone = set()

for call in calls:
    call_by_phone.add(call[0])    
    call_to_phone.add(call[1])
    
telemarketer_set = set()
for call in call_by_phone:
    if (call not in text_by_phones and 
        call not in text_to_phones and
        call not in call_to_phone):
        telemarketer_set.add(call)

telemarketer_set = sorted(telemarketer_set)
print("These numbers could be telemarketers: ")
for phone in telemarketer_set:
    print(phone)

"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
