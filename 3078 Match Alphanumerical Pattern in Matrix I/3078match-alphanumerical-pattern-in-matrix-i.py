from typing import List, Tuple

class Solution:
    def pattern_match_found_in_board(self, board: List[List[int]], pattern: List[str], up_l_c: Tuple[int, int]) -> bool:
        seen_pat_chars: dict[str, int] = {}
        seen_board_ints: dict[int, str] = {}
        s_r_i, s_c_i = up_l_c

        for r_pat_i, r_i in enumerate(range(s_r_i, s_r_i + len(pattern))):
            for c_pat_i, c_i in enumerate(range(s_c_i, s_c_i + len(pattern[0]))):
                cur_board_int = board[r_i][c_i]
                cur_pat_char = pattern[r_pat_i][c_pat_i]

                if cur_pat_char.isdigit():
                    if int(cur_pat_char) != cur_board_int:
                        return False
                else:
                    if (
                        cur_pat_char in seen_pat_chars and seen_pat_chars[cur_pat_char] != cur_board_int
                    ) or (
                        cur_board_int in seen_board_ints and seen_board_ints[cur_board_int] != cur_pat_char
                    ):
                        return False
                    
                    seen_pat_chars.setdefault(cur_pat_char, cur_board_int)
                    seen_board_ints.setdefault(cur_board_int, cur_pat_char)

        return True

    def findPattern(self, board: List[List[int]], pattern: List[str]) -> Tuple[int, int]:
        NO_MATCH_RES = (-1, -1)

        if len(pattern) > len(board) or len(pattern[0]) > len(board[0]):
            return NO_MATCH_RES

        cand_ress: List[Tuple[int, int]] = []
        for r_i in range(len(board) - len(pattern) + 1):                        
            for c_i in range(len(board[0]) - len(pattern[0]) + 1):
                up_l_c = (r_i, c_i)
                if self.pattern_match_found_in_board(board, pattern, up_l_c):
                    cand_ress.append(up_l_c)

        return min(cand_ress, default=NO_MATCH_RES)