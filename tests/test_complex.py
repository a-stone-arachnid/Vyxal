# Test more complex snippets of code, taken from Vyxal answers

from test_utils import run_code
import vyxal.interpreter
import os
import sys
import builtins
from multiprocessing import Manager

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__)) + "/.."
sys.path.insert(1, THIS_FOLDER)


# from from https://codegolf.stackexchange.com/a/210307
fizzbuzz_output = [
    1,
    2,
    "Fizz",
    4,
    "Buzz",
    "Fizz",
    7,
    8,
    "Fizz",
    "Buzz",
    11,
    "Fizz",
    13,
    14,
    "FizzBuzz",
    16,
    17,
    "Fizz",
    19,
    "Buzz",
    "Fizz",
    22,
    23,
    "Fizz",
    "Buzz",
    26,
    "Fizz",
    28,
    29,
    "FizzBuzz",
    31,
    32,
    "Fizz",
    34,
    "Buzz",
    "Fizz",
    37,
    38,
    "Fizz",
    "Buzz",
    41,
    "Fizz",
    43,
    44,
    "FizzBuzz",
    46,
    47,
    "Fizz",
    49,
    "Buzz",
    "Fizz",
    52,
    53,
    "Fizz",
    "Buzz",
    56,
    "Fizz",
    58,
    59,
    "FizzBuzz",
    61,
    62,
    "Fizz",
    64,
    "Buzz",
    "Fizz",
    67,
    68,
    "Fizz",
    "Buzz",
    71,
    "Fizz",
    73,
    74,
    "FizzBuzz",
    76,
    77,
    "Fizz",
    79,
    "Buzz",
    "Fizz",
    82,
    83,
    "Fizz",
    "Buzz",
    86,
    "Fizz",
    88,
    89,
    "FizzBuzz",
    91,
    92,
    "Fizz",
    94,
    "Buzz",
    "Fizz",
    97,
    98,
    "Fizz",
    "Buzz",
]


def test_fizzbuzz():
    stack = run_code("₁ƛ₍₃₅kF½*ṅ⟇", flags=["j"])
    res = vyxal.interpreter.pop(stack)
    assert res == fizzbuzz_output
