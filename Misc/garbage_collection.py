"""Program to demonstrate how garbage collection works in Python"""
import sys
import gc

class Thing:
    def __init__(self):
        print('Initialized..')

    def __delete__(self, instance):
        print('All references deleted!')


ash = Thing()
brock = ash

brock = 4
print(sys.getrefcount(ash))
refers = gc.get_referrers(ash)
print(refers)
