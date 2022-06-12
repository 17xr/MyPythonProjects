# A function to convert romans to numeral
def roman_to_numeral(num):
    # A dictionary with each roman letter and its numerical value
    roman_values = {"M": 1000,
                    "D": 500,
                    "C": 100,
                    "L": 50,
                    "X": 10,
                    "V": 5,
                    "I": 1}s
    # result variable is clear, last will be used to compare current value with the previous one
    last, result = 0, 0
    # Iterate over reversed number
    for i in num[::-1]:
        if last == 0:
            result += roman_values[i]
        # if current number is smaller than previous one then we must remove it as these 2 nums are a 2 digits number
        elif last > roman_values[i]:
            result -= roman_values[i]
        else:
            result += roman_values[i]
        # set current num to last
        last = roman_values[i]
    return result


# A function to convert nums to roman
def numeral_to_roman(num):
    # It's clear (I used a list with sublists instead of a dict as I needed numbers sorted by value)
    roman_values = [["M",1000],
                    ["CM",900],
                    ["D",500],
                    ["CD",400],
                    ["C",100],
                    ["XC",90],
                    ["L",50],
                    ["XL",40],
                    ["X",10],
                    ["IX",9],
                    ["V",5],
                    ["IV",4],
                    ["I",1]]
    # index to iterate over the number
    i = 0
    result = ""
    while num > 0:
        # Quotient of dividing the number by values of list above
        x = num // roman_values[i][1]
        if x > 0:
            result += roman_values[i][0] * x
            # New num value is the remainder of division of previous value
            num = num % roman_values[i][1]
        else:
            # increase iteration
            i += 1
    return result
