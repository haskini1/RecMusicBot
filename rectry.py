"""
201 -> 202, 203
202 -> 203, 201
203 -> 201, 202
not -> 201, 202 (not = 203)
"""

# функция чтобы понять какую группу исполнителей дать на оценку
# (211 получит 212 и 213, 212 получит 213 и 211, 213 получит 211 и 212)
import pandas as pd

def group_to_estimate(group):
    return (group - 210) % 3 + 211

def newlenght(*args):
    l = 0
    for u in args:
        l = l + u**2
    return l**0.5

# скаляр векторов
def scalar(a1, b1, c1, d1, a2, b2, c2, d2):
    return a1 * a2 + b1 * b2 + c1 * c2 + d1 * d2

# длина вектора
def lenghtvector(x, y, z, u):
    return (x ** 2 + y ** 2 + z ** 2 + u ** 2) ** 0.5


# косинусное расстояние
def cosinus(a1, b1, c1, d1, a2, b2, c2, d2):
    return scalar(a1, b1, c1, d1, a2, b2, c2, d2) / ((lenghtvector(a1, b1, c1, d1)) * lenghtvector(a2, b2, c2, d2))


students = [25, 25, 24] # количество студентов в каждой группе

RS = pd.read_excel('D:/verygoodfile.xlsx')


# создадим двумерные массивы из нулей размером (students[index_group]+2) x (11)
table211 = [[0]*10 for i in range(students[0])]
table212 = [[0]*10 for i in range(students[1])]
table213 = [[0]*10 for i in range(students[2])]
swp = [0] * 10
for i in range(10):
    swp[i] = "Singer " + "" + str(i)

for i in range(students[0]):
    for j in range(10):
        table211[i][j] = RS[swp[j]][i]

swp = [0] * 10
for i in range(10):
    swp[i] = "Singer " + "1" + str(i)

for i in range(students[1]):
    for j in range(10):
        table212[i][j] = RS[swp[j]][i]

swp = [0] * 10
for i in range(10):
    swp[i] = "Singer " + "2" + str(i)

for i in range(students[2]):
    for j in range(10):
        table213[i][j] = RS[swp[j]][i]



#for i in ('StudentName', swp[0], swp[1], swp[2], swp[3], swp[4], swp[5], swp[6], swp[7], swp[8], swp[9]):
    #for j in



def rec(estimating_group, usermark0, usermark1,usermark2, usermark3):

    # создадим префиксы, т.е. первую цифру исполнителя чтобы опредеилть каких исполнителей давать на оценку
    if estimating_group == 211:
        prefix = ""
    elif estimating_group == 212:
        prefix = "1"
    elif estimating_group == 213:
        prefix = "2"

    swp = [0]*10
    for i in range(10):
        swp[i] = "Singer " + prefix + str(i)

    RS['alpha'] = -2
    alpha_list = [0]*(students[estimating_group-211]+1)

    for i in range(1, students[estimating_group-211]+1):
        m1 = int(RS[swp[0]][i])
        m2 = int(RS[swp[1]][i])
        m3 = int(RS[swp[2]][i])
        m4 = int(RS[swp[3]][i])
        print(i, cosinus(m1 - 3, m2 - 3, m3 - 3, m4 - 3, usermark0 - 3, usermark1 - 3, usermark2 - 3, usermark3 - 3))
        RS.loc[i, 'alpha'] = cosinus(m1-3, m2-3, m3-3, m4-3, usermark0-3, usermark1-3, usermark2-3, usermark3-3)
        alpha_list[i] = cosinus(m1-3, m2-3, m3-3, m4-3, usermark0-3, usermark1-3, usermark2-3, usermark3-3)


    singer_coef = [-100]*10

    for i in range(4, 10):
        numerator = 0
        denominator = 0
        for j in range(1, students[estimating_group-211]+1):
            numerator += RS['alpha'][j] * RS[swp[i]][j]
        singer_mark_list = [0]* (students[estimating_group-211]+1)
        for j in range(1, students[estimating_group-211]+1):
            singer_mark_list[j] = RS[swp[i]][j]

        denominator = newlenght(*singer_mark_list) * newlenght(*alpha_list)
        singer_coef[i] = 2 * numerator / denominator

    best_singers = [0]*10
    for i in range(0, 10):
        for j in range(0, 10):
            if singer_coef[i] > singer_coef[j]:
                best_singers[i] += 1

    for i in range(0, 4):
        best_singers[i] = -100

    def indexmax(*arr):
        answer_list = [0] * 6
        for i in range(0, 6):
            answer_list[i] = best_singers.index(max(best_singers))
            best_singers[best_singers.index(max(best_singers))] = - 100
        return answer_list

    answer = []
    alpha_answer = []
    for i in indexmax(best_singers):
        print(RS[swp[i]][0])
        answer.append(RS[swp[i]][0])
        alpha_answer.append(singer_coef[i])
    return answer, alpha_answer




print(rec(211, 1, 2, 3, 4))
#a = [[1,2,3], [4,5,7]]
#for i in a:
#    print(i[0])#

#a = rec(211, 1, 2, 3, 4)

#print(rec(211, 1, 2, 3, 4))
#a, b = rec(211, 1, 2, 3, 5)
#print("fsdfmjksdfjsdkfjksdfjksdfjkfsdjkfjksdfjkf")
#print(a, b)
#print(a[0], type(a))
#print(b[0], type(b))#


