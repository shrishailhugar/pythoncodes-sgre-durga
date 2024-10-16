from time import sleep
class Test:
    def __init__(self):
        print('Constructor')
    def __del__(self):
        print('Destroctor')
t=Test()
t=None
sleep(10)
print('End of program')