def score_calculator(stuff):
    score = list(stuff.values())
    total = int(score[1])+int(score[2])+int(score[3])+int(score[4])+int(score[5])
    print(total)
    print('done')
    if 4 <= int(total) <= 8:
        return 'HUFFLEPUFF'
    elif 9 <= int(total) <= 12:
        return 'GRYFFINDOR'
    elif 13 <= int(total) <= 16:
        return 'Ravenclaw'
    else:
        return 'SLYTHERIN'
