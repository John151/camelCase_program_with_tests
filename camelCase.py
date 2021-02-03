def camel_case(sentence):
    # convert sentence into camel case
    title_case = sentence.title()
    upper_camel_cased = title_case.replace(' ', '')
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def main():
    sentence = input('Enter your sentence: ')
    camelcased = camel_case(sentence)
    print(camelcased)

if __name__ == '__main__':
    main()