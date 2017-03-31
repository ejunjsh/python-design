class LeiFeng:
    def sweep(self):
        print "LeiFeng sweep"

class Student(LeiFeng):
    def sweep(self):
        print "Student sweep"

class Violenteer(LeiFeng):
    def sweep(self):
        print "Violenteer sweep"

        
    def __call__(self):
        print "__call__"

class LeiFengFactory:
    def createLeiFeng(self):
        return LeiFeng()

class StudentFactory:
    def createStudent(self):
        return Student()

class ViolenteerFactory:
    def createViolenteer(self):
        return Violenteer()


if __name__=="__main__":
    sf=StudentFactory()
    s=sf.createStudent()
    s.sweep()
    sdf=ViolenteerFactory()
    sd=sdf.createViolenteer()
    sd.sweep()
    sd()