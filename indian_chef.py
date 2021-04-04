# from _distutils_hack import override

from masterchef import MasterChef


class IndianChef(MasterChef):

    def make_roti(self):
        print("makes tandoori roti")

    def make_dal(self):
        print("makes dal makhni")

    def make_dessert(self):
        print("makes gajar ka halwa")
