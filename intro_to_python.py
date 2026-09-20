#hello how are you
#bla bla bla


"""
this is a
multiline comment
"""

'''
sadsadasdasd
'''
#print(2)

color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')

if color == "green":
  print('Go!')
elif color == "yellow":
  print('Slow Down!')
elif color == "red":
  print('Stop!')
else:
  print('Bogus!') 

