#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for i in range(list_length):
        try:
            res_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            res_list.append(0.0)
            print("wrong type")
        except ZeroDivisionError:
            res_list.append(0.0)
            print("division by 0")
        except IndexError:
            print("out of range")
    return res_list
