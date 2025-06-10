while True:
    user = input('Как дела? ')
    try:
        if user == 'Хорошо':
            break
        else:
            user
    except KeyboardInterrupt:
        print('Пока')
        break