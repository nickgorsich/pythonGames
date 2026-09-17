##################################################################################################
'''
Treasure Hunt Text Game
'''
# -------------------------- SET UP -----------------------------------
import time, os
location = 2
player = {'items':[], 'money':0, 'hitpoints':100}
#####################################################---------- HELPERS ---------#################
def win():
  os.system('cls')
  print (BACKGROUND + 'You have won the game. Thanks for playing. \n')
  end_time = time.time()
  x = end_time - start_time
  print('\u001b[0m')
  print(f'It took you {x:.2f} seconds to finish the game.')
  print('Check leaderboard_times to see where you rank on the leaderboard.')
  f = open('leaderboard_times.txt', 'r')
  lines = f.readlines() 
  f.close()
  scores = []
  for line in lines:
    score = float(line.strip())
    scores.append(score)
  scores.append(x)
  scores.sort()
  f = open('leaderboard_times.txt', 'w')
  for score in scores:
    f.write(str(score) + '\n')
  f.close()
  time.sleep(5)
  quit()
# ------------------------------------
def help():
  print('\u001b[37m')
  print ('commands are as follows.')
  print ('[stay], [east], [west]')
  game()
#------------------------------------
def help2():
  print('\u001b[37m')
  print ('commands are as follows.')
  print ('[work] and [search]')
  game()
##############################################################################################
'''
Locations
'''
##########################--------------- BEACH -------------------##############################
def beach():
  print('\033[93m')
  print('You are at the beach.')
  a = input('Enter [work] or [search]: ')
  if a == 'help':
    help2()
  elif a == 'quit':
    print('thanks for playing')
    player['hitpoints'] -= 1000
  elif a == 'work':
    print ('You find work and make 10 moneys.')
    player['money'] += 10  
  elif a == 'search':
    print ('You see sand')
    a = input('Would you like to lay in the sand or dig?: ')
    if a == 'lay':
      print ('You lay down and rest. You gain 5 hp')
      player['hitpoints'] += 5
    elif a == 'dig' and 'shovel' in player['items'] and 'map' in player['items']:
      print('You use your map to find a key, and your shovel to dig it up.')
      print('You have the key!')
      player['items'].append('key')
    elif a == 'dig' and 'shovel' in player['items'] and 'map' not in player['items']:
      print('You dig with your shovel but can not find key.')
    elif a == 'dig' and 'shovel' not in player['items'] and 'map' in player['items']:
      print('You find where key is but can not dig it up.')
    elif a == 'dig' and 'shovel' not in player['items'] and 'map' not in player['items']:
      print('you need a shovel to dig, and a map to locate key')
    else:
      print ('not a valid command. commands are [dig] and [lay]')
  else:
    print ('Not a valid command.')
  time.sleep(4)
  os.system('cls')
  game()
######################--------------- FIELDS -------------------##############################
def fields():
  print('\u001b[34m')
  print('You are in fields.')
  a = input('Enter [work] or [search]: ')
  if a == 'help':
    help2()
  elif a == 'quit':
    print('thanks for playing')
    player['hitpoints'] -= 1000
  elif a == 'work':
    print('there is no work to be found')
  elif a == 'search':
    print('You see a caravan traveling in the distance.')
    a = input ('Do you want to [rob] the caravan or [join] them?: ')
    if a == 'rob':
      if 'knife' in player['items']:
        print ('You whip out your knife and do mean things. The caravan had a lot of money.')
        time.sleep(2)
        player['money'] += 50
        player['hitpoints'] -= 15
      else:
        print('You have no weapons to attack with.')
    elif a == 'join':
      print ('You ask to join their caravan for safer travel.')
      print ('They throw a knife at you and it lands near your feet. You take it as a no.')
      print('You pick up the knife')
      time.sleep(3)
      player['items'].append('knife')
    else:
      print('Not a valid command. Enter [rob] or [join]')  
  else:
    print ('Not a valid command.')
  time.sleep(3)
  os.system('cls')
  game()
#######################--------------- TOWN -------------------##############################
def town():
  print('\u001b[33m')
  print('You are in town.')
  a = input('Enter [work] or [search]: ')
  if a == 'help':
    help2()
  elif a == 'quit':
    print('thanks for playing')
    player['hitpoints'] -= 1000
  elif a == 'work':
    print ('You find hard work and make 15 moneys.')
    player['money'] += 15
    player['hitpoints'] -= 10   
  elif a == 'search':
    print ('You find a store. Map: $20  Binoculars: $40')
    a = input('Would you like to buy map, binoculars or leave store?: ')
    if a == 'map' and player['money'] >= 20:
      print ('You buy map.')
      player['money'] -= 20
      player['items'].append('map')
    elif a == 'binoculars' and player['money'] >= 40:
      print ('You buy binoculars.')
      player['money'] -= 40
      player['items'].append('binoculars')
    elif a == 'leave':
      print ('you leave shop')
    else:
      print('not enough money or not a valid command. enter [map],  [binoculars] or [leave]. if not enough money, find work')
      time.sleep(2)
  else:
    print ('Not a valid command.')
  game() 
