class magicmethods:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def __str__(self):
        return f"name of the student is {self.name}"
s=magicmethods("pranay",6699)
print(s)
