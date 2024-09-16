class person:
    def set(self,name,age):
        self.name=name
        self.age=age
    def output(self):
        print(self.name,self.age)
        print(self.labdien)
    def labdien(self):
        print(f'Labdien,{self.name}')

p=person()
skaits=int(input('Ievadiet cilveka skaitu: '))
for i in range(skaits):
    name=input('Ievadiet vardu: ')
    age=int(input('Ievadiet vecumu: '))
person.set(p,name,age)
person.output(p)