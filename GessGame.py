# Author: Paldin Bet Eivaz
# Date Last Modified: 06/04/2020
# Description: An implementation of the abstract board game Gess.


class Piece:
    """
    The Piece class represents a Gess game piece.

    The Piece class is responsible for defining all attributes related to a Gess game piece such as
    the Piece's center, its 3x3 footprint, whether the specified Piece is a ring, and what moves
    are legal for a specific Piece.

    The Piece class communicates with the GessBoard class in order to get the row and column indexes
    of a Piece's center, to get a Piece's footprint, and to get the legal moves available for a Piece.

    Piece objects are instantiated within the GessGame class in order to make moves.
    """

    def __init__(self, ctr_label):
        """
        Creates a Piece object and initializes the Piece's center, footprint, moves, and ring attributes.

        :param str ctr_label: the map label of the Piece's center (for ex., 'b3' or 'c10')
        """

        self._ctr_label = ctr_label
        self._ctr_coord = tuple()
        self._footprint = []
        self._moves = []
        self._is_ring = None

    def get_ctr_label(self):
        """"
        Returns the Piece's center label.

        :return str self._ctr_label: the Piece object's center label
        """

        return self._ctr_label

    def get_ctr_coord(self, board):
        """
        Gets the row and column indexes of the Piece's center from the board and returns them in a tuple.

        :param board: the GessBoard object
        :return tuple self._ctr_coord: the tuple containing the Piece's center row and column indexes
        """

        # get column index from center label
        ctr_col = board.get_col_idx(self._ctr_label[0])

        # get row index from center label
        ctr_row = board.get_row_idx(self._ctr_label[1:])

        self._ctr_coord = ctr_row, ctr_col

        return self._ctr_coord

    def get_footprint(self, board, ctr_coord):
        """
        Gets the Piece's 3x3 footprint from the Board's map and returns it as a list.

        :param board: the GessBoard object
        :param tuple ctr_coord: the tuple containing the Piece's center row and column indexes
        :return list self._footprint: the Piece's 3x3 footprint
        """

        # get Piece's 3x3 footprint from the Board's map
        for i in range(ctr_coord[0] - 1, ctr_coord[0] + 2):
            for j in range(ctr_coord[1] - 1, ctr_coord[1] + 2):
                if board.get_map()[i][j] == '*':  # if footprint extends outside of map's boundaries
                    self._footprint.append('_')
                else:
                    self._footprint.append(board.get_map()[i][j])

        return self._footprint

    def is_ring(self, footprint):
        """
        Checks the Piece's footprint to determine if the Piece is a ring.

        :param list footprint: the Piece's 3x3 footprint
        :return bool self._is_ring: is True if the Piece is a ring, False otherwise
        """

        # check if footprint is 8 stones surrounding an empty center
        if footprint.count('B') == 8 or footprint.count('W') == 8 and footprint[4] == '_':
            self._is_ring = True
        else:
            self._is_ring = False

        return self._is_ring

    def add_move(self, row, col, board_map):
        """
        Creates a new footprint with center specified by the row and col parameters and uses it
        to determine if a move to that row and col is legal for the Piece. If legal, the move is
        added to the Piece's move list.

        Returns True if the new footprint has not overlapped with any stones and returns False if
        the new footprint has overlapped stones of either player or if the new footprint center
        is out of the map's bounds.

        :param int row: row index of new footprint center
        :param int col: column index of new footprint center
        :param list board_map: the list containing the board's map
        :return bool: True or False depending on if Piece can continue moving in that direction
        """

        # check if center is out of bounds
        if row == 19 or row == 0 or col == 19 or col == 0:

            return False

        # get new footprint
        new_footprint = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if board_map[i][j] == '*':  # if new footprint extends outside of map's boundaries
                    new_footprint.append('_')
                else:
                    new_footprint.append(board_map[i][j])

        # check if new footprint overlaps with stones of either player
        if 'B' in new_footprint or 'W' in new_footprint:
            # move is legal but can't continue moving in this direction, so return False
            self._moves.append((row, col))

            return False

        # check if new footprint does not contain stones of either player
        if 'B' not in new_footprint or 'W' not in new_footprint:
            # move is legal and can continue moving in this direction, so return True
            self._moves.append((row, col))

            return True

    def get_moves(self, footprint, ctr_coord, board, player):
        """
        Returns a list containing the map labels where the Piece's center is allowed to move to.

        :Algorithm:

        Given the Piece's footprint, row and column indexes of its center, and the board object,
        will first remove the Piece's stones from the Board's map. Then, from the Piece's footprint
        will determine how far the Piece is allowed to move and in which directions.

        Will next move the Piece's center in each allowed direction by the allowed distance and will
        add that new center coordinate to the Piece's move list if the move is found to be legal by
        the add_move method. Piece will continually move in each direction until it encounters stones
        of either Player, the center goes out of bounds, or the maximum move length is reached.

        After all potential moves are found, will check if any of those moves leave the Player without
        a ring, if yes then will remove those moves from the list of legal moves.

        :param list footprint: the Piece's 3x3 footprint
        :param tuple ctr_coord: the tuple containing the row and col indexes of the Piece's center
        :param board: the GessBoard object
        :param player: the Player object
        :return list self._moves: the list containing the legal moves for the Piece
        """

        # get Board's map
        board_map = board.get_map()

        # remove Piece's stones from Board
        for i in range(ctr_coord[0] - 1, ctr_coord[0] + 2):
            for j in range(ctr_coord[1] - 1, ctr_coord[1] + 2):
                if board_map[i][j] != '*':  # only remove stones
                    board_map[i][j] = '_'

        # get max distance Piece can move
        if footprint[4] != '_':
            move_len = len(board_map)  # can move any unobstructed distance
        else:
            move_len = 3  # can only move up to 3 squares

        # get legal moves in northwest direction
        if footprint[0] != '_':

            # initialize row and column indexes
            row = ctr_coord[0]
            col = ctr_coord[1]

            # move center a move_len distance in this direction
            for _ in range(move_len):

                # move center by 1 square in the northwest direction
                row -= 1
                col -= 1

                # check if can continue moving in this direction, if not break
                if not self.add_move(row, col, board_map):
                    break

        # same logic is repeated below for N, NE, W, E, SW, S, SE directions

        # get legal moves in north direction
        if footprint[1] != '_':

            # initialize row and column indexes
            row = ctr_coord[0]
            col = ctr_coord[1]

            # move center a move_len distance in this direction
            for _ in range(move_len):

                # move center by 1 square in the north direction
                row -= 1

                # check if can continue moving in this direction, if not break
                if not self.add_move(row, col, board_map):
                    break

        # get legal moves in northeast direction
        if footprint[2] != '_':

            # initialize row and column indexes
            row = ctr_coord[0]
            col = ctr_coord[1]

            # move center a move_len distance in this direction
            for _ in range(move_len):

                # move center by 1 square in the northeast direction
                row -= 1
                col += 1

                # check if can continue moving in this direction, if not break
                if not self.add_move(row, col, board_map):
                    break

        # get legal moves in west direction
        if footprint[3] != '_':

            # initialize row and column indexes
            row = ctr_coord[0]
            col = ctr_coord[1]

            # move center a move_len distance in this direction
            for _ in range(move_len):

                # move center by 1 square in the west direction
                col -= 1

                # check if can continue moving in this direction, if not break
                if not self.add_move(row, col, board_map):
                    break

        # get legal moves in east direction
        if footprint[5] != '_':

            # initialize row and column indexes
            row = ctr_coord[0]
            col = ctr_coord[1]

            # move center a move_len distance in this direction
            for _ in range(move_len):

                # move center by 1 square in the east direction
                col += 1

                # check if can continue moving in this direction, if not break
                if not self.add_move(row, col, board_map):
                    break

        # get legal moves in southwest direction
        if footprint[6] != '_':

            # initialize row and column indexes
            row = ctr_coord[0]
            col = ctr_coord[1]

            # move center a move_len distance in this direction
            for _ in range(move_len):

                # move center by 1 square in the southwest direction
                row += 1
                col -= 1

                # check if can continue moving in this direction, if not break
                if not self.add_move(row, col, board_map):
                    break

        # get legal moves in south direction
        if footprint[7] != '_':

            # initialize row and column indexes
            row = ctr_coord[0]
            col = ctr_coord[1]

            # move center a move_len distance in this direction
            for _ in range(move_len):

                # move center by 1 square in the south direction
                row += 1

                # check if can continue moving in this direction, if not break
                if not self.add_move(row, col, board_map):
                    break

        # get legal moves in southeast direction
        if footprint[8] != '_':

            # initialize row and column indexes
            row = ctr_coord[0]
            col = ctr_coord[1]

            # move center a move_len distance in this direction
            for _ in range(move_len):

                # move center by 1 square in the southeast direction
                row += 1
                col += 1

                # check if can continue moving in this direction, if not break
                if not self.add_move(row, col, board_map):
                    break

        # convert moves from coordinates to map labels
        self._moves = board.get_label_from_coord(self._moves)

        # remove any moves which leave player without a ring
        if player.get_num_rings() == 1 and board.get_label_from_coord([ctr_coord])[0] != player.get_rings()[0]:

            # get ring's footprint
            ring = player.get_rings()[0]
            ring_ftprint = set(board.get_footprint_labels(ring))

            # check if any move footprints overlap with own ring footprint
            for move in self._moves:
                move_ftprint = set(board.get_footprint_labels(move))
                if move_ftprint & ring_ftprint:
                    self._moves.remove(move)

        return self._moves


