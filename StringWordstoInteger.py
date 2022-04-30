def parse_int(string):
    list_num = {'zero': 0,
                'one': 1,
                'two': 2,
                'three': 3,
                'four': 4,
                'five': 5,
                'six': 6,
                'seven': 7,
                'eight': 8,
                'nine': 9,
                'ten': 10,
                'eleven': 11,
                'twelve': 12,
                'thirteen': 13,
                'fourteen': 14,
                'fifteen': 15,
                'sixteen': 16,
                'seventeen': 17,
                'eighteen': 18,
                'nineteen': 19,
                'twenty': 20,
                'thirty': 30,
                'forty': 40,
                'fifty': 50,
                'sixty': 60,
                'seventy': 70,
                'eighty': 80,
                'ninety': 90}
    list_subs ={'thousand': 1000,
                'million': 1000000}
    result = 0
    subs = 0
    new_str = string.replace(" and "," ").replace("-"," ").split()
    for elem in new_str:
        if elem in list_num:
            subs += list_num[elem]
        elif elem == 'hundred':
            subs *= 100
        else:
            subs *= list_subs[elem]
            result += subs
            subs = 0
    result += subs
    return result

print(parse_int("one hundred and one"))