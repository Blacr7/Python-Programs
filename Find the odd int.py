from collections import Counter
def find_it(seq):

    count = Counter()

    for i in seq:
        count[i] += 1

    count = count.most_common()

    for i in range(len(count)):
         while count[i][1] % 2 != 0:
             return(count[i][0])
             i += 1
