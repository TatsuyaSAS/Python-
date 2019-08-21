class Main:
    def __init__(self, num, deci):
        self.num = num
        self.deci = deci

    def Hei(self):
        for i in range(1, self.num+1):
            if self.num > (self.num / i) ** 2:
                break
                
        root = i - 1 + 0.1 ** self.deci
        
        for i in range(self.deci):
            while root ** 2 < self.num:
                root += 0.1 ** (i + 1)
            else:
                root -= 0.1 ** (i + 1)
                
        print(round(root, self.deci))
        
        
num = int(input('数値:'))
deci = int(input('桁数:'))

Main(num,deci).Hei()