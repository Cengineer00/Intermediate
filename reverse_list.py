def reverse_list(lst):
    if len(lst)==0:
        return []
    elif type(lst[0])==list:
        lst[0]=reverse_list(lst[0])
        return  reverse_list(lst[1:]) + [lst[0]]
    else:
        return reverse_list(lst[1:])+[lst[0]]
