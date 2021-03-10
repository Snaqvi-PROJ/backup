#read_file = '/home/saif/Documents/new_env/test_prog/testfile.txt'

""" open
tasks = open('testfile.txt')
for chore in tasks:
  print chore
tasks.close()
"""

with open('testfile.txt', 'a') as log:
  print('a', 'b', file=log)
