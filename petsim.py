import random
import time

class Pet:
      def __init__(self, name, hunger=0, happiness=0, tiredness=0, health=0):
          self.name = name
          self.hunger = hunger
          self.happiness = happiness
          self.tiredness = tiredness
          self.pet_health = health

      def feed(self):
          self.hunger -= 1
          print(f"{self.name} is happy and no longer hungry")

      def play(self):
          self.happiness += 1
          self.tiredness += 1
          print(f"{self.name} says 'I'm so happy, woof woof'")

      def increase_health(self):
          self.pet_health += 1
          print(f"{self.name}'s health is now {self.pet_health}")

      def status(self):
          print(f"{self.name}'s hunger is {self.hunger}")
          print(f"{self.name}'s happiness is {self.happiness}")
          print(f"{self.name}'s tiredness is {self.tiredness}")
          print(f"{self.name}'s health is {self.pet_health}")

pet = Pet("Lulu") #change the name as you like
while True:
      user_choice = input("Enter 'feed', 'play', 'increase_health', 'status', or 'exit': ")
      if user_choice == "feed":
          pet.feed()
      elif user_choice == "play":
          pet.play()
      elif user_choice == "increase_health":
          pet.increase_health()
      elif user_choice == "status":
          pet.status()
      elif user_choice == "exit":
          break
      else:
          print("Invalid choice")
      time.sleep(1)
      pet.hunger += 1
      pet.happiness += 1
      pet.tiredness -= 1
print("goodbye")