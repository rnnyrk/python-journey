from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

knowledge_base = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    knowledge_base,
    # We expect this is true because a knight always tells the truth
    Implication(AKnight, And(AKnight, AKnave)),
    # We expect this is false because a knva always lies
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    knowledge_base,
    # A is a knight and he is telling the truth, because A & B both knaves (NOT POSSIBLE)
    # So A must be a knave because he is lying
    Implication(AKnight, And(AKnave, BKnave)),

    # Reverse the implication if A is lying
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    knowledge_base,
    # If A is a knight, both are the same
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # If A is lying, they are both different
    Implication(AKnave, Or(And(AKnave, BKnight), And(AKnight, BKnave))),

    # If B is a knight, they are both different
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),

    # If B is a knave, they are both the same
    Implication(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    knowledge_base,

    # If not lying, A says either "I am a knight." or "I am a knave.",
    Implication(AKnight, Or(AKnight, AKnave)),
    # if lying, A says I'm neither "a knave." or "a knight.",
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    # B says "A said 'I am a knave'."
    Or(
        # If B is a knight and he is telling the truth
        Implication(BKnight, Or(
            # A is a knight and telling the truth about him being a knave (NOT POSSIBLE)
            And(AKnight, AKnave), 
            # OR A is a knave and lying about him being a knave (ALSO NOT POSSIBLE)
            And(AKnave, AKnight)
        )),

        # If B is a knave and lying 
        # A is NOT a knight and lying about him being a knave
        # OR A is NOT a knave and telling the truth about him being knight
        Implication(BKnave, Not(
            Or(
                And(AKnight, AKnave),
                And(AKnave, AKnight),
            )
        )),
    ),

    # B says "C is a knave.", so if B is a knight, C is a knave
    Implication(BKnight, CKnave),
    # if B is a knave, C is a knight because B is lying
    Implication(BKnave, Not(CKnave)),

    # C says "A is a knight.", so if C is a knight, A is a knight
    Implication(CKnight, AKnight),
    # If C is lying, A is a knave
    Implication(CKnave, Not(AKnight)),
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
