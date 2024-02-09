#def function():
#    print("Hi")


#function()

#def kidnames(*kids):
#    print("Names:" + kids[2])

#kidnames("Tobias","Matias")


#x = lambda a,b,c : a*b+c --> obtain one expression and calculate
#print(x(10,20,10)) 



class number:
    x = 5
y = number()
print(y.x)

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age 

            



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()


