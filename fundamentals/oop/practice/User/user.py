class user:
    def __init__(self,first_name,last_name,email,age):
      self.first_name=first_name
      self.last_name=last_name
      self.email=email
      self.age=age
      self.is_rewards_member="False"
      self.gold_card_points=0

    def display_info(self):
       print(f"Fisrt_name:{self.first_name}")
       print(f"Last_name:{self.last_name}")
       print(f"Email:{self.email}")  
       print(f"Age:{self.age}")
       print(f"Member:{self.is_rewards_member}")
       print(f"point:{self.gold_card_points}")

    def enroll(self) :
       self.is_rewards_member="True" 
       self.gold_card_points=200  

    def spend_points(self, amount) :
     if self.gold_card_points >= amount: 
        self.gold_card_points-=amount
        print(f"{amount} points spent. Remaining points: {self.gold_card_points}")
     else:
        print("Insufficient points.")


User1=user("Malek","Brahmia","brahmia.malek@yahoo.com",30)
User1.display_info()
User1.enroll()
User1.display_info()
User1.spend_points(50)
User1.display_info()
User2=user("joe","ali","hfyfgz@yahoo.com",31)
User2.display_info()
User2.enroll()
User2.display_info() 
User2.spend_points(80) 
User2.display_info() 

    
