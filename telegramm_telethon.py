from telethon import TelegramClient, sync, events

# Бот на отслеживание новых сообщений в группе и последующей рассылке по ответственным

api_id = 777777  # Задается ID группы, которую будем слушать
api_hash = 'sfghdfhdfghdfghdfgh5434'
client = TelegramClient('session_name', api_id, api_hash)

problems = []  # Массив с пулом проблем отловленных по условию
Progs1C = ["xxxxx", "xxxxx2", "xxxxx3", ........"xxxx8"]  # массив для программистов 1С


@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'Problem started' in event.raw_text:  # Если есть проблема
        pr2 = event.raw_text.split('\n')
        for key, value in enumerate(pr2):
            if 'Host' in value:
                problems.append(value.split(': ')[1])
                pr_id = pr2[6].split(': ')[1]
                problems.append(pr_id)
                print(value.split(': ')[1])
                if value.split(': ')[1] in Progs1C:
                    await client.send_message(-xxxxxxx, event.raw_text)  # Если в сообщении есть проблема из
                    #  пула Progs1C то пересылаем сигнал ответственному человеку за 1С
                    print('Сообщение для ФИО о проблеме доставлено')
                print('Проблемы с HOST', value.split(': ')[1])  # Вывод в консоль инфо о проблеме (можно убрать)
                print('содержимое массива: ', problems)

    if 'Resolved' in event.raw_text:  # Если проблема решена
        rv = event.raw_text.split('\n')
        for key, value in enumerate(rv):
            if 'Host' in value:
                print(value.split(': ')[1])
                rs_id = rv[6].split(': ')[1]
                print('ИД решенной проблемы: ', rs_id)
                print(problems)
                if value.split(': ')[1] in Progs1C:
                    await client.send_message(-xxxxxxx, event.raw_text)  # Уведомляем ответственного, что проблема
                    # решена
                    print('Сообщение для ФИО о решении доставлено')
                if rs_id in problems:
                    print('Проблема с хостом ', value.split(': ')[1], ' решена')  # Вывод в консоль о решении
                    problems.remove(rs_id)
                    problems.remove(value.split(': ')[1])  # Удаляем из пула решенную проблему, чтобы не
                    # замусоривать массив

        await event.reply('Проблема решена')


client.start()
client.run_until_disconnected()
