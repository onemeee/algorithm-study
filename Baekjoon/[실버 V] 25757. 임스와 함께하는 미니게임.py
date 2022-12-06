import sys
input = sys.stdin.readline

def ready_player(game_type):
    if game_type == 'Y':
        ready = 1
    elif game_type == 'F':
        ready = 2
    elif game_type == 'O':
        ready = 3
    return ready

def game():
    n, game_type = input().rstrip().split()
    gamed_player = {}
    ready = ready_player(game_type)
    play = 0
    for _ in range(int(n)):
        player = input()
        if player in gamed_player:
            continue
        else:
            ready -= 1
            gamed_player[player] = True
            if not ready:
                play += 1
                ready = ready_player(game_type)
    print(play)

game()