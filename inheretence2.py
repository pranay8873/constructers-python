class printt:
   def __init__(self,name,id):
     self.name=name
     self.id=id
   def showname(self):
      print(f"name is {self.name}")
   def showid(self):
      print(f"id is {self.id}")
class tell(printt):
  def __init__(self,name,id):
     self.name=name
     self.id=id
  def tellname(self):
     print(f"tell name is {self.name}")
  def tellid(self):
     print(f"tell id is {self.id}")
obj1=printt("pranay",99)
obj2=tell("vaishnavi",0)
obj2.showname()
obj1.showname()
obj2.tellname()
obj2.tellid()
obj2.showid()
obj1.showid()
