#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest

import numpy as np
import cshogi

__author__ = 'Yasuhiro'
__date__ = '2019/09/23'


def load_data(file_name):
    with open(file_name, 'r') as f:
        data_list = []
        for line in f:
            sfen = line
            move = next(f)
            score = next(f)
            ply = next(f)
            result = next(f)
            next(f)

            data = {'sfen': sfen[5:].strip(), 'move': move[5:].strip(),
                    'score': int(score[6:]), 'gamePly': int(ply[4:]),
                    'game_result': int(result[7:])}
            data_list.append(data)
    return data_list


class TestLoadPackedSfen(unittest.TestCase):
    # noinspection PyUnresolvedReferences
    def test_loader(self):
        data_dir = '../../../data'
        bin_data_list = np.fromfile(os.path.join(data_dir, 'head0.bin'),
                                    dtype=cshogi.PackedSfenValue)
        txt_data_list = load_data(os.path.join(data_dir, 'head0.txt'))

        board_bin = cshogi.Board()
        board_txt = cshogi.Board()
        for i, (bin_data, txt_data) in enumerate(zip(bin_data_list,
                                                     txt_data_list)):
            board_bin.set_psfen(bin_data['sfen'])
            board_txt.set_sfen(txt_data['sfen'])

            with self.subTest(i=i, board_bin=board_bin, board_txt=board_txt):
                self.assertEqual(board_bin.pieces, board_txt.pieces)
                self.assertTupleEqual(board_bin.pieces_in_hand,
                                      board_txt.pieces_in_hand)
                self.assertEqual(board_bin.turn, board_txt.turn)
                # self.assertEqual(board_bin, board_txt)

                if txt_data['move'][1] == '*':
                    self.assertEqual((bin_data['move'] >> 14) & 0x1, 1)
                    # self.assertGreaterEqual((bin_data['move'] >> 7) & 0x3F, 81)
                # self.assertEqual(cshogi.move_to_usi(bin_data['move']),
                #                  txt_data['move'])
                self.assertEqual(bin_data['score'], txt_data['score'])
                self.assertEqual(bin_data['gamePly'], txt_data['gamePly'])

                tmp = bin_data['game_result']
                result = -1 if tmp == 255 else tmp
                self.assertEqual(result, txt_data['game_result'])


if __name__ == '__main__':
    unittest.main()
