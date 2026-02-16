class hi:
    def __init__(self, name, id):
        self.name = name 
        self.id = id
        print(f"hi {name}")
    
    def show_id(self):
        print(f"id is {self.id}")

class bye(hi):
    def __init__(self, name, id):
        super().__init__(name, id)  # Call parent constructor
        print(f"bye {name}")
    
    def byy(self, name):
        self.name = name
        print(f"bye {name}")
    
    def show_id(self):  # Override parent method
        print(f"bye id is {self.id}")

obj = bye("samuel", 90)
obj.byy("samuel")
obj.show_id()  # Now this will work
