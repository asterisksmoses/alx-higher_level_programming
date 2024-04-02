#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []

    for y in range(list_length):
        try:
            if y < len(my_list_1) and y < len(my_list_2):
                res.append(my_list_1[y] / my_list_2[y])
            else:
                raise IndexError("out of range")
        except ZeroDivisionError:
            print("division by 0")
            res.append(0)
        except TypeError:
            print("wrong type")
            res.append(0)
        except IndexError as e:
            print(e)
            res.append(0)
        finally:
            print(res[y])
        return res
