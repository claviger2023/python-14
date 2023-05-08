import sys


def parse_args():
    result = ""
    n = 0
    for arg in sys.argv:
        if n != 0:
            if result != "":
                result = result + " " + arg
            else:
                result = arg
        n +=1
    print(result)    
    return result

parse_args()