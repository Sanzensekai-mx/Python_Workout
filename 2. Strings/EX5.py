def pig_latin():
    input_str = input('Enter string to translate to Pig Latin: ')
    if input_str[0] in 'aeoiu':
        print(input_str + 'way')
    else:
        print(input_str[1:] + input_str[0] + 'ay')


# pig_latin()

def pig_latin_solution_true(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'


# print(pig_latin_solution_true('python'))


def pig_latin_solution(word):
    if word[0] in 'aeoiuAEOIU':
        output = f'{word}way'
        output = output if word[-1] not in '.,!?;:' else output[0:output.index(word[-1])] + output[output.index(word[-1])+1:] + word[-1]
        output = output if word[0] != word[0].capitalize() else output.title()
    else:
        output = f'{word[1:]}{word[0]}ay'
        output = output if word[-1] not in '.,!?;:' else output[0:output.index(word[-1])] + output[output.index(word[-1])+1:] + word[-1]
        output = output if word[0] != word[0].capitalize() else output.title()
    return output


# print(pig_latin_solution('Python'))
# print(pig_latin_solution('python'))
# print(pig_latin_solution('Python!'))
# print(pig_latin_solution('python?'))
# print(pig_latin_solution('Air'))
# print(pig_latin_solution('air'))
# print(pig_latin_solution('Air?'))
# print(pig_latin_solution('air,'))
# print(pig_latin_solution('Computer'))
# print(pig_latin_solution('computer'))
# print(pig_latin_solution('Computer.'))
# print(pig_latin_solution('computer;'))


def alt_pig_latin(word):
    if len(set(word) & {'a', 'e', 'o', 'i', 'u'}) > 1:
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'


# print(alt_pig_latin('wine'))
# print(alt_pig_latin('beatifulsoup'))
# print(alt_pig_latin('wind'))
# print(alt_pig_latin('cat'))