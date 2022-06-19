user_text = input('введите фразу ')
greeting_phrases = ['привет', 'дароу', 'добрый день']
greeting_phrases_2 = ['до свидания', 'пока', 'покеда', 'доброго вечера']
greeting_phrases_3 = ['бля', 'черт', 'блин']

for greeting_frase in greeting_phrases:
    if user_text == greeting_frase:
        print('привет и тебе!')
        break
else:
    for greeting_frase in greeting_phrases_2:
        if user_text == greeting_frase:
            print('пока!')
            break
    else:
        for greeting_frase in greeting_phrases_3:
            if user_text == greeting_frase:
                print('не ругайся')
                break
            else:
                print('я тебя не понимаю')
