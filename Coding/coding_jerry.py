# Project: Coding question from Jerry.ai
# Made by: Haomin Lin
##################################################################################
# The idea of this program is to model disjoint intervals with breakpoints
# in a continuous integer series, where each time a new interval comes in or
# get removed, the corresponding point in the series will be flagged or unflagged.
##################################################################################
# The runtime of this program basically consists of two parts taking O(n) time in total:
# (1) add/remove: take O(n) time to update the flag values in the series;
# (2) update the disjoint intervals with flag values, traverse the sequence with O(n) time.
# P.S. n represents the largest number in the disjoint intervals.
##################################################################################
# This program runs by manually input data and commands.

class disjoint_intervals:
	def __init__(self,members=[],data={}):
		self.members=members # stores disjoint intervals
		self.data=data # stores flag values

	def update(self,a,b):
		# scan through existing data range
		left_end = min(self.members[0][0],a)
		right_end = max(self.members[-1][1],b)
		# stores the left ends and right ends of intervals
		number_one,number_two = [],[] 

		cur_num = 0
		for num in range(left_end,right_end+1):
			try:
				if self.data[num]==1 and cur_num==0:
					number_one.append(num)
					cur_num = 1
				if self.data[num]==0 and cur_num==1:
					number_two.append(num)
					cur_num = 0
			except:
				if cur_num==1:
					number_two.append(num)
					cur_num = 0
		number_two.append(right_end)
		self.members=[]
		for (l,r) in dict(zip(sorted(number_one),sorted(number_two))).items():
			self.members.append([l,r]) 

	def add(self,a,b):
		for num in range(a,b):
			self.data[num]=1
		if len(self.members)==0:
			self.members.append([a,b])
			return
		if a-1!=self.members[0][0] and a > self.members[-1][1]:
			self.data[a-1]=0 # mark the new neighboring interval to avoid merging
		self.update(a,b)

	def remove(self,a,b):
		if len(self.members)==0:
			print("nothing to remove, please add first")
			return
		if a < self.members[0][0] or b > self.members[-1][1]:
			print("please make sure removed items stay in range and try again")
			return
		for num in range(a,b):
			self.data[num]=0
		self.update(a,b)

	def act(self):
		while True:
			input_data = input("input operated data (a,b)\n")
			try:
				left = int(input_data.split(",")[0])
				right = int(input_data.split(",")[1])
			except:
				print("wrong input, try again\n")
				continue

			while True:
				command = input("action = add(0) or remove(1)\n")
				if command == "0":
					self.add(left,right)
					break
				elif command == "1":
					self.remove(left,right)
					break
				else:
					print("illegal action, try again\n")

			print(self.members)
			stop = input("stop(1) or contine(any other key)\n")
			if stop == "1":
				break

if __name__ == "__main__":
	disjoint_intervals_sequence = disjoint_intervals()
	disjoint_intervals_sequence.act()
