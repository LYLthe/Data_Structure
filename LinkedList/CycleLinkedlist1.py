"""
建立一个学生数据的环形链表
"""


class Student(object):
    def __init__(self):
        self.name = ''
        self.no = ''
        self.next = None


head = Student()
ptr = head
ptr.next = None
select = 0
while select != 2:
    select = int(input('(1)新增 (2)离开 =》'))
    if select == 2:
        break
    ptr.name = input('姓名: ')
    ptr.no = input('学号: ')
    new_data = Student()
    ptr.next = new_data
    new_data.next = None
    ptr = new_data
ptr.next = head
print()
ptr = head
while True:
    print('姓名：%s\t 学号：%s\n' % (ptr.name, ptr.no))
    ptr = ptr.next
    if ptr.next == head:
        break
print('---------------------------------------------')
