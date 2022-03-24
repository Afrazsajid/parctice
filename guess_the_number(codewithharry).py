import random
def game():
	
	n=random.randint(1,10)
	chance=5
	guess=int(input('\nenter your guess '))
	while(n!=guess):
		print('it is not correct guess')
		chance-=1
		print(f'you have {chance} chance\n')
		if(n>guess):
			print(f'{guess} is too low:  ')
			guess=int(input('enter guess again'))
			continue
		elif(n<guess):
		
			print(f'{guess} is too high  ')
			guess=int(input('enter guess again'))
			continue
	else:
		print(f'you have guess the number')
game()
y_n=input('enter yes or no ')
while y_n=='y':
	game()