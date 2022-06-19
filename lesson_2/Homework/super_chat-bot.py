met_bye_phrase = False
while (met_bye_phrase == False):
    user_text = input('введите фразу ')
    greeting_phrases = ['привет', 'дароу', 'добрый день']
    goodbye_phrases = ['до свидания', 'пока', 'покеда', 'доброго вечера']
    bad_phrases = ['бля', 'черт', 'блин']

    for greeting_frase in greeting_phrases:
        if greeting_frase in user_text:
            print('привет и тебе!')
            break
    else:
        for goodbye_frase in goodbye_phrases:
            if goodbye_frase in user_text:
                print('до свидания!')
                met_bye_phrase = True
                break
        else:
            for bad_frase in bad_phrases:
                if bad_frase in user_text:
                    print('не ругайся')
                    break
                else:
                    print('я тебя не понимаю')
                    break
