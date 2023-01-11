from math import floor

def lst_print_split_rec(lst, le, ri):
    leftList = []
    rightList = []
    if len(lst) > 1:
        middle = floor((le + ri) / 2)
        split = floor((len(lst) - 1) / 2)
        for i in range(len(lst)):
            if i <= split:
                leftList.append(lst[i])
            if i > split:
                rightList.append(lst[i])
        print("Middle -> ", middle)
        print("left: ")
        print("\t", leftList)
        print("right: ")
        print("\t", rightList)
        return lst_print_split_rec(leftList, (middle + 1) - len(leftList), middle), lst_print_split_rec(rightList, middle + 1, ri)