import sys

print(sys.argv)

'''
output:- 
python commandline_argument.py java python ruby perl shell 1 2 3 4.4
['commandline_argument.py', 'java', 'python', 'ruby', 'perl', 'shell', '1', '2', '3', '4.4']

*All the input data will be treated as string by sys.argv; and index '0' always will be scriptName.
'''
print(sys.argv[0])
