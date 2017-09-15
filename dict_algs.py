ivan = {
    'name': 'ivan',
    'age':34,
    'children':[{
        'name':'vasja',
        'age':12,
    }, {
        'name':'petja',
        'age':10,
    }],
}
darja = {
    'name':'darja',
    'age':41,
    'children':[{
        'name':'kirill',
        'age':21,
    }, {
        'name':'pavel',
        'age':15,
    }],
}
emps = [ivan, darja]
age=18
def filter (emps, age):
    z=''
    for name in emps:
        emp=name['children']
        for i in emp:
            if i['age']>age:
                z+= name['name']+'\n'
                break
    return z
#z=filter(emps, age)
print(filter(emps, age))