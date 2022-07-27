def subset_sum(numbers, target, out, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        out.append(partial)
    if s >= target:
        return  # if we reach the number why bother to continue
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, out, partial + [n]) 
   
def get_subset(numbers, target):
    """ returns with list of all int combinations, summing up to target number. """
    out = []
    subset_sum(numbers, target, out)
    return out