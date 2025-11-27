class User:
    def __init__(self,name,age,worky):
        self.age = age
        self.name = name
        self.worky = worky

class Car:
    def __init__(self,title,color,year):
        self.title = title
        self.color = color
        self.year = year

class Bir:
    def __init__(self, user, car):
        self.user = user
        self.car = car

class Admin:
    def __init__(self):
        self.users = []
        self.cars = []
        self.adb = []

    def addUser(self):
        user1 = input("Enter the name : ")
        age = input("Enter the age : ")
        worky = input("Enter the working year : ")
        su = User(user1,age,worky)
        self.users.append(su)

    def addCar(self):
        car1 = input("Enter the car name : ")
        color = input("Enter the color : ")
        year = input("Enter the car year : ")
        sc = Car(car1,color,year)
        self.cars.append(sc)

    def printUs(self):
        count = 0
        print("_"*40)
        for user in self.users:
            count+=1
            print(f"{count}. {user.name} {user.age} {user.worky}")

    def printCars(self):
        count = 0
        print("_"*40)
        for car in self.cars:
            count+=1
            print(f"{count}. {car.title} {car.color} {car.year}")

    def birl(self):
        print("=="*20)
        self.printUs()
        print("--"*20)
        self.printCars()
        print("=="*20)
        t1 = int(input("Enter user number : ")) - 1
        t2 = int(input("Enter car number : ")) - 1
        try:
            s1 = Bir(self.users[t1], self.cars[t2])
            self.adb.append(s1)
            self.users.pop(t1)
            self.cars.pop(t2)
        except:
            print("No id found")

    def birl_print(self):
        count = 1
        print("="*30)
        for obj in self.adb:
            print(
                f"{count}. {obj.user.name} {obj.user.age} {obj.user.worky} --> {obj.car.title} {obj.car.color} {obj.car.year}")
            count += 1
    def user_edit(self):
        name = input("Enter user name : ")
        for i in self.users:
            if i.name == name:
                i.name = input("Enter new name : ")
                i.age = input("Enter new age : ")
                i.worky = input("Enter new working year : ")

    def car_edit(self):
        car = input("Enter car name : ")
        for i in self.cars:
            if i.title == car:
                i.title = input("Enter new title : ")
                i.color = input("Enter new color : ")
                i.year = input("Enter new year : ")

    def user_del(self):
        name = input("Enter user name : ")
        for i in self.users:
            if i.name == name:
                self.users.remove(i)
                print("Removed successfully")

    def car_del(self):
        title = input("Enter car name : ")
        for i in self.cars:
            if i.title == title:
                self.cars.remove(i)
                print("Removed successfully")

    def birl_del(self):
        count = 1
        print("=" * 30)
        for obj in self.adb:
            print(
                f"{count}. {obj.user.name} {obj.user.age} {obj.user.worky} --> {obj.car.title} {obj.car.color} {obj.car.year}")
            count += 1
        a1 = int(input("Enter the connection you want to delete : ")) - 1
        t = self.adb[a1]
        user1 = User(t.user.name,t.user.age,t.user.worky)
        car1 = Car(t.car.title,t.car.color,t.car.year)
        self.users.append(user1)
        self.cars.append(car1)
        self.adb.remove(t)


r = Admin()

def manager(s:Admin):
    while True:
        a = input(" 1.Add menu\n 2.Edit menu\n 3.Print menu\n 4.Manage menu\n 5.Delete menu \n 6.Exit\n----->")
        if a == "1":
            while True:
                b = input(" 1.add user\n 2.add car\n 3.exit")
                if b == "1":
                    s.addUser()
                elif b == "2":
                    s.addCar()
                else:
                    break
        elif a == "2":
            while True:
                b = input(" 1.edit user\n 2.edit car\n 3.exit")
                if b == "1":
                    s.user_edit()
                elif b == "2":
                    s.car_edit()
                else:
                    break
        elif a == "3":
            while True:
                b = input(" 1.print users\n 2.print cars\n 3.print groups\n 4.exit")
                if b == "1":
                    s.printUs()
                elif b == "2":
                    s.printCars()
                elif b == "3":
                    s.birl_print()
                else:
                    break
        elif a == "4":
            while True:
                b = input(" 1.manage groups\n 2.exit")
                if b == "1":
                    s.birl()
                else:
                    break
        elif a == "5":
            while True:
                b = input(" 1.delete user\n 2.delete car\n 3.delete groups\n 4.exit")
                if b == "1":
                    s.user_del()
                elif b == "2":
                    s.car_del()
                elif b == "3":
                    s.birl_del()
                else:
                    break
        else:
            break

manager(r)



