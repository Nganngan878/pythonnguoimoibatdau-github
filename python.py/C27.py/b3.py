#30/07/2026
"""
Constructor trong Python
"""
class SoPhuc:
    def __init__(self, r=0, i=0):
        self.phanthuc = r
        self.phanao = i

    def getData(self):
        print("{}+{}j".format(self.phanthuc, self.phanao))

    @classmethod
    def from_parts(cls, thuc, ao=0):
        return cls(thuc, ao)


c1 = SoPhuc(2, 3)
c1.getData()
c2 = SoPhuc.from_parts(5)
# it's allowed to set attributes on instances; avoid using the same name as methods
c2.new_attr = 10
print((c2.phanthuc, c2.phanao, c2.new_attr))

# access the classmethod via the class or the new name
_ = c1.from_parts