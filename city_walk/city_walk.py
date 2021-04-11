"""
Take a 3x3 grid of city intersections, ranging from (0,0) to (2,2). Let all roads connecting
these intersections be one-way roads, where the direction of the one-way road is chosen
randomly. What fraction of the time is it possible to make it from (0,0) to (2,2) following
the one-way roads? Further context can be found in the 'Riddler Classic' problem here:
https://fivethirtyeight.com/features/can-you-navigate-the-one-way-streets/

I also extended this problem to the case of determining whether you can travel from (0,0)
to (2,2) as well as (2,2) to (0,0).
"""


import random

def create_edge_graph():
	edge_dict = {}
	for x in range(3):
		for y in range(3):
			if x+1 < 3:
				val = random.randint(0,1)
				if val:
					if (x,y) not in edge_dict:
						edge_dict[(x,y)] = [(x+1,y)]
					else:
						edge_dict[(x,y)] += [(x+1,y)]
				else:
					if (x+1, y) not in edge_dict:
						edge_dict[(x+1,y)] = [(x,y)]
					else:
						edge_dict[(x+1,y)] += [(x,y)]
			if y+1 < 3:
				val = random.randint(0,1)
				if val:
					if (x,y) not in edge_dict:
						edge_dict[(x,y)] = [(x,y+1)]
					else:
						edge_dict[(x,y)] += [(x,y+1)]
				else:
					if (x,y+1) not in edge_dict:
						edge_dict[(x,y+1)] = [(x,y)]
					else:
						edge_dict[(x,y+1)] += [(x,y)]

	return edge_dict


def perform_search(start_point, end_point, edge_dict):
	reachable_set = set([start_point])

	curr_points = [start_point]
	while len(curr_points) > 0:
		if end_point in reachable_set:
			return True
		curr_point = curr_points.pop()
		if curr_point in edge_dict:
			adjacencies = edge_dict[curr_point]
			for next_point in adjacencies:
				if next_point not in reachable_set:
					reachable_set.add(next_point)
					curr_points.append(next_point)
	return False

def run_round(start_point, end_point, both_directions):
	edge_dict = create_edge_graph()

	forward_bool = perform_search(start_point, end_point, edge_dict)

	if both_directions:
		if forward_bool:
			backward_bool = perform_search(end_point, start_point, edge_dict)
			return forward_bool and backward_bool
		else:
			return False

	return forward_bool

	

def run_multiple_rounds(start_point, end_point, num_rounds, both_directions=False):
	num_wins = 0
	for curr_round in range(num_rounds):
		if run_round(start_point, end_point, both_directions):
			num_wins += 1

	return num_wins/num_rounds

print(run_multiple_rounds((0,0), (2,2), 1000000))


print(run_multiple_rounds((0,0), (2,2), 1000000, True))



