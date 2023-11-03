def solution(n, words):
    word_set = set()
    previous_word = words[0]
    result = [0, 0]
    
    for (seq, word) in enumerate(words):
        # 중복 단어 확인
        if (word in word_set) or (previous_word != word and previous_word[len(previous_word) - 1] != word[0]):
            result[0] = seq % n + 1
            result[1] = seq // n + 1
            break
        
        previous_word = word
        word_set.add(word)

    return result