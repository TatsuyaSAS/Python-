class Main:
    def __init__(self,num):
        self.num = num

    def Hei(self):
        for i in range(1, self.num+1):
            if self.num > (self.num / i) ** 2:
                break
        print(i-1)
        
num = int(input('数値:'))
Main(num).Hei()
#for j in range(i * 10,  (i - 1) * 10, -1):
#    if x < (x / (j / 10)) ** 2:
#        break