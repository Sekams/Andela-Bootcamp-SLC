def find_missing(list1, list2):
    missing = list(set(list2).difference(set(list1)))
    if not missing:
        missing.append(0)
    return missing[0]
