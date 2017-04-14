from blackjack import Game

print('Welcome to blackjack')
print('Please enter your name:')
name = input()
print('How many other players should be in the game?')
while True:
    try:
        player_count = int(input())
        if player_count >= 0 and player_count < 6:
            break
        else:
            print('Please enter a valid number between 1 and 5:')
    except ValueError:
        print('Please enter a valid number between 1 and 5:')


game = Game(name, player_count)
game.play_game()