class Player:
    """
    The Player class represents a Gess player.

    The Player class is responsible for defining all attributes related to a Gess player such as the
    Player's ring collection and ring count. The class also provides several methods to update
    information related to a Player's rings. These include updating the location of a Player's ring,
    adding/removing a ring from a Player's ring collection, and checking if a Player has any rings remaining.

    In the GessGame class, composition is used to instantiate the player attributes (self._black and self._white)
    as Player objects, making all the Player methods available to the GessGame class. This allows GessGame to
    update each Player's ring information after each move is made and enables GessGame to determine the winner
    of the game by checking each Player's ring count.
    """

    def __init__(self, ring_ctr):
        """
        Creates a Player object and initializes Player's ring collection and ring count.

        :param str ring_ctr: the map label of the center of a Player's ring (for ex., 'l3')
        """

        self._rings = [ring_ctr]
        self._num_rings = 1

    def get_rings(self):
        """
        Returns the Player's ring collection.

        :return list self._rings: contains the map labels of the centers of the Player's rings
        """

        return self._rings

    def get_num_rings(self):
        """
        Returns the Player's ring count.

        :return int self._num_rings: the number of rings the Player has remaining
        """

        return self._num_rings

    def move_ring(self, move_from, move_to):
        """
        When a Player's ring is moved, this method updates the
        Player's ring collection with the ring's new location.

        :param str move_from: the original map label of the ring's center
        :param str move_to: the new map label of the ring's center
        """

        # update the ring's location
        if move_from in self._rings:
            self._rings.remove(move_from)
            self._rings.append(move_to)

    def add_ring(self, ring_ctr):
        """
        Adds a specified ring to Player's ring collection.

        :param str ring_ctr: the map label of the ring's center to be added
        """

        # add the ring and increment Player's ring count
        self._rings.append(ring_ctr)
        self._num_rings += 1

    def remove_ring(self, ring_ctr):
        """
        Removes a specified ring from Player's ring collection.

        :param str ring_ctr: the map label of the ring's center to be removed
        """

        # remove the ring and decrement Player's ring count
        if ring_ctr in self._rings:
            self._rings.remove(ring_ctr)
        self._num_rings -= 1

    def has_no_rings(self):
        """
        Checks if the Player has no rings remaining.

        :return bool: returns True if Player's ring count is zero, returns False otherwise
        """

        # check if Player's ring count is zero
        return self._num_rings == 0


