"""
建立一个员工数据的单向链表，允许在链表头部、链表中间、链表末尾添加数据
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
    while ptr is not None:
        if ptr.num == num:
            return ptr
        ptr = ptr.next
    return ptr


def insertnode(head, ptr, num, salary, name):
    newnode = Employee()
    if not newnode:
        return None
    newnode.num = num
    newnode.salary = salary
    newnode.name = name
    newnode.next = None
    if ptr is None:                    # 插入第一个节点
        newnode.next = head
        return newnode
    else:
        if ptr.next is None:          # 插入最后一个节点
            ptr.next = newnode
        else:                         # 插入中间节点
            newnode.next = ptr.next
            ptr.next = newnode
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

head = Employee()              # 建立链表的头部
head.next = None

if not head:
    print('Error!! 内存分配失败！！ \n')
    sys.exit(1)

head.num = data[0][0]
head.name = namedata[0]
head.salary = data[0][1]
head.next = None

ptr = head
for i in range(1, 12):
    node = Employee()
    node.next = None
    node.num = data[i][0]
    node.name = namedata[i]
    node.salary = data[i][1]
    node.next = None
    ptr.next = node
    ptr = ptr.next

# # 遍历链表
# cur = head.next
# while cur is not None:
#     print('姓名：%s\t编号：%d\t薪水：%d' % (cur.name, cur.num, cur.salary))
#     cur = cur.next

count = 0
while count != 1:
    print('请输入要插入其后的员工编号，如输入的编号不在此链表中，')
    position = int(input('新输入的员工节点将视为此链表的链表头部，要结束插入过程，请输入-1：'))
    if position == -1:
        break
    else:
        ptr = findnode(head, position)
        new_num = int(input('请输入新插入的员工编号: '))
        new_salary = int(input('请输入新插入的员工薪水: '))
        new_name = input('请输入新插入的员工姓名： ')
        head = insertnode(head, ptr, new_num, new_salary, new_name)
        count = count+1
    print()

ptr = head
print('\t员工编号     姓名\t薪水')
print('\t========================')
while ptr is not None:
    print('\t[%2d]\t[%-7s]\t[%3d]' % (ptr.num, ptr.name, ptr.salary))
ptr = ptr.next
