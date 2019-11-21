import os


def camelcase(s):
    return 1 + len(list(filter(lambda x: x & 0x20 == 0, bytearray(s, "utf8"))))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + "\n")

    fptr.close()
