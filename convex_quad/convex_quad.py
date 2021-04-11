"""
Calculating the average area of a triangle when the points are chosen according to a 
certain distribution.
"""

import random

def random_point_draw():
	x = 2 * random.random() - 1
	y = 2 * random.random() - 1
	while x**2 + y**2 > 1:
		x = 2 * random.random() - 1
		y = 2 * random.random() - 1
	return (x,y)

def triple_random_draw():
	point_a = random_point_draw()
	point_b = random_point_draw()
	point_c = random_point_draw()
	return [point_a, point_b, point_c]

def find_triangle_area(point_list):
	point_a = point_list[0]
	point_b = point_list[1]
	point_c = point_list[2]
	lr_shoelaces = (point_a[0] * point_b[1]) + (point_b[0] * point_c[1]) + (point_c[0] * point_a[1])
	rl_shoelaces = (point_a[1] * point_b[0]) + (point_b[1] * point_c[0]) + (point_c[1] * point_a[0])
	area = abs((lr_shoelaces - rl_shoelaces)/2)
	return area

def calculate_area_average(num):
	counter = 0
	area_sum = 0
	while counter < num:
		new_triangle = triple_random_draw()
		triangle_area = find_triangle_area(new_triangle)
		counter += 1
		area_sum += triangle_area
	return area_sum/num


print(calculate_area_average(1000000))