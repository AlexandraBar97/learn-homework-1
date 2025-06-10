questions_and_answers = {'Привет!': 'Привет!', 'Как у тебя дела?': 'Хорошо', 'Чем занимаешься?': 'Пытаюсь всё запомнить'}
while True:
    question = input('Введите вопрос: ')
    if question in questions_and_answers:
        print(questions_and_answers[question])
    else:
        question