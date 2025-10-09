def func(conditions, objects):
    placeholder = []
    deleted = []

    for i in range(0, len(objects), 2):
        subrange = [objects[i], objects[i+1]]
        for cond in conditions:
            cond = [[cond[0], cond[0]+cond[2]-1], [cond[1], cond[1]+cond[2]-1]]
            print(cond, subrange)
            if subrange[0] >= cond[0][0] and subrange[1] <= cond[0][1]:
                placeholder.append([cond[0][0], subrange[0]])
                placeholder.append([cond[1][0], cond[1][1]])
                placeholder.append([cond[0][1], subrange[1]])
                deleted.append([objects[i], objects[i+1]])
                break
            # elif subrange[0] <= cond[0][1]:
            #     placeholder.append([subrange[0], cond[0][1]])
            #     placeholder.append([cond[1][0]+cond[0][1]-subrange[0], cond[1][1]])
            #     deleted.append([objects[i], objects[i+1]])
            #     break
            # elif subrange[1] >= cond[0][0]:
            #     placeholder.append([subrange[0], cond[0][0]])
            #     placeholder.append([cond[1][0], cond[1][1]-subrange[1]+cond[0][0]])
            #     deleted.append([objects[i], objects[i+1]])
            #     break
        if [objects[i], objects[i+1]] not in deleted:
            placeholder.append([objects[i], objects[i+1]])
                
    p = []
    for element in placeholder:
        p.extend(element)
    return p

with open('Day5-If-You-Give-A-Seed-A-Fertilizer-input.txt', 'r') as file:
    line = file.readline().replace("\n", "").split(" ")
    for i in range(len(line)):
        try:
            line[i] = int(line[i])
        except ValueError:
            pass
    seeds = line[1:]
    s = []
    for i in range(0, len(seeds), 2):
        s.extend([seeds[i], seeds[i] + seeds[i+1] - 1])
    seeds = s
    print(seeds)
    conditions = []
    for _ in range(32):
        line = file.readline().replace("\n", "").split(" ")
        if len(line) == 3:
            conditions.append([int(i) for i in line])
        elif len(line) == 1 and _ > 3:
            print(conditions, seeds)
            seeds = func(conditions, seeds)
            print(seeds)
            conditions = []
        else:
            continue
print(min(seeds))