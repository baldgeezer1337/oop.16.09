class person:
    def set(self,name,age):
        self.name=name
        self.age=age
    def labdien(self,name,labdien):
        self.labdien=labdien
    def output(self):
        print(self.name,self.age)
        print(self.labdien)

p=person()
p.set('Peter',20)
p.output()