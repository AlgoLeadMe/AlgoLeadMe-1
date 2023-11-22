def solution(babbling):
    pronunciations = ("aya", "ye", "woo", "ma")
    count = 0

    for text in babbling:
        last_sub_text = ""
        is_vaild = False

        while len(text) > 0:
            is_vaild = False
            for available_pron in pronunciations:
                if text.startswith(available_pron):
                    if last_sub_text == available_pron:
                        is_vaild = False
                    else:
                        last_sub_text = available_pron
                        text = text[len(available_pron) :]
                        is_vaild = True

                    break

            if not is_vaild:
                break

        if is_vaild:
            count += 1

    return count
