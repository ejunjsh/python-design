class Interface:
    def request(self):
        return 0


class RealSubject(Interface):
    def request(self):
        print "Real request."


class Proxy(Interface):
    subject = None

    def __init__(self, subject):
        self.subject = subject

    def request(self):
        print "proxy do first."
        self.subject.request()


if __name__ == "__main__":
    p = Proxy(RealSubject())
    p.request()
