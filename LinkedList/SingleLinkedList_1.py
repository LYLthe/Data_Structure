"""
建立一个动态创建学生信息的单链表
"""


class Student(object):
    def __init__(self):
        self.name = ''
        self.math = 0
        self.english = 0
        self.no = ''
        self.next = None


head = Student()
head.next = None
ptr = head
Msum = Esum = num = student_no = 0
select = 0

while select != 2:
    print('(1)新增(2)离开=>')
    try:
        select = int(input('请输入一个选项：'))
    except ValueError:
        print('输入错误')
        print('请重新输入\n')
    if select == 1:
        new_data = Student()
        new_data.name = input('姓名：')
        new_data.no = input('学号：')
        new_data.math = eval(input('数学成绩：'))
        new_data.english = eval(input('英语成绩：'))
        ptr.next = new_data
        new_data.next = None
        ptr = ptr.next
        num = num+1


ptr = head.next
print()
while ptr is not None:
    print('姓名：%s\t学号：%s\t数学成绩：%d\t英语成绩：%d'%(ptr.name, ptr.no, ptr.math, ptr.english))
    ptr = ptr.next