########################--------------- FOREST -------------------###########################
def forest():
  print('\u001b[32m')
  print('You are in a forest.')
  a = input('Enter [work] or [search]: ')
  if a == 'help':
    help2()
  elif a == 'quit':
    print('thanks for playing')
    player['hitpoints'] -= 1000
  elif a == 'work':
    print ('You find strenuous labor and lose hp. You do not get money but they leave you with a shovel.')
    player['hitpoints'] -= 20
    player['items'].append('shovel')
    time.sleep(3)
  elif a == 'search':
    print ('You find a tavern and a poor man outside')
    a = input('Would you like to [enter] or [talk] to the old man?: ')
    if a == 'enter':
      print ('you drink and gain hp')
      player['hitpoints'] += 10
    elif a == 'talk':
      print ('the old man reveals secrets')
      print('He tells you of a treasure hidden in the mountains. binoculars are required to find it. a key is needed to open it. The key is located at the beach.')
      time.sleep(8)
    else:
      print('not a valid command. enter [enter] or [talk]')
  else:
    print ('Not a valid command.')
  time.sleep(3)
  os.system('cls')
  game()
######################--------------- MOUNTAINS -------------------###############################
def mountains():
  print('\u001b[31m')
  print('You are in the mountains.')
  a = input('Enter [work] or [search]: ')
  if a == 'help':
    help2()
  elif a == 'quit':
    print('thanks for playing')
    player['hitpoints'] -= 1000
  elif a == 'work':
    print('there is no work to be found')
  elif a == 'search':
    print('You find yourself on trails')
    a = input('Would you like to adventure by [day] or [night]?: ')
    if a == 'night':
      print('You are happily walking and fall down a cliff.')
      player['hitpoints'] -= 60
    elif a == 'day':
      print('You walk the trail and never find anything')
      b = input ('Do you have binoculars?: ')
      if b == 'yes':
        if 'binoculars' in player['items']:
          print('You look through the binoculars and you find the treasure hidden in a cave!')
          c = input('Do you have the key?: ')
          if c == 'yes':
            print('You pull out your key and open the treasure!')
            time.sleep(2)
            print('Lying inside is infinite money and happiness')
            time.sleep(4)
            win()
          elif c == 'no':
            print ('Need key to open treasure, go find it')
          else:
            print('not a valid command. enter [yes] or [no]')
        else:
          print('Liar')
      elif b == 'no':
        print('Go buy some.')
      else:
        print('not a valid command. enter [yes] or [no].')
    else: 
      print('not a valid command. Enter [day] or [night]')
    
  else:
    print ('Not a valid command.')
  time.sleep(4)
  os.system('cls')
  game()
#####################--------------- WORLD -------------------##############################
world = [
  'Beach',
  'Fields',
  'Town',
  'Forest',
  'Mountains'
  ]

##################################################################################################
#####################--------------- MAIN PROGRAM -------------------#############################
##################################################################################################
start_time = time.time()
BACKGROUND ='\033[7m' 
RESET = '\u001b[0m'
print ('Welcome to game! Object:')
print (BACKGROUND + 'FIND AND OPEN THE TREASURE BEFORE YOU DIE.' + RESET)
print ('To find the treasure you must [stay] at locations.')
print ('Enter [work] and [search] AFTER staying at locations.')
print ('Enter [help] at any point for commands.')
print ('Enter [quit] to leave game.')
print ('Hint: Keep an eye on hitpoints (you can gain HP).')
##################################################################################################
'''
Cental Game Code
'''

def game():
  global location
  while player['hitpoints'] >= 1:
    print('-----------------------------------')
    print ('Items:', player['items'], ' Money:', player['money'], ' Hitpoints:', player['hitpoints'])
    print ('\nYou are at', world[location])
    a = input('[stay] at '+(world[location])+', go [east], or go [west]?: \n\n->')
    if a == 'stay':
      if location == 0:
        return beach()
      elif location == 1:
        return fields()
      elif location == 2:
        return town()
      elif location == 3:
        return forest()
      elif location == 4:
        return mountains()
      
    elif a == 'east':
      location = (location - 1) % 5
      game() 
    elif a == 'west':
      location = (location + 1) % 5
      game()
    elif a == 'help':
      help()
    elif a == 'quit':
      print('thanks for playing')
      player['hitpoints'] -= 1000
    else:
      print('not a valid command. Enter [east] or [west]')
  while player['hitpoints'] <= 0:
    print('You have died.')
    print('Thanks for playing')
    time.sleep(5)
    quit()
##################################################################################################

''' To Do List:

- Fix Leaderboard write ups and display leaderboard.
- Refine commands and make more user friendly.


- Turn into Website???'''

print(10%9)
# game()

print('\u001b[0m') # reset terminal colors