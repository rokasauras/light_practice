def formatting(sentence):
    updated = sentence.lower()
    words = updated.split()
    capitalised_words = [word.capitalize() for word in words]
    result = ' '.join(capitalised_words)
    return result
    

print(formatting("SATRAJ SINGH HARLEEN KAUR ADVITHI RAJA AADIRA RAJA EMILY GOMES"))








#wanna take an input like "ROKAS JELINSKAS" and convert it to Rokas Jelinskas