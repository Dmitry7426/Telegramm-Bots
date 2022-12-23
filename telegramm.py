import csv
import datetime
import time
import telebot

TOKEN = 'token'
bot = telebot.TeleBot('YorKey')  # Здесь необходимо указать токен бота


#  Реагируем на команды /start или /help и говорим как отсылать данные
@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, 'Введите инв.номер устройства, наименование, и место куда установили - '
                                      'все данные указывать строго через запятую!')


# Получение, обработка ответа
@bot.message_handler(content_types=['text'])
def msg(message):
    mes = message.text.split(',')
    mes.append(datetime.datetime.now())
    user = message.from_user.first_name
    mes.append(user)
    if len(mes) != 5:  # Если длинна не равно пяти - массив не полный либо лишние данные, значит нужно ввести
        # заново информацию. Массив должен быть из 5 колонок: Инвентарный номер, наименование техники,
        # куда и(или) кому установлено. Коленка Дата и Автор устанавливается автоматически,
        # для того чтобы пользователь не мог подменить свое имя на чужое
        bot.send_message(message.chat.id, 'Введены не полные данные, не корректные, либо вы не верно поставили '
                                          'разделители - (нужно: Инв.номер, наименование полное, отдел')
    else:
        bot.send_message(message.chat.id, 'Отлично! Сообщение получено и занесено в базу')
        with open('bot_info.csv', mode='a', encoding='UTF-8') as file:  # Производим запись в файл
            file_writer = csv.writer(file, delimiter=',')
            file_writer.writerow(mes)


# Создаем вечный цикл
while True:
    try:
        bot.polling(none_stop=True)

    # Обходим ошибки чтобы скрипт не падал
    except Exception as err:
        print(err, datetime.datetime.now())
        time.sleep(15)
