from socketIO_client import SocketIO
from select import select
import sys

playerKey = 'FPO3eDaQwp'
gameKey = 'fGmbGTO4EWX2EFP4fRwn'
socket_var = SocketIO('10.7.90.8', 4000)

def connection_response(*args):
  print args

def opponent_turn_response(*args):
  print 'Oppponent turn response'

def your_turn_response(*args):
  print 'Your turn:'
  #print args
  state = raw_input('Bot or Manual?')
  if(state == 'n'):
	  pos = raw_input('pos')
	  force = raw_input('force')
	  angle = raw_input('angle')
	  socket_var.emit('player_input', {'position': pos, 'force': force, 'angle': angle})
  else:
	  pos = 500
	  force = 4000
	  angle = 90
	  coins = args[0]['position']
	  #Do calculations here with coins object and calculate pos, force and angle for a particular coin.
	  through_coins = list()
	  for i in range(0,len(coins)):
		if coins[i]['x'] < (846.7742-30):
			through_coins.append(coins[i])
	 	y_position = coins[i]['y']
	  print through_coins
	  #print 'Coins data extracted from data:'
	  #print coins
	  #print 'Hit params that are going to be sent:',
	  #print pos, force, angle
	  socket_var.emit('player_input', {'position': pos, 'force': force, 'angle': angle})
 
print socket_var.connected
socket_var.emit("connect_game", {'playerKey': playerKey, 'gameKey': gameKey})
socket_var.on('connect_game', connection_response)
socket_var.on('opponent_turn', opponent_turn_response)
socket_var.on('your_turn', your_turn_response)
socket_var.on('player_input', connection_response)
socket_var.wait()
