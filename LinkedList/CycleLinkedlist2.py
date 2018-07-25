"""
建立一个员工数据的环形链表
允许在链表头部和链表中间插入节点
"""
import sys


class Employee(object):
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ''
        self.next = None


def findnode(head, num):
    ptr = head
    while ptr.next != head:
        if ptr.num == num:
            return ptr
        ptr = ptr.next
    return ptr


def insertnode(head, after, num, name, salary):
    InsertNode = Employee()
    CurNode = None
    InsertNode.num = num
    InsertNode.name = name
    InsertNode.salary = salary
    InsertNode.next = None
    if InsertNode is None:
        print('内存分配失败!!!')
        sys.exit(0)
    else:
        if head is None:   # 判断链表是否为空
            head = InsertNode
            InsertNode.next = head
            return head
        else:
            if after.next == head:
                InsertNode.next = head
                CurNode = head
                while CurNode.next != head:
                    CurNode = CurNode.next
                CurNode.next = InsertNode
                head = InsertNode
                return head
            else:
                InsertNode.next = after.next
                after.next = InsertNode
                return head


position = 0
data = [[1001, 32367], [1002, 24388], [1003, 27556], [1007, 31299],
        [1012, 42660], [1014, 25676], [1018, 44145], [1043, 52182],
        [1031, 32769], [1037, 21100], [1041, 32196], [1046, 25776]]
namedata = ['Allen', 'Scott', 'Marry', 'John', 'Mark', 'Ricky',
            'Lisa', 'Jasica', 'Hanson', 'Amy', 'Bob', 'Jack']
print('员工编号 薪水   员工编号 薪水   员工编号 薪水   员工编号 薪水')
print('--------------------------------------------------------------')
for i in range(3):
    for j in range(4):
        print(' [%4d] $%5d ' % (data[j*3+i][0], data[j*3+i][1]), end='')
    print()
print('-------------------------------------------------------------')

head = Employee()
if not head:
    print('Error!!! 内存分配失败！！！')
    sys.exit(0)

head.num = data[0][0]
head.name = namedata[0]
head.salary = data[0][1]
head.next = None

ptr = head
for i in range(1, 12):
    newnode = Employee()
    newnode.num = data[i][0]
    newnode.name = namedata[i]
    newnode.salary = data[i][1]
    newnode.next = None
    ptr.next = newnode
    ptr = newnode

newnode.next = head


while True:
    print('请输入要插入其后的员工编号，如果输入的编号不在此链表中，')
    position = int(input('则新输入的员工节点将视为此链表的第一个节点，要结束循环过程，请输入-1： '))
    if position == -1:
        break
    else:
        ptr = findnode(head, position)
        new_num = int(input('请输入新插入的员工编号: '))
        new_salary = int(input('请输入新插入的员工薪水: '))
        new_name = input('请输入新插入的员工姓名: ')
        head = insertnode(head, ptr, new_num, new_name, new_salary)

ptr = head
print('\t员工编号     姓名\t     薪水')
print('\t===========================')
while True:
    print('\t[%2d]\t[%-6s]\t[%3d]' % (ptr.num, ptr.name, ptr.salary))
    ptr = ptr.next
    if head == ptr or head == head.next:
        break
print('\t--------------------------')
