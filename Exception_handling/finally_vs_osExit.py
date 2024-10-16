import os
try:
    print('try')
    os._exit(0)
except:
    print('except')
finally:
    print('finally')