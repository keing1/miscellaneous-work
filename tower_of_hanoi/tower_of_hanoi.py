"""
Let's say you have a tower of Hanoi puzzle with three disks. If you randomly make a legal
move at every timestep, how many moves in expectation will it take to win the game and
move all three disks to another pillar?

More context can be found here: 
https://fivethirtyeight.com/features/can-you-randomly-move-the-tower/
"""

import numpy as np

def find_move_list(pillar_1, pillar_2, pillar_3):
	move_list = []

	top_list = []

	if len(pillar_1) > 0:
		top_list += [(1,pillar_1[-1])]
	if len(pillar_2) > 0:
		top_list += [(2,pillar_2[-1])]
	if len(pillar_3) > 0:
		top_list += [(3,pillar_3[-1])]

	if len(top_list) == 1:
		no_disk_list = [elem for elem in [1,2,3] if elem not in [a[0] for a in top_list]]
		move_list = [(top_list[0][0], no_disk_list[0]),
		 			(top_list[0][0], no_disk_list[1])]
	elif len(top_list) == 2:
		no_disk_list = [elem for elem in [1,2,3] if elem not in [a[0] for a in top_list]]
		sorted_top_list = sorted(top_list, key=lambda s: s[1])
		move_list = [(sorted_top_list[0][0], sorted_top_list[1][0]),
		 			(sorted_top_list[0][0], no_disk_list[0]),
		 			(sorted_top_list[1][0], no_disk_list[0])]
	else:
		 sorted_top_list = sorted(top_list, key=lambda s: s[1])
		 move_list = [(sorted_top_list[1][0], sorted_top_list[2][0]),
		 			(sorted_top_list[0][0], sorted_top_list[2][0]),
		 			(sorted_top_list[0][0], sorted_top_list[1][0])]

	return move_list

def make_move(pillar_1, pillar_2, pillar_3, move_list):
	move_index = np.random.randint(len(move_list))
	move = move_list[move_index]
	pillar_dict = {1: pillar_1, 2: pillar_2, 3: pillar_3}

	take_pillar = pillar_dict[move[0]]
	give_pillar = pillar_dict[move[1]]

	disk_move = take_pillar.pop()
	give_pillar += [disk_move]
	return

def run_hanoi():
	num_moves = 0
	pillar_1 = [3,2,1]
	pillar_2 = []
	pillar_3 = []

	while len(pillar_2) < 3 and len(pillar_3) < 3:
		my_moves = find_move_list(pillar_1, pillar_2, pillar_3)
		make_move(pillar_1, pillar_2, pillar_3, my_moves)
		num_moves += 1

	return num_moves

def run_hanoi_multiple(num_games):
	hanoi_total = 0

	for i in range(num_games):
		if i % 1000000 == 0:
			print('Game number: {}'.format(i+1))
		hanoi_total += run_hanoi()

	return hanoi_total / num_games


if __name__ == '__main__':
	print(run_hanoi_multiple(10000000))
