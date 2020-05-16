# -*- coding: utf-8 -*-
"""
Created on Sat May 16 16:32:13 2020

@author: genti
"""
import itertools

GUI = {
        (0, 0): {"ymin": 292, "ymax": 326, "xmin": 555, "xmax": 586},
        (1, 0): {"ymin": 292, "ymax": 326, "xmin": 634, "xmax": 664},
        (2, 0): {"ymin": 292, "ymax": 326, "xmin": 718, "xmax": 743},
        (3, 0): {"ymin": 292, "ymax": 326, "xmin": 792, "xmax": 821},
        (0, 1): {"ymin": 377, "ymax": 400, "xmin": 555, "xmax": 586},
        (1, 1): {"ymin": 377, "ymax": 400, "xmin": 634, "xmax": 664},
        (2, 1): {"ymin": 377, "ymax": 400, "xmin": 718, "xmax": 743},
        (3, 1): {"ymin": 377, "ymax": 400, "xmin": 792, "xmax": 821},
        (0, 2): {"ymin": 456, "ymax": 478, "xmin": 555, "xmax": 586},
        (1, 2): {"ymin": 456, "ymax": 478, "xmin": 634, "xmax": 664},
        (2, 2): {"ymin": 456, "ymax": 478, "xmin": 718, "xmax": 743},
        (3, 2): {"ymin": 456, "ymax": 478, "xmin": 792, "xmax": 821},
        (0, 3): {"ymin": 533, "ymax": 555, "xmin": 555, "xmax": 586},
        (1, 3): {"ymin": 533, "ymax": 555, "xmin": 634, "xmax": 664},
        (2, 3): {"ymin": 533, "ymax": 555, "xmin": 718, "xmax": 743},
        (3, 3): {"ymin": 533, "ymax": 555, "xmin": 792, "xmax": 821}
}

def get_vocabulary(filename="language_files\italian_vocab.txt"):
    with open(filename, "r") as file:
        WORDS = [line.replace("\n","") for line in file.readlines()]
        WORDS = [w for w in WORDS if 2 <= len(w) <= 16]
        
        return WORDS

def check(point, pos, path, father):
    if pos < len(word):
        letter = word[pos]
        path[pos] = []
        for direction, cell in point.loc.items():
            if cell and cell.contains(letter) and cell not in father:
                path[pos].append(cell)
                if pos == len(word)-1:
                    father.append(point)
                    father.append(cell)
                    return father

        if not path[pos]:
            pass
        
        elif path[pos] and pos == len(word)-1:
            return father
        
        else:
            new_pos = pos + 1
            father.append(point)
            for cell in path[pos]:
                found = check(cell, new_pos, path, father)
                if found:
                    return found
                
class Cell:
    def __init__(self, coords=tuple, letter=str, visited=False):
        self.coords = coords
        self.x, self.y = self.coords
        self.gui = GUI[self.coords]
        self.real_x = int
        self.real_y = int
        self.letter = letter
        self.visited = visited
        self.loc = {(self.x-1, self.y-1): Cell , (self.x, self.y-1): Cell, (self.x+1, self.y-1): Cell,
                   (self.x-1, self.y): Cell,                              (self.x+1, self.y): Cell,
                   (self.x-1, self.y+1): Cell, (self.x, self.y+1): Cell, (self.x+1, self.y+1): Cell
                   }
    
        if self.y == 0:
            self.loc[(self.x-1, self.y-1)] = None
            self.loc[(self.x, self.y-1)] = None
            self.loc[(self.x+1, self.y-1)] = None
        
        if self.y == 3:
            self.loc[(self.x-1, self.y+1)] = None
            self.loc[(self.x, self.y+1)] = None
            self.loc[(self.x+1, self.y+1)] = None
            
        if self.x == 0:
            self.loc[(self.x-1, self.y-1)] = None
            self.loc[(self.x-1, self.y)] = None
            self.loc[(self.x-1, self.y+1)] = None   
        
        if self.x == 3:
            self.loc[(self.x+1, self.y-1)] = None
            self.loc[(self.x+1, self.y)] = None
            self.loc[(self.x+1, self.y+1)] = None
    
    def __repr__(self):
        return self.letter
    
    def visit(self):
        self.visited = True
    
    def is_close(self, Cell):
        return Cell.coords in self.loc.values()
    
    def is_close_to_letter(self, letter):
        return [c for c in self.loc.values() if c and c.contains(letter)]
        
    def contains(self, letter):
        return self.letter == letter

        
class Frame:
    def __init__(self, gs):
        board = [gs[i:i+4] for i in range(0, len(gs), 4)]
        self.board = [[Cell(coords=(j, i), letter=c) for j, c in enumerate(l)]\
                       for i, l in enumerate(board)]
        self.frame = list(itertools.chain(*self.board))
        
        for i, line in enumerate(self.board):
            for j, cell in enumerate(line):
                for xy, v in cell.loc.items():
                    if v:
                        self.board[i][j].loc[xy] = self.board[xy[1]][xy[0]]
    
    def __repr__(self):
        return "\n".join([" ".join([c.letter for c in l]) for l in self.board])
                
      