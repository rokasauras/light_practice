def parse_int(string):
    zero_nineteen = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    twenty_ninety = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    
    word_to_number = {word: idx for idx, word in enumerate(zero_nineteen)}
    word_to_number.update({word: idx * 10 for idx, word in enumerate(twenty_ninety) if word})
    word_to_number["hundred"] = 100
    word_to_number["thousand"] = 1000
    word_to_number["million"] = 1000000

    number = string.split()


    
    

print(parse_int("one hundred and one"))




'''
If "one" = 1 
Need to make a list with that index, and take the index number so , list = [one, two, ..., nine, ten] list(one) + 1 = value
'''