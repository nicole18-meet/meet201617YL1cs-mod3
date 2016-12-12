class Student:
    def __init__(self, name, hometown, age, height, fav_ic_f):
        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.fav_ic_f=fav_ic_f
    def print_summary(self,name_request):
        self.name_request=name_request
        if name_request==self.name:
            print ("my name is "+self.name+", I live in "+self.hometown+
                   ", I'm "+self.age+" years old, my height (in cm) is "+
                   str(self.height)+" and my favorite ice cream flavor is "+self.fav_ic_f+".")
