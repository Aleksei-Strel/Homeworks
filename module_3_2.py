def send_email(message, recipient, sender="univerity.help@gmail.com"):
    if '@' not in recipient or not recipient.endswith(
            ('.com', '.ru', '.net')) or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "univerity.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса{sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



send_email('messagje','university.@helpail.cm', sender = '@.com')
send_email('messagje','university.@helpail.com', sender = '.com')
send_email('messagje','mail@mail.ru',    'mail@mail.ru')
send_email('messagje','university@.com')
send_email('messagje','university@.com',    'mail@mail.ru')


