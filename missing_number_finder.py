import itertools


def find_missing_numbers():
    possible_numbers = [1, 3, 6, 7]
    string = "2??8+?456==?174"

    possibilities = itertools.permutations(possible_numbers)
    for each_possibility in possibilities:
        new_string = string
        for each_number in each_possibility:
            # we put 1 in below statement to state that only replace the first occurance of question mark, otherwise it will replace with all of them.
            new_string = new_string.replace('?', str(each_number), 1)
        # (eval checks for the equation) if eqaution comes true means if equation gives right answer then print it.
        if eval(new_string):
            print(new_string)


find_missing_numbers()
