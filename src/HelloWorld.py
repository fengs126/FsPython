'''
Created on 2019/05/20

@author: Administrator
'''
from src import People as pe
from urllib.request import urlopen
import pygame
import random
import re
import pyttsx3


def main():
    print("你好，世界4");
    f = "1"

    for i in range(2):
        f = foo(i);
        print(f);

    tup1 = ("a",)
    print(tup1);

    str1 = "a" + str(f) + "b"
    print(str1);

    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
        print(repr(x * x * x).rjust(4))

    divide(2, 1)
    divide(2, 0)

    p = pe.people('W3Cschool', 10, 30)
    print(p.speak());
    print(p + p);
    p.age = 50
    print(p.age);

    for line in urlopen('https://www.cnblogs.com/dy2903/p/7750335.html'):
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'pip' in line:  # look for Eastern Time
            print(line)

    a1 = 10
    print("a1 ==" + str(a1));
    if a1 == 10:
        a1 = 20
    print("a1 ==" + str(a1));

    print(pygame.font.get_fonts())
    print(0 % 100)

    print(random.choice([0, 1, 2, 4, 5, 6]))

    b1 = '何時間,なんじかん,3,名,几个钟头，几小时'
    print(b1.split(','))
    print(re.split(',| |\t', b1))

#     rate = [10, 30, 60]
#     for i in range(100):
#         print(random_index(rate))
    print(random.randint(1, 5))

    fdicts = dict()
    fdicts.update({'a':1})
    print(fdicts.get('b', 'NA'))
    print('へ' == 'ヘ')

    print(len(re.split(',', 'ab,c')))
    print('  abc   '.strip('\n'))

#     r1 = []
#     for i in range(100):
#         rdmidx = random.randint(0, 1000)
#         if rdmidx in r1:
#             print(str(rdmidx) + '+++++++')
#         else:
#             print(str(rdmidx))
#         r1.append(rdmidx)

    l1 = ['a', 'b', 'c', 'd', 'e']
    l2 = l1.copy()
    l2.sort()
    print(l2)
    s1 = set(l2)
    print(s1)
    l2.clear()
    l2 = l1.copy()
    s2 = set(l2)
    print(s2)

    s3 = set()
    s3.add('a')
    s3.add('b')
    s3.add('c')
    s3.add('d')
    print(s3)
    s3.add('e')
    print(s3)

    print('a' in s1)

    if not ''.strip():
        print('a')
    else:
        print('b')

    print(s1)
    s1.add('や')
    print(s1)
    s1.add('看')
    print(s1)

    l3 = []
    if not 'a' in l3:
        l3.append('a')
    if not 'a' in l3:
        l3.append('a')
    if not 'a' in l3:
        l3.append('a')
    print(l3)

    file1()

    l4 = ['a', 'b', 'c']
    l5 = ['e', 'f', 'g']
    l6 = []
    l6.append(l4)
    l6.append(l5)
    print(l6)
    l7 = []
    l7.extend(l6[0])
    print(l7)
    l6.remove(l7)
    print(l6)

    l8 = [['要る', 'いる', '0', '自五', '要，需要'], ['例', 'れい', '1', '名', '例子'], ['所為', 'せい', '1', '名', '原因'], ['点', 'てん', '0', '名', '点，分数，观点'], ['脱ぐ', 'ぬぐ', '1', '他五', '脱']]
    print(l8)
    l9 = [['敷地', 'しきち', '0', '名', '占地，用地'], ['憩い', 'いこい', '2', '名', '休息']]
    for bline in l9:
        l8.append(bline)
    print(l8)
    l8.remove(l8[3])
    print(l8)

#     ms1()

    l10 = ['a', 'b', 'c']
    l11 = []
    l11.append(l10)
    print(l10)
    print(l11)
    l10.clear()
    l10.extend(l5)
    print(l10)
    print(l11)


def foo(p1):
    res = p1 + 1;
    return res;


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


def random_index(rate):
    start = 0
    index = 0
    randnum = random.randint(1, sum(rate))
    for index, scope in enumerate(rate):
        start += scope
        if randnum <= start:
            break

    return index


def file1():
    filename = 'C:\\Users\\Administrator\\Desktop\\単語2.txt'
    flines = []
    fline1 = []
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count9 = 0
    if filename.strip():

        ffile = open(filename.strip(), 'r', encoding='UTF-8')
        for l in ffile.readlines():
            lformat = l.strip('\n').strip()

            if lformat and not lformat in flines:
                flines.append(lformat)

                rline = re.split(',|\t', lformat)
                tvalue = ''
                if len(rline) > 1:
                    tvalue = rline[1].strip()
                else:
                    tvalue = rline[0].strip()

                if len(tvalue) == 1:
                    count1 += 1
                if len(tvalue) == 2:
                    count2 += 1
                if len(tvalue) == 3:
                    count3 += 1
                if len(tvalue) == 4:
                    count4 += 1
                if len(tvalue) == 5:
                    count5 += 1
                if len(tvalue) > 5:
                    count9 += 1

                if tvalue in fline1:
                    print(tvalue)
                else:
                    fline1.append(tvalue)

        print(len(flines))
        print(count1)
        print(count2)
        print(count3)
        print(count4)
        print(count5)
        print(count9)
        ffile.close()


def ms1():
    print('pyttsx3 start')
    engine = pyttsx3.init()
    engine.say('甲斐')
    engine.runAndWait()
    print('pyttsx3 end')

    pass


main();
