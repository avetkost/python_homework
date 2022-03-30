def pascal(column,member):
    # return 1 if column == 1 elif member == 1 1 elif column == 2 member else column
   if column == 1:
        return 1
    elif member == 1:
        return 1
    elif column == 2:
        return member
    elif member == 2:
        return column
    return pascal(column-1,member) + pascal(column,member-1)


print(pascal(3,6))



