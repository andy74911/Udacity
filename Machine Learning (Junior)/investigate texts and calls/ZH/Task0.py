"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

datetime_tmp = datetime.max
earliest_text = ''
for data in texts:
    dt = datetime.strptime(data[2], '%d-%m-%Y %H:%M:%S')
    if dt < datetime_tmp:
        datetime_tmp = dt
        earliest_text = data
print('First record of texts, {} texts {} at time {}'.format(
    earliest_text[0], earliest_text[1], earliest_text[2]))


datetime_tmp = datetime.min
latest_text = ''
for data in calls:
    dt = datetime.strptime(data[2], '%d-%m-%Y %H:%M:%S')
    if datetime_tmp < dt:
        datetime_tmp = dt
        latest_text = data
print(
    'Last record of calls, {} calls {} at time {}, lasting {} seconds'.format(
        latest_text[0],
        latest_text[1],
        latest_text[2],
        latest_text[3]))
