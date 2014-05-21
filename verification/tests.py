"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["hello", "lo", "he"],
            "answer": True,
            "explanation": ["hel", "lo"]
        },
        {
            "input": ["hello", "la", "hellow", "cow"],
            "answer": False,
            "explanation": None
        },
        {
            "input": ["walk", "duckwalk"],
            "answer": True,
            "explanation": ["duck", "walk"]
        },
        {
            "input": ["one"],
            "answer": False,
            "explanation": None
        },
        {
            "input": ["helicopter", "li", "he"],
            "answer": False,
            "explanation": None
        },

    ],
    "Extra": [
        {
            "input": ["a", "the", "wall", "world", "nine"],
            "answer": False,
            "explanation": None
        },
        {
            "input": ['longest', 'aa', 'a'],
            "answer": True,
            "explanation": ["a", "a"]
        },
        {
            "input": [
                'jsakhfakljsdfhsakjdfhljkasdhfkasdjhfjklasdhfkasdhfalksjdhejkyrieucbciuwaeiuwhewkqjiorfuvnfjhbkehraa',
                'aarhekbhjfnvufroijqkwehwuieawuicbcueirykjehdjsklafhdsakfhdsalkjfhjdsakfhdsakjlhfdjkashfdsjlkafhkasj'],
            "answer": False,
            "explanation": None
        },


        {
            "input": ["abc", "cba", "ba", "a", "c"],
            "answer": True,
            "explanation": ["cba", "ba"]
        },
        {
            "input": ["chupacabra", "megachupacabra", "gigachupacabra"],
            "answer": True,
            "explanation": ["mega", "chupacabra"]
        },
        {
            "input": ["giga", "mega", "woltz", "kilo"],
            "answer": False,
            "explanation": None
        },
        {
            "input": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"],
            "answer": False,
            "explanation": None
        },
        {
            "input": ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "pacsix"],
            "answer": True,
            "explanation": ["pac", "six"]
        },
        {
            "input": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v', 'w', 'x', 'y', 'z'],
            "answer": False,
            "explanation": None
        },
        {
            "input": ["check", "io", "checkio"],
            "answer": True,
            "explanation": ["check", "io"]
        },


    ]
}
