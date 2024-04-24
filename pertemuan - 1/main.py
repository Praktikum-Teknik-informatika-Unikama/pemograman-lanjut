class Manusia:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def sayHello(self):
        print('Hello', self.name, ' anda sekarang berumur ', self.age)


nama = input('masukkan nama anda : ')
age = int(input('masukkan umur anda : '))
aufal = Manusia(nama, age)

aufal.sayHello()
