def pl_sentence(sentence):
    result_list = []
    for word in sentence.split():
        if word[0] in 'aeoiu':
            result_list.append(f'{word}way')
        else:
            result_list.append(f'{word[1:]}{word[0]}ay')
    return ' '.join(result_list)


# print(pl_sentence('this is a test translation'))


def strange_func(list_input):
    output = []
    list_from_element = []
    for new_lst in range(len(list_input)):
        output.append([])
    for element in list_input:
        list_from_element.append(element.split())
    for lists in list_from_element:
        for string in lists:
            for index in range(len(lists)):
                if lists.index(string) == index:
                    output[index].append(string)
                    break
    return output


# print(strange_func(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))

