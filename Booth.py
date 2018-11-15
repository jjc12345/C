#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 19:56
# @Author  : JasonWan
# @Site    : 
# @File    : Booth.py
# @Software: PyCharm
def format(st):    #格式化数据，去掉第一个零，方便后面的表示
    s = st.copy()
    i = 0
    if(s[i] is '-'):
        i = 1
    while(s[i] is '0'):
        s.remove('0')
    return s

def getcomple(st,f = 0):    #获取补码的操作
    s = st.copy()
    flag = s[0]
    s.reverse()
    i = s.index('1') + 1
    if(flag is '-'):
        for t in s[i:]:
            if(t is '1'):
                s[i] = '0'
            elif(t is '0'):
                s[i] = '1'
            else:
                s[i] = t
            i+=1
        s.reverse()
        s.remove('-')
        s.insert(0,'1')
        if(f != 0):
            s.insert(0,'1')
    else:
        s.reverse()
        s.insert(0, '0')
        if(f !=0):
            s.insert(0,'0')
    return s

def get_x(xt):     #获取-X的补码，用于后面的加法计算
    x = xt.copy()
    if(x[0] is '-'):
        x.remove('-')
        return getcomple(x, 1)
    else:
        x.insert(0, '-')
        return getcomple(x, 1)

def add(A, B):    #定义二进制相加的函数
    A = A.copy()
    B = B.copy()
    d = 0
    i =len(B) - 1
    while(i>=0):
        if(A[i] is '0' and B[i] is '0'):
            if(d == 0):
                A[i] = '0'
                d = 0
            else:
                A[i] = '1'
                d = 0
        elif(A[i] is '1' and B[i] is '1'):
            if(d == 0):
                A[i] = '0'
                d = 1
            else:
                A[i] = '1'
                d = 1
        else:
            if(d == 0):
                A[i] = '1'
                d = 0
            else:
                A[i] = '0'
                d = 1
        i -= 1
    return A


def caculate(X, _X, Y):
    B = X.copy()
    _B = _X.copy()
    C = Y.copy()
    if('.' in X):
        B.remove('.')
        _B.remove('.')
    if('.' in Y):
        C.remove('.')
    C.append('0')
    A = ['0' for i in B]

    Cn = []       #存储进行加减还是移位的操作
    re = []       #存储最后的计算的结果

    i = len(C) - 2

    while(i>=0):
        if(C[i] is '1' and C[i+1] is '0'):
            Cn.append('-')
        elif(C[i] is '0' and C[i+1] is '1'):
            Cn.append('+')
        else:
            Cn.append('0')
        i -= 1

    l = len(Cn) - 1
    i = 0

    for t in Cn:
        if(t is '+'):
            A = add(A,B)
        elif(t is '-'):
            A = add(A,_B)
        if(l != i):
            re.insert(0,A.pop())
            if(A[0] is '0'):
                A.insert(0,'0')
            else:
                A.insert(0,'1')
        i += 1
    A.extend(re)
    return A

def main():
    xt, yt = input("请输入两个操作数 中间以空格隔开").split()
    x = format(list(xt))
    y = format(list(yt))
    X = getcomple(x, 1)
    _X = get_x(x)
    Y = getcomple(y)
    print("X补码:",''.join(X),"_X补码:",''.join(_X),"Y的补码:",''.join(Y))
    re = []
    point = 0
    if('.' in X):
        point = X.index('.')
        re = caculate(X, _X, Y)
        re.insert(point,'.')
    else:
        re = caculate(X, _X, Y)
    print("结果为:",''.join(re[1:]))



if __name__ == "__main__":
    main()