def depth_first_search(capacity, initial, goal):
    dfs = Bottle(capacity,initial,goal)

    state = (dfs.initial[0], dfs.initial[1], dfs.initial[2]) 

    # to mark visited states
    memory = {}

    # store solution path
    ans = []
    
    a = int(dfs.initial[0])
    b = int(dfs.initial[1])
    c = int(dfs.initial[2])

    g1 = int(dfs.goal[0])
    g2 = int(dfs.goal[1])
    g3 = int(dfs.goal[2])

    x = int(dfs.capacity[0])
    y = int(dfs.capacity[1])
    z = int(dfs.capacity[2])
    
    if(a==g1 and b==g2 and c==g3):
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
            else:
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
    
    ans.reverse()
    for i in ans:
	    print(i)