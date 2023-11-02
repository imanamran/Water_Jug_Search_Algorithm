# 3 water jugs capacity -> (x,y,z) where x>y>z
# initial state (12,0,0)
# final state (6,6,0)
		
capacity = (10,6,5) 
# Maximum capacities of 3 jugs -> x,y,z
x = capacity[0]
y = capacity[1]
z = capacity[2]

# to mark visited states
memory = {}

# store solution path
ans = []

def depth_first_search(state):
	# Let the 3 jugs be called a,b,c
	a = state[0]
	b = state[1]
	c = state[2]

	if(a==0 and b==0 and c==1):
		ans.append(state)
		return True

	# if current state is already visited earlier
	if((a,b,c) in memory):
		return False

	memory[(a,b,c)] = 1

	#fill jug
	if(a>=0 and a < x):
		if( depth_first_search((x,b,c)) ):
				ans.append(state)
				return True
	
	if(b>=0 and b < y):
		if( depth_first_search((a,y,c)) ):
				ans.append(state)
				return True

	if(c>=0 and c < z):
		if( depth_first_search((a,b,z)) ):
				ans.append(state)
				return True

	#empty jug a
	if(a>0):
		#empty a into b
		if(a+b<=y):
			if( depth_first_search((0,a+b,c)) ):
				ans.append(state)
				return True
		else:
			if( depth_first_search((a-(y-b), y, c)) ):
				ans.append(state)
				return True
		#empty a into c
		if(a+c<=z):
			if( depth_first_search((0,b,a+c)) ):
				ans.append(state)
				return True
		else:
			if( depth_first_search((a-(z-c), b, z)) ):
				ans.append(state)
				return True

	#empty jug b
	if(b>0):
		#empty b into a
		if(a+b<=x):
			if( depth_first_search((a+b, 0, c)) ):
				ans.append(state)
				return True
		else:
			if( depth_first_search((x, b-(x-a), c)) ):
				ans.append(state)
				return True
		#empty b into c
		if(b+c<=z):
			if( depth_first_search((a, 0, b+c)) ):
				ans.append(state)
				return True
		else:
			if( depth_first_search((a, b-(z-c), z)) ):
				ans.append(state)
				return True

	#empty jug c
	if(c>0):
		#empty c into a
		if(a+c<=x):
			if( depth_first_search((a+c, b, 0)) ):
				ans.append(state)
				return True
		elif():
			if( depth_first_search((x, b, c-(x-a))) ):
				ans.append(state)
				return True
				
		#empty c into b
		if(b+c<=y):
			if( depth_first_search((a, b+c, 0)) ):
				ans.append(state)
				return True
		else:
			if( depth_first_search((a, y, c-(y-b))) ):
				ans.append(state)
				return True
		
		if(a == 0):
			if( depth_first_search((a, b, 0)) ):
					ans.append(state)
					return True
		

initial_state = (3,0,0)
print("Starting work...\n")
depth_first_search(initial_state)
ans.reverse()
for i in ans:
	print(i)