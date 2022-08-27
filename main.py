#vor_al_dm_bot
#'5618758673:AAGmPuE3AM60Z2ITmfbQbK2mQQKppYG4ys4'


import telebot
from telebot import types
bot = telebot.TeleBot('5618758673:AAGmPuE3AM60Z2ITmfbQbK2mQQKppYG4ys4')#токен бота

@bot.message_handler (commands = ['start'])

#отрисовка кнопок + отпрвка приветственного сообщения

def button_message (message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Мероприятия")
    markup.add(item1)
    item1 = types.KeyboardButton("Контакты")
    markup.add(item1)
    item1 = types.KeyboardButton("Отзывы и предложения")
    markup.add (item1)
    item1 = types.KeyboardButton("FAQ")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Здравствуйте, вас приветствует бот отряда ВСКС 👋 \nесли вас интересует информация о ближайщих мероприятиях - нажмите кнопку "Мероприятия" 📅\nесли у вас появились вопросы, связанные с деятельностью отряда - нажмите кнопку "Контакты" 🤵\nесли у вас появились вопросы, связанные с работой бота - нажмите кнопку "FAQ" 🖥\nесли у вас появились предложения по улучшению работы сервиса - нажмите кнопку "Отзывы и предложения" 📞', reply_markup=markup)


@bot.message_handler (content_types='text')

def message_reply (message):

    #список мероприятий
    if message.text == "Мероприятия":
        bot.send_message (message.chat.id,'КВН \nТеатр')
    #список контактов
    if message.text == "Контакты":
        bot.send_message(message.chat.id, 'Тимофей \n8 (981) 983-08-07 \nпропуск на Кпп, набор новых людей  \n\nАндрей Покладок\n+7 (929) 365-93-01\nФорма\n\nВлад Шаров \n8 (911) 784-15-73\nВсе вопросы по отрядам их руководителям в каком отряде человек\n\nЗадворная Саша\n+7 (911) 879-27-08\nСпорт\n Расписание спортивного зала, тренировок и спортивных мероприятий\n\nФомин Кирилл\n+7 (937) 034-00-40\nСтроевая подготовка, РПК\n\nЕвстифеева Ксюша\n8 (931) 209-10-35\nУроки безопасности в школах\nМероприятия связанные с нашими традициями (чаепитие, день рождения корпуса)\n\nНекрасова Виктория\n8 (903) 070-22-53\nПресса\n\nСилантьева Екатерина\n8 (919) 016-51-92\nТворческое направление\n\nЖукина Анастасия\n8 (921) 437-98-65\nПомощь ветеранам\n\nГоловенских Альбина\n8 (981) 845-30-23\nНаправление по грантам\n\nРябухин Михаил Николаевич\n+7 (911) 987-51-20\nРуководитель Санкт-Петербургского регионального отделения ВСКС  ')
    #отправка отзывов Карине
    if message.text == "Отзывы и предложения":
        bot.reply_to(message, 'Введите текст, он будет автоматически отправлен модератору')

        @bot.message_handler(content_types=['text'])  # ф-ия реагирующая на сообщение
        def message_input_step(message):
            global text #переменная с текстом обращения

            text = message.text
            bot.send_message(message.chat.id,'ваше пожелание отправлено')#подтверждение отправки
            bot.send_message(763025006,text)# ID Карины

        bot.register_next_step_handler(message, message_input_step)

    #частозадаваемые вопросы
    if message.text == "FAQ":
        bot.send_message(message.chat.id, 'Если вас интересует информация о ближайщих мероприятиях - нажмите кнопку "Мероприятия" 📅\nесли у вас появились вопросы, связанные с деятельностью отряда - нажмите кнопку "Контакты" 🤵\nесли у вас появились предложения по улучшению работы сервиса - нажмите кнопку "Отзывы и предложения" 📞')
bot.infinity_polling()



