def func(condidions, objects):
    placeholder = []
    deleted = []
    for obj in objects:
        for cond in condidions:
            if obj >= cond[1] and obj < (cond[1] + cond[2]):
                placeholder.append(cond[0] + obj - cond[1])
                # print(f"condition: {cond}")
                # print(f"{obj} -> {cond[0] + obj - cond[1]}")
                deleted.append(obj)
                break
        if obj not in deleted:
            # print(f"{obj} -> {obj}")
            placeholder.append(obj)
    return placeholder

with open('Day5-If-You-Give-A-Seed-A-Fertilizer-input.txt', 'r') as file:
    line = file.readline().replace("\n", "").split(" ")
    for i in range(len(line)):
        try:
            line[i] = int(line[i])
        except ValueError:
            pass
    seeds = line[1:]
    conditions = []
    for _ in range(32):
        line = file.readline().replace("\n", "").split(" ")
        print(line, _)
        if len(line) == 3:
            conditions.append([int(i) for i in line])
        elif len(line) == 1:
            seeds = func(conditions, seeds)
            conditions = []
        else:
            continue
print(min(seeds))