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
    ],
    "Extra": [
        {
            "input": [6, 3],
            "answer": 9,
            "explanation": "6+3=?"
        },
        {
            "input": [6, 7],
            "answer": 13,
            "explanation": "6+7=?"
        }
    ]
}
