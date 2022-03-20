import random
score1=0
score2=0
computer=0
sen='welcome to the guessing game'
print(sen.center(210,'-'))
(x,y)=(int(input('enter range first number ')),int(input('enter range last number ')))
while(score1<9 and score2<9):
	print('lets play game again')
	print('your score is',score1)
	print('computer is',score2)
	computer=random.randint(x,y)
	print(computer)
	tell=input('is it correct guess "y" for yes and "n" for no  ')
	if(tell!='y'):
	    print('you win')
	    score1+=1
	    print('is it too high(h) or to low(l)')
	    tell1=input()
	    if(tell1=='h'):
	        y=computer-1
	    else:
	    	x=computer+1
	else:
	    x=int(input('enter range again '))
	    y=int(input('enter range again '))
	    score2+=1
	    print('computer win')
	    print('\nstart again')
if(score1>score2):
	print('\n\nfinallu you win')
	print('your score is',score1)
else:
	print('finally computer win')
	print('computer score is')
	
 