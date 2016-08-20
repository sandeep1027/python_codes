#feel free to edit my code and give new and better solution...
'''
Sample Input
(Plaintext Link)

3
2 qwopwasp
wdw
abco

5 eeeessaa
valentina
esta
jugando
con
marcia

5 ahi
valentina
esta
jugando
con
susamigas

Sample Output
(Plaintext Link)

1
2
1

 Explanation

In the first sample test case, there are n=2n=2 teams. The string showed by Marcia is s="qwopwasp"s="qwopwasp". There are two letters 'w' in ss, so two points are given to every girl who has chosen a letter 'w'.

Team 1 has three members. Two of them has chosen a letter 'w', and the other one has chosen a letter 'd'. The two girls get two points each, but the other girl has zero points because a letter 'd' doesn't occur in ss at all. The score of team 1 is 2+2=4 2+2=4.

Team 2 has four members. A girl who has chosen a letter 'a' gets one point, and so does a girl who has chosen a letter 'o'. The score of team 2 is 1+1=2 1+1=2.

So, in the first sample test case there is no tie and team 1 clearly wins.

Stack Limit for C++ is 8MB. You are allowed to increase it in your code, e.g. using setrlimit().

'''

#read file for data
with open('test1.txt') as f:
    content = f.readlines()

#split the code so that mystring and number of team get seprated ex. erdcsse 4
my_temp=content[0].split(" ")

#Number of teams in game
no_team=my_temp[0].rstrip()

#Main string of code
myString=my_temp[1].rstrip()

#loop to store teams in list(team)
team={}
for i in range(1,int(no_team)+1):
	team[i]=content[i].rstrip()

#stack is use to store number of charater count occur in mystring
stack={}
#find the number of charater count in mystraing and save it in list stack
for i in range(0,len(myString)):
	count=0
	word=myString[i]
	for s in range(0,len(myString)):
		if(word==myString[s]):
			count+=1
			stack[word]=count
			
#print stack			
# out put of stack must look like this  {'a': 1, 'o': 1, 'q': 1, 'p': 2, 's': 1, 'w': 2}
#now calculate which team get how many points
#create points list which store points for team
points={}
#temp variable to store points
temp_team=""
for i in range(1, len(team)+1):
	#set point to zero for every team
	point=0
	#temp variable which store team name
	temp_team=team[i]
	#loop through all charater for every team one my one
	for j in range(0,len(temp_team)):
		#check if that charater is present in stack or not if yes then give the letter point from stack
		if(temp_team[j] in stack):
			point+=stack[temp_team[j]]
			
	#print point
	#store the point in points list
	points[i]=point
	#print '\n'	
		
#print points

#now check which team is win the game by hige score
#assume first team has the max points and  win the match
max=points[1]
team_name=1
for i in range(1,len(points)):
	if(points[i]>max):
		max=points[i]
		team_name=i

#print which team really won the game
print "team "+str(team_name)+" win the game."	