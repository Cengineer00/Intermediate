def sum_all(lst):
    if len(lst)==0:
        return 0
    elif type(lst[0])==list:
        lst=lst[0][:]+lst[1:]
        return sum_all(lst)
    else:
        return lst[0]+sum_all(lst[1:])
