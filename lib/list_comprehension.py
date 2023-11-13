#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [num for num in num_list if num % 2 == 0]
    return even_nums

print(return_evens([1,2,3,4,5,6,7,8,9]))



def make_exclamation(sentence_list):
    exclamatory = [sentence + '!' for sentence in sentence_list]
    return exclamatory
    