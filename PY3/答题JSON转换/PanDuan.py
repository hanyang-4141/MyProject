f = open(r'd:\panduandaan.txt', 'r',encoding='UTF-8')
strlist = f.read()
# print(strlist)
l1 = strlist.split('；')
pd_daan = []
print(l1)
for ll in l1:
    ll = ll[-1:]
    if ll == '√':

        pd_daan.append(True)
    else:
        pd_daan.append(False)
print(pd_daan)


ff = open(r'd:\panduan.txt', 'r',encoding='UTF-8')
strlist1 = ff.readlines()
print(strlist1)

Questions = []
print('题目长度',len(strlist1))
print('答案长度',len(l1))
for index,h in enumerate(strlist1):
    mydict = {}
    print(h)
    mydict.setdefault('answer', pd_daan[index])
    mydict.setdefault('options', [{'checked': False,'name':'正确','value':'A'},{'checked': False,'name':'错误','value':'B'}])
    mydict.setdefault('title', h)

    Questions.append(mydict)
# print(Questions)
# for q in Questions:
#     print(q)
import  json
ddd = {}
ddd.setdefault('PanDuan',Questions)
print(ddd)
myjson = json.dumps(ddd)
print(myjson)