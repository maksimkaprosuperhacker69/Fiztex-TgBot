import telebot
from telebot import types



bot=telebot.TeleBot('6077200675:AAH0C6Vb4dZe__W4p0NUxU4H1Dm1V85xzX8')



@bot.message_handler(commands=['start'])
def start (message):
    with open('user_ids.txt', 'a') as file:
        file.write(str(message.chat.id) + '\n')
    mess=f'Привет,<b>{message.from_user.first_name}</b> это бот школы ФизТех,здесь ты сможешь найти расписание! <b>Если хочешь узнать расписание звонков пиши /raspisanie</b>'
    bot.send_message(message.chat.id,mess,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    sevenD = types.KeyboardButton('/7Д')
    sevenE = types.KeyboardButton('/7Е')
    sevenZh = types.KeyboardButton('/7Ж')
    sevenAe = types.KeyboardButton('/7AE')
    eightAe = types.KeyboardButton('/8AE')
    eightV = types.KeyboardButton('/8В')
    sevenB=types.KeyboardButton('/7Б')
    sevenV=types.KeyboardButton('/7В')
    sevenG=types.KeyboardButton('/7Г')
    eightA=types.KeyboardButton('/8А')
    eightB=types.KeyboardButton('/8Б')
    markup.add(sevenD,sevenE,sevenZh,sevenAe,eightAe,eightV,sevenB,sevenV,sevenG,eightA,eightB )
    bot.send_message(message.chat.id, 'Выбери свой класс:', parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['7Д'])
def sevenD(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon1')
    Tue = types.KeyboardButton('/Tue1')
    Wed = types.KeyboardButton('/Wed1')
    Thur = types.KeyboardButton('/Thur1')
    Fri = types.KeyboardButton('/Fri1')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon1'])
    def MonSevD(message):
        photo = open('7Д Пн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Tue1'])
    def TueSevD(message):
        photo1 = open('7Д ВТ (2).jpeg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Wed1'])
    def WedSevD(message):
        photo2 = open('7Д Ср.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Thur1'])
    def ThurSevD(message):
        photo3 = open('7Д Чв.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo3)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Fri1'])
    def FriSevD(message):
        photo4 = open('7Д ПТ.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo4)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)






@bot.message_handler(commands=['7Е'])
def sevenE(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon2')
    Tue = types.KeyboardButton('/Tue2')
    Wed = types.KeyboardButton('/Wed2')
    Thur = types.KeyboardButton('/Thur2')
    Fri = types.KeyboardButton('/Fri2')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon2'])
    def MonSevE(message):
        photo = open('7ЕПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
        return
    @bot.message_handler(commands=['Tue2'])
    def TueSevE(message):
        photo = open('7ЕВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Wed2'])
    def WedSevE(message):
        photo = open('7ЕСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Thur2'])
    def ThurSevE(message):
        photo = open('7ЕЧТ.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Fri2'])
    def FriSevE(message):
        photo = open('7E ПТ.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)






@bot.message_handler(commands=['7Ж'])
def sevenZh(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon3')
    Tue = types.KeyboardButton('/Tue3')
    Wed = types.KeyboardButton('/Wed3')
    Thur = types.KeyboardButton('/Thur3')
    Fri = types.KeyboardButton('/Fri3')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon3'])
    def MonSevZh(message):
        photo = open('7жПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Tue3'])
    def TueSevZh(message):
        photo = open('7жВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Wed3'])
    def WedSevZh(message):
        photo = open('7жСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Thur3'])
    def ThurSevZh(message):
        photo = open('7жЧт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Fri3'])
    def FriSevZh(message):
        photo = open('7жПт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)







@bot.message_handler(commands=['7AE'])
def sevenAe(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon4')
    Tue = types.KeyboardButton('/Tue4')
    Wed = types.KeyboardButton('/Wed4')
    Thur = types.KeyboardButton('/Thur4')
    Fri = types.KeyboardButton('/Fri4')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon4'])
    def MonSevAe(message):
        photo = open('7ЭПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Tue4'])
    def TueSevAe(message):
        photo = open('7эВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Wed4'])
    def WedSevAe(message):
        photo = open('7эСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Thur4'])
    def ThurSevAe(message):
        photo = open('7эЧт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Fri4'])
    def FriSevAe(message):
        photo = open('7эПт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)









@bot.message_handler(commands=['8В'])
def eightV(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon5')
    Tue = types.KeyboardButton('/Tue5')
    Wed = types.KeyboardButton('/Wed5')
    Thur = types.KeyboardButton('/Thur5')
    Fri = types.KeyboardButton('/Fri5')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon5'])
    def MonEiV(message):
        photo = open('8вПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Tue5'])
    def TueEiV(message):
        photo = open('8вВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Wed5'])
    def WedEiV(message):
        photo = open('8вСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Thur5'])
    def ThurEiV(message):
        photo = open('8вЧт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Fri5'])
    def FriEiV(message):
        photo = open('8вПт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)









@bot.message_handler(commands=['8AE'])
def eightE(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon6')
    Tue = types.KeyboardButton('/Tue6')
    Wed = types.KeyboardButton('/Wed6')
    Thur = types.KeyboardButton('/Thur6')
    Fri = types.KeyboardButton('/Fri6')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon6'])
    def MonEiAe(message):
        photo = open('8эПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Tue6'])
    def TueEiAe(message):
        photo = open('8эВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Wed6'])
    def WedEiAe(message):
        photo = open('8эСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Thur6'])
    def ThurEiAe(message):
        photo = open('8эЧт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Fri6'])
    def FriEiAe(message):
        photo = open('8эПт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)








@bot.message_handler(commands=['7Б'])
def sevenB(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon7')
    Tue = types.KeyboardButton('/Tue7')
    Wed = types.KeyboardButton('/Wed7')
    Thur = types.KeyboardButton('/Thur7')
    Fri = types.KeyboardButton('/Fri7')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon7'])
    def MonSevB(message):
        photo = open('7бПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Tue7'])
    def TueSevB(message):
        photo = open('7бВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Wed7'])
    def WedSevB(message):
        photo = open('7бСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Thur7'])
    def ThurSevB(message):
        photo = open('7бЧт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Fri7'])
    def FriSevB(message):
        photo = open('7бПт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)







@bot.message_handler(commands=['7В'])
def sevenV(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon8')
    Tue = types.KeyboardButton('/Tue8')
    Wed = types.KeyboardButton('/Wed8')
    Thur = types.KeyboardButton('/Thur8')
    Fri = types.KeyboardButton('/Fri8')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon8'])
    def MonSevV(message):
        photo = open('7вПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Tue8'])
    def TueSevV(message):
        photo = open('7вВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Wed8'])
    def WedSevV(message):
        photo = open('7вСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Thur8'])
    def ThurSevV(message):
        photo = open('7вЧт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Fri8'])
    def FriSevV(message):
        photo = open('7вПт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)






@bot.message_handler(commands=['7Г'])
def sevenG(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon9')
    Tue = types.KeyboardButton('/Tue9')
    Wed = types.KeyboardButton('/Wed9')
    Thur = types.KeyboardButton('/Thur9')
    Fri = types.KeyboardButton('/Fri9')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon9'])
    def MonSevG(message):
        photo = open('7гПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Tue9'])
    def TueSevG(message):
        photo = open('7гВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Wed9'])
    def WedSevG(message):
        photo = open('7гСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Thur9'])
    def ThurSevG(message):
        photo = open('7гЧт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Fri9'])
    def FriSevG(message):
        photo = open('7гПт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)






@bot.message_handler(commands=['8А'])
def eightA(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon10')
    Tue = types.KeyboardButton('/Tue10')
    Wed = types.KeyboardButton('/Wed10')
    Thur = types.KeyboardButton('/Thur10')
    Fri = types.KeyboardButton('/Fri10')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon10'])
    def MonEiA(message):
        photo = open('8аПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Tue10'])
    def TueEiA(message):
        photo = open('8аВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Wed10'])
    def WedEiA(message):
        photo = open('8аСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Thur10'])
    def ThurEiA(message):
        photo = open('8аЧт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)
    @bot.message_handler(commands=['Fri10'])
    def FriEiA(message):
        photo = open('8аПт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)






@bot.message_handler(commands=['8Б'])
def eightA(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    Mon = types.KeyboardButton('/Mon11')
    Tue = types.KeyboardButton('/Tue11')
    Wed = types.KeyboardButton('/Wed11')
    Thur = types.KeyboardButton('/Thur11')
    Fri = types.KeyboardButton('/Fri11')
    markup.add(Mon,Tue,Wed,Thur,Fri)
    bot.send_message(message.chat.id, 'Выбери день недели:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['Mon11'])
    def MonEiB(message):
        photo = open('8бПн.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id,'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Tue11'])
    def TueEiB(message):
        photo = open('8бВт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Wed11'])
    def WedEiB(message):
        photo = open('8бСр.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Thur11'])
    def ThurEiB(message):
        photo = open('8бЧт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание, но здесь могут быть неправильности...')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)

    @bot.message_handler(commands=['Fri11'])
    def FriEiB(message):
        photo = open('8бПт.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Вот твое расписание')
        bot.send_message(message.chat.id, 'Спасибо,за то что использовал бота,удачного дня!  <b>Напиши /start ,если хочешь поменять класс.</b>',parse_mode='html')
        photo1 = open('reakcii-v-telegram-1-696x348.jpg', 'rb')
        bot.send_photo(message.chat.id, photo1)






@bot.message_handler(commands=['raspisanie'])
def raspisanie(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    first = types.KeyboardButton('/1смена')
    second =types.KeyboardButton('/2смена')
    markup.add(first,second)
    bot.send_message(message.chat.id, 'Выбери смену:', parse_mode='html', reply_markup=markup)
    @bot.message_handler(commands=['1смена'])
    def firsta(message):
        photo1 = open('fista.png', 'rb')
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, 'Напиши /start если  хочешь узнать расписание.')
    @bot.message_handler(commands=['2смена'])
    def seconda(message):
        photo2 = open('seconda.png', 'rb')
        bot.send_photo(message.chat.id, photo2)
        bot.send_message(message.chat.id,'/start')





def delete(message):
    bot.delete_message(message.chat.id, message.message_id - 1)

bot.polling(none_stop=True)