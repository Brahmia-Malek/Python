class Ninja ():
  def __int__(self,first_name,last_name,treats,pet_food , pet):
       self.first_name=first_name
       self.last_name=last_name
       self.treats=treats
       self.pet_food=pet_food 
       self.pet=pet
  def walk(self):
      self.pet.play()
      return(self)
  def bathe(self):
      self.pet.noise()
      return(self)