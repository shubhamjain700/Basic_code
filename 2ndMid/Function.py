# def xyz():
#     def local():
#         a=10
#     def local():
#         a=10
#     def non_local():
#         nonlocal a
#         a=10


# d={'a':'b'}
# d[d.update({'b':'a'})] = d.clear()
# print(d)
# def xyz(name,age,section):
#     f = '''
#     :param name: {}
#     :param age: {}
#     :param section: {}
#     '''.format(name,age,section)
#     return f
# re = xyz('Ravi','B',20)
# print(re)
D = {'name':'Ram','Age':25}
for i in D:
    D[i.lower()]=D.pop(i)
print(D)