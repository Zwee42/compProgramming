def extract_most_ones(s):
    most_ones = 0
    ones = 0
    index = -1
    p_index = -1
    for c_index, digit in enumerate(s):
        if digit == '1':
            ones += 1
            if(p_index == -1):
                p_index = c_index
        else:
            if ones > most_ones:
                most_ones = ones
                index = p_index
            p_index = -1
            ones = 0
    if ones > most_ones:
        most_ones = ones
        index = p_index

    return (most_ones, s[:index] + s[index+most_ones:])


n = int(input())

for i in range(1, n + 1):
    v = input()   
    a_score = 0
    a_turn = True
    while('1' in  v):
        (score, new_v) = extract_most_ones(v)
        v = new_v
        if a_turn:
            a_score += score
        a_turn = not a_turn

    print(a_score)


