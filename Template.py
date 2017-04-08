class ExamPager:
    def question1(self):
        print "Exam1:A. B. C. B."
        print "(%s)" % self.answer1()

    def question2(self):
        print "Exam2:A. B. C. B."
        print "(%s)" % self.answer2()

    def answer1(self):
        pass

    def answer2(self):
        pass


class ExamPagerA(ExamPager):
    def answer1(self):
        return "A"

    def answer2(self):
        return "B"


class ExamPagerB(ExamPager):
    def answer1(self):
        return "C"

    def answer2(self):
        return "D"


if __name__ == "__main__":
    s1 = ExamPagerA()
    s2 = ExamPagerB()
    print "student 1"
    s1.question1()
    s1.question2()
    print "student 2"
    s2.question1()
    s2.question2()
