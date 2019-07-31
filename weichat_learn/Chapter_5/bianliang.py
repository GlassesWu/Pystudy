name = '111'


def func1(n = name):
    print(n)

def func2():
    name = '222'
    func1(name)

func2()