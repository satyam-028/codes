class Parents: 
    def func(self):
        print("this is parent function")

class chlid(Parents):
    def func(self):
        print("the is child function")

c = chlid()
c.func()