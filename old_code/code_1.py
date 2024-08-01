import game_init

#reset
#reward
#play_action -> direction
#game-iteration
#is-collision


# pygame setup
running = True
dt = 0

game_handler = game_init.Game("easy")

while game_handler.running:
    game_handler.play_step()

    if(game_handler.check_collision()):
        print(f"Final Score: {game_handler.score}")
        game_handler = game_init.Game("easy")