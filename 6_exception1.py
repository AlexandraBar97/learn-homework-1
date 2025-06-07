"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
user = input('Как дела? ')
def hello_user(user):
  try:
    while True:
      if user == 'Хорошо':
        break
  except:
    print('Пока')
    break