def reconstruct_string(input_string):
    i = 0
    reps = []
    while i < len(input_string):
        count = 1
        while i < len(input_string)-1 and input_string[i] == input_string[i+1]:
            count += 1
            i += 1
            j = i
        while count >= 4:
            reps.append(j)
            j -= 1
            count -= 1
        i += 1
    return "".join([input_string[x] for x in range(len(input_string)) if x not in reps])
