# I made myself

import random

print('Welcome to the DDLC bio reader')

def main():
  char = input('Which character do you want to know about?\n').lower()
  if char == 'sayori':
    print('Sayori: Cheerful and optimistic friend. Loves to help others.')
  elif char == 'natsuki':
    print('Energetic and passionate about baking. Can be quite tsundere.')
  if char == 'yuri':
    print('Shy and reserved. Enjoys reading and intellectual discussions. Reads portrait of markov, presumably libitina')
  if char == 'monika':
    print('Confident and driven leader of the Literature Club. The antogonist')

a = random.randint(1, 10)
if a == 1:
  print('Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head Get out of my head ')
else:
  main()
