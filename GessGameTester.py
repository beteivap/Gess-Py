# Author: Paldin Bet Eivaz
# Date Last Modified: 06/04/2020
# Description: Unit tester for GessGame.

import unittest
from GessGame import Piece, Player, GessBoard, GessGame


class GessGameTester(unittest.TestCase):
    """Unit tester for GessGame"""

    def test_white_wins(self):
        """Tests a simple scenario where White wins"""

        game = GessGame()
        game.make_move('l3', 'l6')
        game.make_move('l15', 'l12')
        game.make_move('l6', 'l9')
        game.make_move('l12', 'l11')
        self.assertEqual(game.get_game_state(), 'WHITE_WON')

    def test_black_wins(self):
        """Tests a simple scenario where Black wins"""

        game = GessGame()
        game.make_move('l6', 'l9')
        game.make_move('l18', 'l15')
        game.make_move('l9', 'l12')
        game.make_move('r15', 'r14')
        game.make_move('l12', 'l13')
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

    def test_longer_game(self):
        """Tests a longer game with more moves"""

        game = GessGame()
        game.make_move('i6', 'i9')
        game.make_move('c15', 'c12')
        game.make_move('i3', 'i7')
        game.make_move('p18', 'p16')
        game.make_move('i7', 'k9')
        game.make_move('p15', 'l11')
        game.make_move('l8', 'l9')
        game.make_move('l12', 'l11')
        game.make_move('j9', 'f13')
        game.make_move('l11', 'l10')
        game.make_move('l7', 'l8')
        game.make_move('m11', 'm10')
        game.make_move('p6', 'n8')
        game.make_move('e18', 'e15')
        game.make_move('g12', 'f13')
        game.make_move('j14', 'g14')
        game.make_move('f3', 'l9')
        game.make_move('i18', 'i3')
        game.make_move('l3', 'k3')
        game.make_move('h3', 'i3')
        self.assertTrue(game.get_game_state(), 'WHITE_WON')

    def test_longer_game_2(self):
        """Tests a longer game with more moves"""

        game = GessGame()
        game.make_move('c6', 'c8')
        game.make_move('r15', 'r12')
        game.make_move('i6', 'i9')
        game.make_move('r18', 'r14')
        game.make_move('i9', 'i11')
        game.make_move('i15', 'i13')
        game.make_move('i3', 'i11')
        game.make_move('f15', 'f14')
        game.make_move('i11', 'q11')
        game.make_move('r14', 'r13')
        game.make_move('f3', 'j7')
        game.make_move('c18', 'c15')
        game.make_move('j7', 'e12')
        game.make_move('c15', 'b15')
        game.make_move('e12', 'c14')
        game.make_move('r13', 'r12')
        game.make_move('p10', 'q10')
        game.make_move('r13', 's12')
        game.make_move('q9', 'r10')
        game.make_move('s13', 's12')
        game.make_move('c14', 'e16')
        game.make_move('h18', 'h3')
        game.make_move('l3', 'j3')
        game.make_move('l15', 'l12')
        game.make_move('e16', 'b19')
        game.make_move('o18', 's14')
        game.make_move('p11', 'p13')
        game.make_move('r14', 'r13')
        game.make_move('j3', 'i3')
        game.make_move('l18', 'l15')
        game.make_move('i3', 'h3')
        game.make_move('l15', 'i12')
        game.make_move('h3', 'h6')
        game.make_move('i12', 'i9')
        game.make_move('h6', 'i7')
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

    def test_longer_game_3(self):
        """Tests a longer game with more moves"""

        game = GessGame()
        game.make_move('f6', 'f8')
        game.make_move('r15', 'r12')
        game.make_move('k6', 'm8')
        game.make_move('s12', 'q10')
        game.make_move('n6', 'p8')
        game.make_move('r18', 'r10')
        game.make_move('r6', 'r8')
        game.make_move('r11', 'r10')
        game.make_move('p3', 'p4')
        game.make_move('r10', 'r5')
        game.make_move('s2', 'r3')
        game.make_move('r6', 'r5')
        game.make_move('p3', 'q3')
        game.make_move('o15', 'o12')
        game.make_move('f8', 'f10')
        game.make_move('f15', 'f12')
        game.make_move('m8', 'o10')
        game.make_move('k14', 'n14')
        game.make_move('o10', 'q12')
        game.make_move('n14', 'q14')
        game.make_move('h6', 'k9')
        self.assertFalse(game.make_move('l18', 'l19'))  # White tries to destroy own ring going out of bounds
        game.make_move('h14', 'k14')
        game.make_move('k10', 'm10')
        game.make_move('s15', 'r14')
        game.make_move('m9', 'p12')
        game.make_move('o18', 's14')
        self.assertFalse(game.make_move('q12', 'q13'))  # Black tries to move Piece with white stones
        game.make_move('p4', 'p9')
        game.make_move('s14', 'r13')
        game.make_move('p9', 'p11')
        game.make_move('l18', 'm18')
        game.make_move('c6', 'c8')
        self.assertFalse(game.make_move('m18', 'n16'))  # not a valid move for White's ring
        game.make_move('m18', 'm17')
        game.make_move('b8', 'e11')
        game.make_move('m14', 'j14')
        game.make_move('s2', 'p5')
        game.make_move('j15', 'g12')
        game.make_move('q11', 'o11')
        game.make_move('r14', 'o14')
        game.make_move('m12', 'n12')
        self.assertFalse(game.make_move('n15', 'n14'))  # White tries to destroy own ring by moving its stones
        self.assertFalse(game.make_move('m17', 'i14'))  # White tries to make an illegal move for ring
        game.make_move('m17', 'k15')
        game.make_move('o5', 'o7')
        game.make_move('n15', 'n13')
        game.make_move('o10', 'o11')
        game.make_move('k15', 'h15')
        game.make_move('o11', 'o18')
        game.make_move('i18', 'n18')
        game.make_move('o7', 'o9')
        game.make_move('n18', 'n11')
        game.make_move('o7', 'm9')
        game.make_move('n11', 'm11')
        game.make_move('i3', 'i13')
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

    def test_longer_game_4(self):
        """Tests a longer game with more moves"""

        game = GessGame()
        game.make_move('b6', 'e9')
        game.make_move('o15', 'o12')
        game.make_move('l3', 'k3')
        game.make_move('i18', 'i17')
        game.make_move('c3', 'c13')
        game.make_move('l18', 'm17')
        game.make_move('s6', 'p9')
        game.make_move('m17', 'm16')
        game.make_move('n9', 'o10')
        game.make_move('g15', 'e13')
        game.make_move('b11', 'c12')
        game.make_move('g15', 'e13')
        game.make_move('f9', 'f12')
        game.make_move('c18', 'c15')
        game.make_move('f3', 'b7')
        game.make_move('c15', 'h15')
        game.make_move('f12', 'f14')
        game.make_move('i15', 'g15')
        game.make_move('b7', 'j15')
        game.make_move('m16', 'l16')
        game.make_move('h3', 'h6')
        game.make_move('l16', 'k15')
        game.make_move('h6', 'h14')
        game.make_move('k15', 'j15')
        game.make_move('k3', 'j4')
        game.make_move('r18', 'r15')
        game.make_move('j4', 'g7')
        game.make_move('j15', 'i14')
        game.make_move('g7', 'd10')
        game.make_move('r15', 'r5')
        game.make_move('o3', 'l6')
        game.make_move('o18', 's14')
        game.make_move('d10', 'd11')
        game.make_move('i14', 'i11')
        game.make_move('l6', 'i9')
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

    def test_longer_game_5(self):
        """Tests a longer game with more moves"""

        game = GessGame()
        game.make_move('b6', 'e9')
        game.make_move('m15', 'k13')
        game.make_move('e6', 'h9')
        game.make_move('j13', 'j11')
        game.make_move('c3', 'c9')
        game.make_move('j13', 'g10')
        game.make_move('c9', 'e9')
        game.make_move('i11', 'l8')
        game.make_move('l3', 'l6')
        game.make_move('o15', 'o12')
        game.make_move('s6', 'q8')
        game.make_move('n12', 'p10')
        game.make_move('r3', 'r8')
        game.make_move('i18', 'i8')
        game.make_move('l6', 'l3')
        game.make_move('i8', 'l5')
        self.assertEqual(game.get_game_state(), 'WHITE_WON')

    def test_longer_game_6(self):
        """Tests a longer game with more moves"""

        game = GessGame()
        game.make_move('c6', 'c9')
        game.make_move('s15', 'p12')
        game.make_move('b9', 'c10')
        game.make_move('b15', 'e12')
        game.make_move('c3', 'c16')
        game.make_move('b19', 'c18')
        game.make_move('c15', 'b16')
        game.make_move('d19', 'd18')
        self.assertFalse(game.make_move('a16', 'c18'))  # selected center out of bounds

    def test_longer_game_7(self):
        """Tests a longer game with more moves"""

        game = GessGame()
        game.make_move('r3', 'r6')
        game.make_move('o15', 'o12')
        game.make_move('r6', 'r8')
        game.make_move('n12', 'q9')
        game.make_move('r6', 'r7')
        game.make_move('b15', 'e12')
        game.make_move('s7', 'p10')
        game.make_move('k15', 'n12')
        game.make_move('o3', 'r6')
        game.make_move('p18', 'p15')
        game.make_move('c3', 'c4')
        game.make_move('p15', 'p12')
        game.make_move('n7', 'o7')
        game.make_move('s18', 'p18')  # creates 2 side-by-side rings
        game.make_move('q6', 'n9')
        white_rings = game.get_player().get_rings()
        self.assertEqual(game.get_player().get_num_rings(), 2)
        self.assertIn('n18', white_rings)
        self.assertIn('l18', white_rings)
        game.make_move('h15', 'k12')
        game.make_move('n9', 'n11')
        game.make_move('k10', 'l11')  # traps some of Black's stones
        game.make_move('n10', 'o11')
        game.make_move('l12', 'n12')  # fully traps Black's stone
        self.assertFalse(game.make_move('p11', 'p12'))
        self.assertFalse(game.make_move('q11', 'p12'))
        game.make_move('k6', 'n9')
        game.make_move('r13', 'q12')
        game.make_move('o9', 'o10')
        game.make_move('o13', 'o12')
        game.make_move('i3', 'i6')
        game.make_move('g18', 'g15')
        game.make_move('i6', 'l6')
        game.make_move('j18', 'j8')
        game.make_move('e6', 'h9')
        game.make_move('e12', 'h9')
        game.make_move('m6', 'm16')
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

    def test_longer_game_8(self):
        """Tests a longer game with more moves"""

        game = GessGame()
        game.make_move('p3', 'p5')
        game.make_move('p15', 'o14')
        game.make_move('p6', 'i13')
        game.make_move('i18', 'i15')
        game.make_move('s2', 's3')
        game.make_move('i15', 'i14')
        game.make_move('s2', 'r3')
        game.make_move('p18', 'p15')
        game.make_move('q3', 'q6')
        game.make_move('p15', 'p12')
        game.make_move('k7', 'n7')
        game.make_move('r18', 'r16')
        game.make_move('p6', 'm9')
        game.make_move('i14', 'i13')
        game.make_move('m9', 'o11')
        game.make_move('o14', 'n13')
        game.make_move('h6', 'k9')
        game.make_move('n13', 'l11')
        game.make_move('i3', 'i11')
        game.make_move('r15', 'r13')
        game.make_move('l3', 'k4')
        game.make_move('l18', 'k18')
        game.make_move('i11', 'i12')
        game.make_move('k18', 'i16')
        game.make_move('k4', 'h7')
        game.make_move('c18', 'c15')
        game.make_move('h7', 'j9')
        game.make_move('i16', 'l16')
        game.make_move('j9', 'm6')
        game.make_move('l16', 'l15')
        game.make_move('m6', 'm9')
        game.make_move('r13', 'r3')
        game.make_move('i12', 'i13')
        game.make_move('l15', 'k14')
        game.make_move('c3', 'c6')
        game.make_move('s3', 'p3')
        game.make_move('f3', 'j7')
        game.make_move('k14', 'j13')
        game.make_move('j7', 'd13')
        game.make_move('j13', 'i13')
        game.make_move('c6', 'c11')
        game.make_move('p3', 'o3')
        game.make_move('m9', 'm12')
        game.make_move('c16', 'c15')
        game.make_move('c11', 'c12')
        game.make_move('o18', 'l15')
        game.make_move('d11', 'e12')
        game.make_move('c15', 'd14')
        game.make_move('d11', 'd12')
        game.make_move('f15', 'f14')
        game.make_move('m12', 'k12')
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

    def test_get_moves(self):
        """Tests get_move algorithm to ensure returning correct legal moves"""

        # test a move across the length of the board
        game = GessGame()
        game.make_move('c3', 'c6')
        game.make_move('c18', 'c15')
        game.make_move('c6', 'c2')
        game.make_move('c15', 'e15')
        game.make_move('r6', 'r7')
        game.make_move('e15', 'h15')
        self.assertTrue(game.make_move('c2', 'c19'))

        # test moves for a rook Piece
        game = GessGame()
        board = game.get_board()
        game.make_move('c3', 'c6')
        game.make_move('r15', 'r14')
        game.make_move('c6', 'c10')
        game.make_move('r12', 'r13')
        game.make_move('c10', 'j10')
        game.make_move('r13', 'r14')
        player = game.get_player()
        piece = Piece('j10')
        ctr_coord = piece.get_ctr_coord(board)
        footprint = piece.get_footprint(board, ctr_coord)
        legal_moves = piece.get_moves(footprint, ctr_coord, board, player)
        print(legal_moves)

        # test moves for a bishop Piece
        game = GessGame()
        board = game.get_board()
        game.make_move('f3', 'e4')
        game.make_move('r15', 'r14')
        game.make_move('e4', 'g6')
        game.make_move('r12', 'r13')
        game.make_move('g6', 'h7')
        game.make_move('r13', 'r14')
        player = game.get_player()
        piece = Piece('h7')
        ctr_coord = piece.get_ctr_coord(board)
        footprint = piece.get_footprint(board, ctr_coord)
        legal_moves = piece.get_moves(footprint, ctr_coord, board, player)
        print(legal_moves)

        # test moves for a pawn in both diag and orthag directions
        game = GessGame()
        board = game.get_board()
        game.make_move('i6', 'i9')
        game.make_move('r13', 'r14')
        player = game.get_player()
        # piece = Piece('i9')
        # ctr_coord = piece.get_ctr_coord(board)
        # footprint = piece.get_footprint(board, ctr_coord)
        # legal_moves = piece.get_moves(footprint, ctr_coord, board, player)
        # print(legal_moves)
        piece = Piece('j9')
        ctr_coord = piece.get_ctr_coord(board)
        footprint = piece.get_footprint(board, ctr_coord)
        legal_moves = piece.get_moves(footprint, ctr_coord, board, player)
        print(legal_moves)

        # test moves for a ring
        game = GessGame()
        board = game.get_board()
        player = game.get_player()
        piece = Piece('l3')
        ctr_coord = piece.get_ctr_coord(board)
        footprint = piece.get_footprint(board, ctr_coord)
        legal_moves = piece.get_moves(footprint, ctr_coord, board, player)
        print(legal_moves)

        # test more moves for a ring
        game = GessGame()
        board = game.get_board()
        game.make_move('l3', 'l6')
        game.make_move('r15', 'r14')
        game.make_move('l6', 'l9')
        game.make_move('r12', 'r13')
        player = game.get_player()
        piece = Piece('l9')
        ctr_coord = piece.get_ctr_coord(board)
        footprint = piece.get_footprint(board, ctr_coord)
        legal_moves = piece.get_moves(footprint, ctr_coord, board, player)
        print(legal_moves)
        self.assertFalse(game.make_move('h6', 'h8'))  # move destroys own ring

    def test_valid_input(self):
        """Tests user input is valid"""

        game = GessGame()
        self.assertFalse(game.make_move('cc3', 'c5'))
        self.assertFalse(game.make_move('c3', 'cc5'))
        self.assertFalse(game.make_move('c33', 'c5'))
        self.assertFalse(game.make_move('c3', 'c55'))
        self.assertFalse(game.make_move('z3', 'c5'))
        self.assertFalse(game.make_move('c3', 'z3'))
        self.assertFalse(game.make_move('c21', 'c5'))
        self.assertFalse(game.make_move('c3', 'c21'))

    def test_no_ring(self):
        """Tests that move does not leave Player without a ring"""

        # destroy own last ring with own Piece which has no stones that are part of ring
        game = GessGame()
        self.assertFalse(game.make_move('o3', 'n4'))  # Black attempts to destroy own ring
        game.make_move('c3', 'c5')  # make it White's turn
        self.assertFalse(game.make_move('o18', 'n17'))  # White attempts to destroy own ring

        # destroy own last ring with own Piece which has stones that are part of ring
        game = GessGame()
        game.make_move('l3', 'l6')
        game.make_move('l18', 'l15')
        game.make_move('l6', 'j8')
        game.make_move('l15', 'n13')
        self.assertFalse(game.make_move('i9', 'j9'))  # Black tries to destroy own ring
        self.assertFalse(game.make_move('e7', 'h7'))  # Black tries to destroy own ring w/ diff stone
        game.make_move('e7', 'g7')
        self.assertFalse(game.make_move('n12', 'o12'))  # White tries to destroy own ring
        self.assertFalse(game.make_move('o18', 'l15'))  # White tries to destroy own ring w/ diff stone
        game.make_move('o18', 'm16')
        self.assertFalse(game.make_move('h8', 'h6'))  # Black tries to destroy own ring
        game.make_move('c6', 'c8')
        self.assertFalse(game.make_move('m14', 'n14'))  # White tries to destroy own ring
        game.make_move('n13', 'p11')
        game.make_move('o6', 'o9')  # Black destroys White's ring
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

        # test Player moves ring such that ring breaks because some of its stones go out of bounds
        game = GessGame()
        self.assertFalse(game.make_move('l3', 'l2'))  # Black tries to move own ring out of bounds
        game.make_move('l3', 'l6')
        game.make_move('l18', 'l15')
        game.make_move('l6', 'n8')
        game.make_move('l15', 'n13')
        game.make_move('n8', 'q8')
        game.make_move('n13', 'q13')
        self.assertFalse(game.make_move('q8', 's8'))  # Black tries to move own ring out of bounds
        self.assertTrue(game.make_move('q8', 'q9'))
        self.assertFalse(game.make_move('q13', 's13'))  # White tries to move own ring out of bounds
        self.assertFalse(game.make_move('r18', 'r15'))  # White tries to destroy own ring w/ diff stone

    def test_player_turn(self):
        """Tests that Player can't make a move out of turn"""

        game = GessGame()
        self.assertTrue(game.make_move('c6', 'c7'))  # Black makes a valid move
        self.assertFalse(game.make_move('c7', 'c8'))  # Black tries to make another move
        self.assertTrue(game.make_move('r15', 'r14'))  # White makes a valid move
        self.assertFalse(game.make_move('r14', 'r13'))  # White tries to make another move

    def test_illegal_moves(self):
        """Tests that Player can't make any moves which are illegal for a Piece"""

        game = GessGame()
        self.assertFalse(game.make_move('c3', 'c3'))  # Player not allowed to pass turn
        self.assertFalse(game.make_move('c3', 'c8'))  # Black's own stone at 'c7' blocks move
        self.assertFalse(game.make_move('c3', 'c1'))  # Piece's center can't go out of row bounds
        self.assertFalse(game.make_move('c3', 'a3'))  # Piece's center can't go out of col bounds
        self.assertFalse(game.make_move('c6', 'c10'))  # Piece tries to move too far

        game.make_move('c3', 'c6')
        game.make_move('r18', 'r15')
        self.assertFalse(game.make_move('c6', 'd7'))  # Piece moves in an invalid direction
        self.assertTrue(game.make_move('c6', 'c13'))  # checks Piece can move any unobstructed distance
        self.assertFalse(game.make_move('r15', 'r6'))  # checks Piece can only move an unobstructed distance
        self.assertFalse(game.make_move('o18', 'o17'))  # Piece moves in an invalid direction

    def test_not_a_piece(self):
        """Tests that Player can't select an invalid Piece"""

        game = GessGame()
        self.assertFalse(game.make_move('c1', 'c2'))  # selected center is out of row bounds
        self.assertFalse(game.make_move('t3', 's3'))  # selected center is out of column bounds
        game.make_move('c6', 'c7')
        self.assertFalse(game.make_move('c18', 'c20'))  # selected center is out of row bounds
        self.assertFalse(game.make_move('c18', 'a18'))  # selected center is out of column bounds

        game = GessGame()
        game.make_move('f6', 'f9')
        game.make_move('f15', 'f12')
        self.assertFalse(game.make_move('e11', 'f10'))  # Black tries to move a Piece containing White's stones
        game.make_move('c6', 'c8')
        self.assertFalse(game.make_move('g10', 'f11'))  # White tries to move a Piece containing Black's stones

        game = GessGame()
        self.assertFalse(game.make_move('c9', 'c10'))  # Black tries to move a Piece with no stones
        self.assertFalse(game.make_move('c7', 'c8'))  # Black tries to move a Piece with only 1 stone in center

    def test_stones_removed(self):
        """Tests that any stones which are out of bounds after move is made are removed"""

        game = GessGame()
        board = game.get_board()

        piece = Piece('c3')
        ctr_coord = piece.get_ctr_coord(board)
        footprint = piece.get_footprint(board, ctr_coord)
        self.assertEqual(footprint.count('B'), 5)
        self.assertTrue(game.make_move('c3', 'b3'))  # 1 stone goes out of bounds

        # check that same Piece has 1 less stone
        piece = Piece('c3')
        ctr_coord = piece.get_ctr_coord(board)
        footprint = piece.get_footprint(board, ctr_coord)
        self.assertEqual(footprint.count('B'), 4)

        # check that Piece can no longer move in the direction stone was removed from
        game.make_move('r18', 'r17')
        game.make_move('b3', 'c3')
        game.make_move('r17', 'r16')
        self.assertFalse(game.make_move('c3', 'b3'))

    def test_resign_game(self):
        """Tests that Player can resign"""

        game = GessGame()
        game.make_move('c6', 'c7')
        game.make_move('r15', 'r14')
        game.resign_game()  # Black resigns
        self.assertEqual(game.get_game_state(), 'WHITE_WON')
        self.assertFalse(game.make_move('c7', 'c8'))  # checks that no moves can be made if Game already won

        game = GessGame()
        game.make_move('c6', 'c7')
        game.make_move('r15', 'r14')
        game.make_move('c7', 'c8')
        game.resign_game()  # White resigns
        self.assertEqual(game.get_game_state(), 'BLACK_WON')
        self.assertFalse(game.make_move('r14', 'r13'))  # checks that no moves can be made if Game already won

    def test_mult_rings(self):
        """Tests multiple ring functionality"""

        game = GessGame()
        game.make_move('g3', 'g4')
        game.make_move('g18', 'g17')
        game.make_move('d3', 'e4')
        game.make_move('d18', 'e17')
        game.make_move('g4', 'f5')
        game.make_move('g17', 'f16')
        game.make_move('f5', 'f4')
        game.make_move('f16', 'f17')
        game.make_move('c4', 'd4')  # new ring created for Black at 'f4'
        game.make_move('c17', 'd17')  # new ring created for White at 'f17'

        self.assertEqual(game.get_player().get_num_rings(), 2)  # check that Black has two rings
        black_rings = game.get_player().get_rings()
        self.assertIn('l3', black_rings)  # check Black's ring locations are correct
        self.assertIn('f4', black_rings)
        # self.assertTrue(game.make_move('f5', 'g5'))  # Black destroys ring with own stones
        # self.assertTrue(game.make_move('f4', 'f2'))  # Black destroys own ring by going out of bounds
        # self.assertTrue(game.make_move('i3', 'j3'))  # moves destroys Black's ring but replaces in same move
        self.assertTrue(game.make_move('o3', 'n4'))  # Black destroys own ring at 'l3'

        self.assertEqual(game.get_player().get_num_rings(), 2)  # check that White has two rings
        white_rings = game.get_player().get_rings()
        self.assertIn('l18', white_rings)  # check White's ring locations are correct
        self.assertIn('f17', white_rings)
        game.make_move('o18', 'n17')  # White destroys own ring at 'l18'

        self.assertEqual(game.get_player().get_num_rings(), 1)  # check that Black has one ring
        black_rings = game.get_player().get_rings()
        self.assertNotIn('l3', black_rings)  # check destroyed ring removed from Black's rings
        game.make_move('f4', 'f6')  # Black makes a valid move

        self.assertEqual(game.get_player().get_num_rings(), 1)  # check that White has one ring
        white_rings = game.get_player().get_rings()
        self.assertNotIn('l18', white_rings)  # check destroyed ring removed from White's rings
        game.make_move('f17', 'f15')

        # check that Black's new ring's movement is being tracked
        black_rings = game.get_player().get_rings()
        self.assertIn('f6', black_rings)
        game.make_move('f6', 'f9')

        # check that White's new ring's movement is being tracked
        white_rings = game.get_player().get_rings()
        self.assertIn('f15', white_rings)
        game.make_move('f15', 'f12')

        game.make_move('f9', 'f10')  # Black's last ring destroys White's last ring
        self.assertEqual(game.get_game_state(), 'BLACK_WON')

    def test_move_edge_piece(self):
        """Tests movement of Piece with part of footprint out of bounds"""

        game = GessGame()
        board = game.get_board()
        piece = Piece('b6')
        ctr_coord = piece.get_ctr_coord(board)
        footprint = piece.get_footprint(board, ctr_coord)
        print(footprint)
        self.assertTrue(game.make_move('b6', 'e9'))
        game.get_board().print_map()

    def test_readme_example(self):
        """Tests the example in the readme"""

        game = GessGame()
        self.assertFalse(game.make_move('m3', 'm6'))  # Black attempts to destroy own ring
        self.assertFalse(game.make_move('e14', 'g14'))  # White tries to move Piece, but not White's turn
        self.assertEqual(game.get_game_state(), 'UNFINISHED')
        game.resign_game()
        self.assertEqual(game.get_game_state(), 'WHITE_WON')

    # def test_edge_cases(self):

        # game = GessGame()
        # self.assertTrue(game.make_move('i3', 'j3'))  # moves destroys Black's ring but replaces in same move


if __name__ == "__main__":
    unittest.main()
