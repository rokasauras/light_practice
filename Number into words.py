
def parse_int(string):
    zero_nineteen = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    twenty_ninety = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    word_to_number = {word: idx for idx, word in enumerate(zero_nineteen)}
    word_to_number.update({word: idx * 10 for idx, word in enumerate(twenty_ninety) if word})
    word_to_number["hundred"] = 100
    word_to_number["thousand"] = 1000
    word_to_number["million"] = 1000000

    number_words = string.replace("-", " ").split()

    total = 0
    current = 0

    for word in number_words:
        if word in word_to_number:
            value = word_to_number[word]
            if value == 100:
                current *= value
            elif value >= 1000:
                total += current * value
                current = 0
            else:
                current += value
    
    return total + current




print(parse_int("Ninety-nine million nine hundred ninety-nine"))

