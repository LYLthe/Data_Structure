"""
建立5个学生成绩的单向链表
遍历每一个节点并打印学生成绩
"""


class Student(object):
    def __init__(self):
        self.num = 0
        self.name = ''
        self.score = 0
        self.next = None


print('-------------------')
print('请输入5项学生数据：')
head = Student()
head.next = None
ptr = head
for i in range(1, 2):
    new_node = Student()
    new_node.num = eval(input('请输入学生学号: '))
    new_node.name = input('请输入学生姓名: ')
    new_node.score = eval(input('请输入学生成绩: '))
    ptr.next = new_node
    ptr = ptr.next

ptr = head
print('学号\t姓名\t成绩\n==========================')
while ptr is not None:
    print('%3d\t%-s\t%3d' % (ptr.num, ptr.name, ptr.score))
    head = ptr
    ptr = ptr.next
