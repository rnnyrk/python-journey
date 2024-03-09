import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """

        if len(self.cells) == self.count and self.count != 0:
            return self.cells

        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """

        if self.count == 0:
            return self.cells

        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """

        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """

        if cell in self.cells:
            self.cells.remove(cell)



class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):
        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)

        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """

        self.moves_made.add(cell)
        self.mark_safe(cell)

        undetermined_cells = set()
        count_mines = 0

        # The first time we click on a cell, we create a sentence with the cell and its count

        # Get neighbours of the clicked cell
        for i in range(max(0, cell[0] - 1), min(cell[0] + 2, self.height)):
            for j in range(max(0, cell[1] - 1), min(cell[1] + 2, self.width)):
                # Don't check the cell itself
                if (i, j) != cell:
                    # Count mines around the cell
                    if (i, j) in self.mines:
                        count_mines += 1
                    elif (i, j) not in self.safes:
                        # If it's not a mine and it's not yet added in self.safes
                        # it's an undetermined cell
                        undetermined_cells.add((i, j))



        new_count = count - count_mines

        # Sentence returns: { (row,cell), (row,cell), (row,cell), (row,cell) } = AMOUNT_MINES
        new_sentence = Sentence(undetermined_cells, new_count)
        print(f"New sentence: {new_sentence}")

        self.knowledge.append(new_sentence)

        # Loop over all the sentences
        for sentence in self.knowledge:
            print(f"Looped sentence known_safes: {sentence.known_safes()}")
            print(f"Looped sentence known_mines: {sentence.known_mines()}")

            # If there are no undetermined cells, remove the sentence
            if len(sentence.cells) == 0:
                self.knowledge.remove(sentence)
            else:
                # Initial (first click) known_safes and known_mines are an empty set()
                # Make a copy of the object, because we change .known_safes() with the for loop
                # not copying results in -> RuntimeError: Set changed size during iteration

                # .mark_safe() and .mark_mine() both add the cell to this MinesweeperAI instance
                # as well to EVERY sentence in self.knowledge

                for safe_cell in sentence.known_safes().copy():
                    self.mark_safe(safe_cell)

                for mine_cell in sentence.known_mines().copy():
                    self.mark_mine(mine_cell)


        # Infere new senteces if new_sentence is a subset of another sentence
        for sentence in self.knowledge:
            # Sentence should have count > 0, because if count == 0, it's already marked as safe
            if new_sentence.cells.issubset(sentence.cells) and sentence.count > 0 and new_sentence.count > 0 and new_sentence != sentence:
                # Keep remaining cells and mines
                new_subset = sentence.cells.difference(new_sentence.cells)
                new_count = sentence.count - new_sentence.count

                new_sentence_subset = Sentence(new_subset, new_count)
                self.knowledge.append(new_sentence_subset)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """

        for cell in self.safes:
            if cell not in self.moves_made:
                return cell

        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """

        possible_moves = set()

        for i in range(self.height): # Loop all rows
            for j in range(self.width): # Loop all cells
                cell = (i, j)
                # If cell is not a mine and not already chosen
                if cell not in self.moves_made and cell not in self.mines:
                    possible_moves.add(cell)

        if len(possible_moves) == 0:
            return None

        return random.choice(tuple(possible_moves))
