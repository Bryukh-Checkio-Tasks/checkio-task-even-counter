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
            "input": 123456,
            "answer": 3
        },
        {
            "input": 111111,
            "answer": 0,
        },
        {
            "input": 24680,
            "answer": 5,
        },
        {
            "input": 1234567890,
            "answer": 5,
        },
        {
            "input": 9999999999,
            "answer": 0,
        },
        {
            "input": 1000000000,
            "answer": 9,
        },
        {
            "input": 42,
            "answer": 2,
        }
    ],
    "Extra": [
        {
            "input": 2000000000,
            "answer": 10,
        },
        {
            "input": 777,
            "answer": 0,
        },
        {
            "input": 134,
            "answer": 1,
        },
        {
            "input": 88,
            "answer": 2,
        },
    ]
}
