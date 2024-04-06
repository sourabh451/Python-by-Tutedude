# Multi Level Inheritance
class A:

    def state_1(self):
        print("State_1 present")

    def state_2(self):
        print("State_2 present")

    def state_3(self):
        print("State_3 present")


class B(A):

    def state_4(self):
        print("State_4 present")

    def state_5(self):
        print("State_5 present")


class C(B):

    def state_6(self):
        print("State_6 present")

c = C()
c.state_1()
c.state_5()
c.state_6()
