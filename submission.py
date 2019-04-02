import helper
import numpy as np


def fool_classifier(test_data):
    strategy_instance = helper.strategy()

    words_dict = {}
    num = 0

    for line in strategy_instance.class0:
        for content in line:
            if content not in words_dict.keys():
                words_dict[content] = num
                num += 1
    for line in strategy_instance.class1:
        for content in line:
            if content not in words_dict.keys():
                words_dict[content] = num
                num += 1

    data_x = []
    data_y = []
    for line in strategy_instance.class0:
        son_x = [0 for _ in range(len(words_dict))]
        for content in line:
            num = words_dict[content]
            son_x[num] += 1
        data_x.append(son_x)
        data_y.append(0)
    for line in strategy_instance.class1:
        son_x = [0 for _ in range(len(words_dict))]
        for content in line:
            num = words_dict[content]
            son_x[num] += 1
        data_x.append(son_x)
        data_y.append(1)

    clf = strategy_instance.train_svm({'gamma': 0.1, 'C': 0.01, 'kernel': 'linear',
                                       'degree': 2.0, 'coef0': 0.01}, np.array(data_x), np.array(data_y))
    with open(test_data, 'r') as fp:
        t_data = [line.strip().split(' ') for line in fp]
    word_weights = list(clf.coef_[0])
    add_word_list = []
    modified_data = './modified_data.txt'
    with open(modified_data, 'w') as fp:
        for line in t_data:
            remain_word = []
            remove_word = []
            remove_word_weight = []
            for content in line:
                if content in words_dict.keys():
                    if content in remove_word:
                        continue
                    num = words_dict[content]
                    weight = word_weights[num]
                    insert_index = 0
                    for w in remove_word_weight:
                        if w < weight:
                            break
                        insert_index += 1
                    remove_word_weight.insert(insert_index, weight)
                    remove_word.insert(insert_index, content)
                else:
                    if content not in remain_word:
                        remain_word.append(content)
            if len(remove_word) > 20:
                remove_word = remove_word[20:]
                for w in remove_word:
                    fp.write(w + " ")
                for w in remain_word:
                    fp.write(w + " ")
                fp.write("\n")
            else:
                if len(remain_word) >= 20 - len(remove_word):
                    remain_word = remove_word[20 - len(remove_word)]
                    for w in remain_word:
                        fp.write(w + " ")
                    fp.write("\n")
                else:
                    count = 20 - len(remove_word) - len(remove_word)
                    i = 0
                    for key, value in words_dict:
                        if key not in line:
                            i += 1
                            fp.write(key + " ")
                            if i == count:
                                break
                    fp.write("\n")

    assert strategy_instance.check_data(test_data, modified_data)
    return strategy_instance  ## NOTE: You are required to return the instance of this class.


strategy = fool_classifier('test_data.txt')
