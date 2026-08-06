#6/08/2026
"""
Example 29-1. specialize.py
"""
class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()
class Inheritor(Super):
    def action(self):
        print('in Inheritor.action()')
class Replacer(Super):
    def method(self):
        print('in Replacer.method()')
class Extender(Super):
    def method(self):
        print(' starting Extndex.method')
        super().method()
        print('in Extender.method')
class Provider(Super):
    def action(self):
        print('in Provider.action()')
if __name__=='__main__':
    for klass in (Inheritor, Provider):
        print('\n'+klass.__name__+'...')
        klass().delegate()

    for klass in (Replacer, Extender):
        print('\n'+klass.__name__+'...')
        klass().method()

    print('\nProvider')
    x = Provider()
    x.delegate()
          