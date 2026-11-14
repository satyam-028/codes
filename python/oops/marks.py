class Students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0 
        for i in self.marks:
            sum += i
        print("hlo", self.name, "your socre is : ", sum/3)
        
s1 = Students('satyam', [77,78,56])
s1.get_avg()

s1.name = "sharma"
s1.get_avg()
