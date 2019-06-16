#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-16 11:06
# @Author  : Mermaid  
# @File    : bahuanghou.py
num = 8#只需要判断皇后所在列数
result = [-1 for _ in range(num)]
enable0 = [True for _ in range(num)]
enable1 = [True for _ in range(2 * num - 1)]
enable2 = [True for _ in range(2 * num - 1)]
result = [-1 for _ in range(num)]
out_list = []


def queen(r):
    if (r == 8):
        #print(result)
        out_list.append(result.copy())
        return 0
    else:
        #结束为止为num
        for c in range(num):
            if (enable0[c] and enable1[r + c] and enable2[r - c + num - 1]):
                enable0[c] = False
                enable1[r + c] = False
                enable2[r - c + num - 1] = False
                result[r] = c
                queen(r + 1)
                result[r] = -1
                enable0[c] = True
                enable1[r + c] = True
                enable2[r - c + num - 1] = True
queen(0)
print('Number of all solution :', len(out_list))
one_solution = out_list[1]
for index in one_solution:
    temp = ['_' for _ in range(8)]
    temp[index] = '*'
    print(temp)
