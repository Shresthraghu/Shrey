stu={}
print(stu)

stu={
    'nm':'Anu',
    'cls':12,
    'phy':90,
    'che':80,
    'mat':85
    }
print(stu)
cl=[12,2,3]
stu={
    'nm':['Anu','renu','tiya'],
    'cls':cl,
    'phy':[90,50,80],
    'che':80,
    'mat':85
    }
print(stu)
print("---------------------")
print(stu['phy'])
print("---------------------")
print(stu['cls'])
stu['phy']=[100,200]
print("---------------------")
print(stu['phy'])
print(stu)
for k,v in stu.items():
    print(k,v)
