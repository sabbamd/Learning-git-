# delete the static variable --> Anywhere:  del classname.variablename , class method : del cls.variable name
class test:
    a = 40

    def __init__(self):
        test.b = 30
        del test.a

    def m1(self):
        test.c = 50
        del test.b

    @classmethod
    def m2(cls):
        cls.d = 60
        del test.c

    @staticmethod
    def m3():
        test.e = 100
        del test.d


t = test()
t.m1()
test.m2()
test.m3()
print(test.__dict__)
