#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def min_or_max(type='max'):
    def inner(collection):
        if type == 'max':
            return max(collection)
        else:
            return min(collection)
    return inner


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    max_func = min_or_max('max')
    print(max_func(my_list))

    min_func = min_or_max('min')
    print(min_func(my_list))

    default_func = min_or_max()
    print(default_func(my_list))