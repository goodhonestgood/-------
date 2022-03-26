exs = input()
counts = exs.count('-')
if counts == 0:
    print(sum(list(map(int, exs.split('+')))))
else:
    exs_list = exs.split('-')
    results = []
    for ex in exs_list:
        results.append(sum(list(map(int, ex.split('+')))))

    print(sum([results[0]]+[r*(-1) for r in results[1:]]))