class GessBoard:
    """
    The GessBoard class represents a Gess playing board.

    The GessBoard class is responsible for defining all attributes related to a Gess board such as
    the map of the board (with positions of all the stones) and the row and column labels of the board.
    The class provides methods to convert between map labels and row and column indexes. The class
    also has a method to print the current state of the Board's map.

    In the GessGame class, composition is used to instantiate a board attribute (self._board) as a
    GessBoard object, making all the GessBoard methods available to the GessGame class. This enables
    the GessGame class to update the Board's map after a valid move is made.

    The GessBoard class is also used by the Piece class to get a Piece's legal moves and 3x3 footprint.
    """

    def __init__(self):
        """
        Creates a GessBoard object and initializes the Board's map and labels.
        """

        self._map = [
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
            ['*', '_', 'W', '_', 'W', '_', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '_', 'W', '_', 'W', '_', '*'],
            ['*', 'W', 'W', 'W', '_', 'W', '_', 'W', 'W', 'W', 'W', '_', 'W', '_', 'W', '_', 'W', 'W', 'W', '*'],
            ['*', '_', 'W', '_', 'W', '_', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '_', 'W', '_', 'W', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', 'W', '_', '_', 'W', '_', '_', 'W', '_', '_', 'W', '_', '_', 'W', '_', '_', 'W', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', 'B', '_', '_', 'B', '_', '_', 'B', '_', '_', 'B', '_', '_', 'B', '_', '_', 'B', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '*'],
            ['*', '_', 'B', '_', 'B', '_', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '_', 'B', '_', 'B', '_', '*'],
            ['*', 'B', 'B', 'B', '_', 'B', '_', 'B', 'B', 'B', 'B', '_', 'B', '_', 'B', '_', 'B', 'B', 'B', '*'],
            ['*', '_', 'B', '_', 'B', '_', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '_', 'B', '_', 'B', '_', '*'],
            ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]
        self._row_labels = [str(num) for num in range(20, 0, -1)]
        self._col_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
        self._map_bounds = ['b', 's', '2', '19']
        self._map_edges = ['a', 't', '1', '20']

    def get_map(self):
        """
        Returns the Board's map.

        :return list self._map: the Board object's map
        """

        return self._map

    def get_row_labels(self):
        """
        Returns the map's row labels.

        :return list self._row_labels: the map's row labels
        """

        return self._row_labels

    def get_col_labels(self):
        """
        Returns the map's column labels.

        :return list self._col_labels: the map's column labels
        """

        return self._col_labels

    def get_map_bounds(self):
        """
        Returns the map's boundary labels.

        :return list self._map_bounds: the map's boundary labels
        """

        return self._map_bounds

    def get_map_edges(self):
        """
        Returns the map's edge labels.

        :return list self._map_edges: the map's edge labels
        """

        return self._map_edges

    def get_row_idx(self, row_label):
        """
        Returns the map's row index corresponding to row_label.

        :param str row_label: one of the map's row labels
        :return int: the index corresponding to row_label
        """

        return self._row_labels.index(row_label)

    def get_col_idx(self, col_label):
        """
        Returns the map's column index corresponding to col_label.

        :param str col_label: one of the map's column labels
        :return int: the index corresponding to col_label
        """

        return self._col_labels.index(col_label)

    def get_label_from_coord(self, coord_li):
        """
        Returns a list of map labels corresponding to the row and column coordinates passed in coord_li.

        :param list coord_li: the list containing tuples with row and column indexes
        :return list label_li: the list containing the map labels
        """

        label_li = []

        # get the map labels for each of the coordinates in coord_li and add them to a list
        for coord in coord_li:
            row_label = str(self._row_labels[coord[0]])
            col_label = str(self._col_labels[coord[1]])
            map_label = col_label + row_label
            label_li.append(map_label)

        return label_li

    def get_footprint_labels(self, ctr_label):
        """
        Returns the map labels of a Piece's 3x3 footprint with specified center label.

        :param str ctr_label: the map label of the Piece's center
        :return list: the list containing the map labels of the Piece's 3x3 footprint
        """

        # get row and column indexes of center
        ctr_col = self.get_col_idx(ctr_label[0])
        ctr_row = self.get_row_idx(ctr_label[1:])

        # get the row and column indexes of each square in the Piece's footprint and add them to a list as a tuple
        ftprint_coords = []
        for i in range(ctr_row - 1, ctr_row + 2):
            for j in range(ctr_col - 1, ctr_col + 2):
                ftprint_coords.append((i, j))

        return self.get_label_from_coord(ftprint_coords)

    def print_map(self):
        """
        Prints the Board's map.
        """

        # print the column labels
        print()
        print('  ', end='')
        for letter in self._col_labels:
            print(' ' + str(letter), end='')
        print()

        # iterate over the whole row
        for i in range(len(self._map)):

            # align row labels
            if int(self._row_labels[i]) < 10:
                print(' ', end='')

            # print the row labels
            print(str(self._row_labels[i]), end='')

            # print the board contents
            for square in self._map[i]:
                print(' ' + str(square), end='')
            print()


