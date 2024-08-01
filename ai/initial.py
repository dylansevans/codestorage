import game_initAI


#reset
#reward
#play_action -> direction
#game-iteration
#is-collision


# pygame setup
def main(genomes = [], config = [], neat=[]):
    game_handler = game_initAI.Game("easy", genomes, config, neat)

    while len(game_handler.birds) > 0:
        game_handler.play_step()