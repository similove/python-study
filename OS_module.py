import os
from pprint import pprint
r = os.listdir('.')
# os.mkdir('aaa')
# os.mkdir('bbb')
# os.rmdir('aaa')
# os.rmdir('bbb')
# os.remove('xxx.flv')
pprint(r)
cwd = os.getcwd()
pprint(cwd)