class GessGame:
    """
    The GessGame class represents the abstract board game Gess.

    The GessGame class is responsible for defining all attributes related to a Gess board game such as the
    Gess playing board, the Gess players, the current state of the Gess game, and the tracking of player turns.
    The class provides methods to get the GessBoard object, and to get and update information regarding
    the state of the game and which player's turn it is. The class also has a method which allows a player
    to move a Piece from one location on the board to another.

    Several attributes of the GessGame class are composed of other classes. The board attribute (self._board)
    is instantiated as a GessBoard object and the player attributes (self._white, self._black) are instantiated
    as Player objects. Also, in the make_move method Piece objects are instantiated. These classes work together
    to emulate a turn-based game of Gess.

    Most of the game logic takes place within the make_move method. There, moves are first checked to ensure
    they are legal. If the move is legal, the move is made, which then triggers any necessary updates to
    player ring, board map, and game state information.
    """

    def __init__(self):
        """
        Creates a GessGame object and initializes the board, players, game state, and current player's turn
        """

        self._board = GessBoard()
        self._white = Player('l18')
        self._black = Player('l3')
        self._game_state = 'UNFINISHED'
        self._curr_player = 'BLACK'

    def get_board(self):
        """
        Returns the GessBoard object.

        :return self._board: the GessBoard object
        """

        return self._board

    def get_game_state(self):
        """
        Returns state of the Gess game.

        :return str self._game_state: the state of the Gess game, can be 'UNFINISHED', 'BLACK_WON', 'WHITE_WON'
        """

        return self._game_state

    def get_player(self):
        """
        Returns the Player object for the current player.

        :return: the Player object, can be either the black or white player
        """

        if self._curr_player == 'BLACK':

            return self._black

        else:

            return self._white

    def set_curr_player(self):
        """
        Sets which Player's turn it is.
        """

        if self._curr_player == 'BLACK':
            self._curr_player = 'WHITE'
        else:
            self._curr_player = 'BLACK'

    def resign_game(self):
        """
        Resigns game for current player.
        If currently black Player's turn, then white Player wins and vice versa.
        """

        if self._curr_player == 'BLACK':
            self._game_state = 'WHITE_WON'
        else:
            self._game_state = 'BLACK_WON'

    def make_move(self, move_from, move_to):
        """
        Moves a Piece's center from map label specified in move_from to map label specified in move_to.

        Returns False if the indicated move is not legal for the current player
        or if the game has already been won.

        Otherwise, the indicated move is made and the Board's map, Player's ring information,
        the Game's state, and the Player's turn are updated, and True is returned.

        :param str move_from: the map label of the center of the Piece being moved
        :param str move_to: the map label of the desired new location of the Piece's center
        :return bool: Returns True if move is successfully made, returns False otherwise
        """

        # ensure letters are lowercase
        move_from = move_from.lower()
        move_to = move_to.lower()

        # check user input is valid
        if move_from[0] not in self._board.get_col_labels() or move_from[1:] not in self._board.get_row_labels() or \
                move_to[0] not in self._board.get_col_labels() or move_to[1:] not in self._board.get_row_labels():

            return False

        # check game not already won
        if self._game_state != 'UNFINISHED':

            return False

        # get the bounds and edges of the board
        bounds = self._board.get_map_bounds()
        edges = self._board.get_map_edges()

        # check if selected center is out of bounds
        if move_from[0] in edges or move_from[1:] in edges or move_to[0] in edges or move_to[1:] in edges:

            return False

        # get the Piece, the Player, and the Board's map
        piece = Piece(move_from)
        player = self.get_player()
        board_map = self._board.get_map()

        # get the Piece's center coordinates and footprint
        ctr_coord = piece.get_ctr_coord(self._board)
        footprint = piece.get_footprint(self._board, ctr_coord)

        # check if footprint has stones belonging to the wrong player
        if self._curr_player == 'BLACK' and 'W' in footprint:

            return False

        elif self._curr_player == 'WHITE' and 'B' in footprint:

            return False

        # check if Piece's footprint is only 1 stone in center
        if footprint.count('_') == 8 and footprint[4] != '_':

            return False

        # check if Piece has no stones in footprint
        if footprint.count('_') == 9:

            return False

        # check that Player does not move ring stones which would break Player's last ring
        if player.get_num_rings() == 1 and set(self._board.get_footprint_labels(player.get_rings()[0])) \
                & set(self._board.get_footprint_labels(move_from)) and move_from != player.get_rings()[0]:

            return False

        # check that Player does not break last ring by losing stones which go out of bounds
        if player.get_num_rings() == 1 and move_from == player.get_rings()[0] and \
                (move_to[0] in bounds or move_to[1:] in bounds):

            return False

        # get all moves which are legal for the Piece
        legal_moves = piece.get_moves(footprint, ctr_coord, self._board, player)

        # check if desired move is legal
        if move_to not in legal_moves:

            # move not legal, keep Piece at same position and return False
            k = 0
            for i in range(ctr_coord[0] - 1, ctr_coord[0] + 2):
                for j in range(ctr_coord[1] - 1, ctr_coord[1] + 2):
                    if self._board.get_map()[i][j] != '*':  # don't write footprint to outer bounds
                        self._board.get_map()[i][j] = footprint[k]
                    k += 1

            return False

        # make the desired move
        else:

            # get row and column indexes of Piece's new center
            new_col = self._board.get_col_idx(move_to[0])
            new_row = self._board.get_row_idx(move_to[1:])

            # move Piece to new center
            k = 0
            for i in range(new_row - 1, new_row + 2):
                for j in range(new_col - 1, new_col + 2):
                    if self._board.get_map()[i][j] != '*':  # remove any stones which are out of bounds
                        self._board.get_map()[i][j] = footprint[k]
                    k += 1

            # check if Player moved a ring, if yes update ring's location
            if move_from in player.get_rings():
                player.move_ring(move_from, move_to)

            # check the Board's map for an empty square
            for i in range(len(board_map)):
                for j in range(len(board_map)):
                    if board_map[i][j] == '_':

                        # get the 3x3 footprint around that empty square
                        ctr_label = self._board.get_label_from_coord([(i, j)])[0]
                        piece = Piece(ctr_label)
                        footprint = piece.get_footprint(self._board, (i, j))

                        # check if that 3x3 footprint is a new ring for either Player, if yes add ring
                        if piece.is_ring(footprint) and 'B' in footprint and ctr_label not in self._black.get_rings():
                            self._black.add_ring(ctr_label)
                        elif piece.is_ring(footprint) and 'W' in footprint and ctr_label not in self._white.get_rings():
                            self._white.add_ring(ctr_label)

                        # check if any of either Player's rings were broken, if yes remove ring
                        if ctr_label in self._black.get_rings() and not piece.is_ring(footprint):
                            self._black.remove_ring(ctr_label)
                        elif ctr_label in self._white.get_rings() and not piece.is_ring(footprint):
                            self._white.remove_ring(ctr_label)

            # check if either Player has no remaining rings, if yes update game state
            if self._black.has_no_rings():
                self._game_state = 'WHITE_WON'
            elif self._white.has_no_rings():
                self._game_state = 'BLACK_WON'

            # set next Player's turn
            self.set_curr_player()

            return True
