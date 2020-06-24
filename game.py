# 추측 게임 만들기
import random # 랜덤 프로그램 만들기
number = random.randint(1,10) # 1에서 10사이의 숫자 생성후 number의 변수에 저장
player_name = input("Hello. what's your name?")
print('okay!' +player_name + 'I am Guessing a number between 1 and 10:')

while number_of_guesses <5 :
    guess = int(input())
    number_of_guesses +=1
    if guess <number :
        print('Your guess is too low')
    if guess > number :
        print('Your guess is too high')
    if guess == number :
        break  # 루프 종료
if guess == number :
    print('You guessed the number in' + str(number_of_guesses) + "tries!")
else :
    print('You did not guess the number, the number was ' + str(number))

    