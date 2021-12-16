import sys
from math import log

DIGIT_MAP = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "height": "8",
    "nine": "9",
}


def convert(s):
    try:
        number = ""
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f"Conversion succeded x = {x}")
    # except (KeyError, TypeError):
    #     print("Conversion failed")
    #     return -1
    except (KeyError, TypeError) as expr:
        print(f"Conversion error: {expr!r}", file=sys.stderr)
        # raise is used to see the exception from convert instead of code error from log.
        raise


def string_log(s):
    v = convert(s)
    return log(v)


# print(convert("one three three seven".split()))
# print(convert("eleventeen".split()))
# print(convert(512))
print(string_log)
# will create 2 errors: TypeError(from convert()) and ValueError(from log())
print(string_log("text".split()))
# print(string_log(567))
