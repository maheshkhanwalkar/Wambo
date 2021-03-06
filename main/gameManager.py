from humanPlayer import HumanPlayer
from AI import AI
from node import Node
from gamePiece import GamePiece

RED = (202, 52, 51)
GREEN = (67, 124, 23)
GREY = (200, 200, 200)
WHITE = 255
BLACK = 0


class GameManager:
    def __init__(self, game_size, game_state, node_percent, center_percent, pieces_per_player, piece_size_percent,
                 player_one_int, player_two_int):
        GamePiece.num_on_green_bench = 0
        GamePiece.num_on_red_bench = 0
        self.selected_piece = ''
        self.game_state = game_state
        self.nodes = []
        self.players = []

        red_str = "RED, pieces_per_player, node_percent * piece_size_percent, game_size, self.nodes"
        green_str = "GREEN, pieces_per_player, node_percent * piece_size_percent, game_size, self.nodes"

        # Handle AI parameters -- if they exist
        if isinstance(player_one_int, list):
            self.players.append(eval(player_one_int[0] + "(" + red_str + ", " + player_one_int[1] +
                                     ", " + player_one_int[2] + ")"))
        else:
            self.players.append(eval(player_one_int + "(" + red_str + ")"))

        if isinstance(player_two_int, list):
            self.players.append(eval(player_two_int[0] + "(" + green_str + ", " + player_two_int[1] +
                                     ", " + player_two_int[2] + ")"))
        else:
            self.players.append(eval(player_two_int + "(" + green_str + ")"))

        for i in range(24):
            self.nodes.append(Node(game_size * node_percent, game_size * node_percent * center_percent, i))

        s1 = (game_size * .1) + (game_size * .05)
        s2 = (game_size * .3) + (game_size * .025)
        s3 = (game_size * .5)
        s4 = (game_size * .7) - (game_size * .025)
        s5 = (game_size * .9) - (game_size * .05)

        self.nodes[0].set([self.nodes[1], self.nodes[2]], s3, s1, GREEN)
        self.nodes[1].set([self.nodes[0], self.nodes[3]], s2, s1)
        self.nodes[2].set([self.nodes[0], self.nodes[4]], s4, s1)
        self.nodes[3].set([self.nodes[1], self.nodes[7], self.nodes[9]], s1, s1)
        self.nodes[4].set([self.nodes[2], self.nodes[6], self.nodes[8]], s5, s1)
        self.nodes[5].set([self.nodes[6], self.nodes[7]], s3, s2)
        self.nodes[6].set([self.nodes[4], self.nodes[5], self.nodes[10]], s4, s2)
        self.nodes[7].set([self.nodes[3], self.nodes[5], self.nodes[11]], s2, s2)
        self.nodes[8].set([self.nodes[4], self.nodes[12]], s5, s2)
        self.nodes[9].set([self.nodes[3], self.nodes[13]], s1, s2)
        self.nodes[10].set([self.nodes[6], self.nodes[12], self.nodes[14]], s4, s3)
        self.nodes[11].set([self.nodes[7], self.nodes[13], self.nodes[15]], s2, s3)
        self.nodes[12].set([self.nodes[8], self.nodes[10], self.nodes[16]], s5, s3)
        self.nodes[13].set([self.nodes[9], self.nodes[11], self.nodes[17]], s1, s3)
        self.nodes[14].set([self.nodes[10], self.nodes[18], self.nodes[20]], s4, s4)
        self.nodes[15].set([self.nodes[11], self.nodes[18], self.nodes[19]], s2, s4)
        self.nodes[16].set([self.nodes[12], self.nodes[20]], s5, s4)
        self.nodes[17].set([self.nodes[13], self.nodes[19]], s1, s4)
        self.nodes[18].set([self.nodes[14], self.nodes[15]], s3, s4)
        self.nodes[19].set([self.nodes[15], self.nodes[17], self.nodes[21]], s1, s5)
        self.nodes[20].set([self.nodes[14], self.nodes[16], self.nodes[22]], s5, s5)
        self.nodes[21].set([self.nodes[19], self.nodes[23]], s2, s5)
        self.nodes[22].set([self.nodes[20], self.nodes[23]], s4, s5)
        self.nodes[23].set([self.nodes[21], self.nodes[22]], s3, s5, RED)
