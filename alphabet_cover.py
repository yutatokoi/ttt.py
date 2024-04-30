import itertools

def alphabet_cover(word_list):
    output = None
    shortest_len = len(word_list)

    for i in range(len(word_list)):
        combination = itertools.combinations(word_list, i)
        
        for c in combination:
            if len(c) < shortest_len and len(set("".join(c))) == 26:
                output = c
                shortest_len = min(shortest_len, len(c))
    return output


print(alphabet_cover(['abcpqr', 'omg', 'abxy', 'onmlkjihgfed', 'stuvwxyz']))

