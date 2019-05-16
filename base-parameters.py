#! /usr/bin/python3

import argparse
import sys
sys.path.append('D:\\git\\RDES')
import RDES as rd

def main():
	temp=rd.read_txt(parse_arguments().path)
	data=[]
	for ch in temp:
		data.append(int(ch))
	bp = calculate_base_parameter(data)
	print('Base parameter is ' + str(bp))

def calculate_base_parameter(data):
	bp = 1
	while True:
		subsets = break_into_subsets(data, bp)
		if find_twins(subsets):
			bp += 1
		else:
			return bp
			
def break_into_subsets(data, length):
	return [data[x:x+length] for x in range(len(data)-length+1)]
	
def find_twins(data):
	for d in data:
		if data.count(d) > 1:
			return True
	return False
	
def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument('path', type=str)
	args = parser.parse_args()
	return args
	
if __name__ == '__main__':
	main()
