class daavana:
     def set(self,name,price):
        self.name=name
        self.price=price
     def output(self):
        print(f'davanas nosaukums {self.name}, cena {self.cena}')
d=daavana()
d.set('gramata',15)
daavana.output()