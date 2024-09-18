# This is from a youtube class I took on OOP from google

class Apple:
    color = ""
    flavor = ""
    
jonagold = Apple()
jonagold.flavor = "sweet"
jonagold.color = "red"

print(jonagold.color.upper())
print(jonagold.flavor.capitalize())


################################################################

class Piglet:
    name = "piglet"
    def speak(self):
        print("Oink! I'm {}! Oink!". format(self.name))

hamlet = Piglet()
hamlet.name = "hamlet"
print(hamlet.speak())

Petunia = Piglet()
Petunia.name = "Petunia"
print(Petunia.speak())


################################################################


class PigletAge:
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = PigletAge()
piggy.years = 2
print(piggy.pig_years())
