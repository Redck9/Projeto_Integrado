class Point(object):
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y




class WordSearch(object):

    def __init__(self, puzzle):
        self.lines = puzzle


    def search(self, word):
        for r_s in range(0, len(self.lines)):
            for c_s in range(0, len(self.lines[r_s])):
                if self.lines[r_s][c_s] == word[0]:
                    for dir_row in range(-1, 2):
                        for dir_col in range(-1, 2):
                            if dir_row != 0  or  dir_col != 0:
                                mismatch_fnd = False
                                i = 1
                                while mismatch_fnd == False  and  i < len(word):
                                    r = r_s + dir_row * i
                                    c = c_s + dir_col * i

                                    if (r not in range(0, len(self.lines))) or \
                                       (c not in range(0, len(self.lines[r_s]))) or \
                                       (self.lines[r][c] != word[i]):
                                        mismatch_fnd = True
                                    else:
                                        i += 1

                                if mismatch_fnd == False:
                                    return (Point(c_s, r_s), Point(c, r))