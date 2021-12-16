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
    except (KeyError, TypeError):
        print("Conversion failed")
        return -1


print(convert("one three three seven".split()))
print(convert("eleventeen".split()))
print(convert(512))


# print(f"Conversion succeeded! x={x}")
# except (KeyError, TypeError) as e:

#     print(f"Conversion error: {e!r}", file=sys.stderr)
# return -1
