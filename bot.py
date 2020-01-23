import requests # библотека requests
from misc import token #импортируем токен
import json # импортируем модуль json
from yobit import get_btc #импортируем функцию получения url с валютой
# https://api.telegram.org/bot1080218380:AAGiJuCrrhER482gEkbTrrkx8UqwMU5ZSc8/sendmessage?chat_id=662122625&text=привет мир
URL = f"https://api.telegram.org/bot{token}/" #формируем глбольный url для отправки запросов к API телеграмма



global last_update_id #объявляем глобальную переменную
last_update_id = 0 # приравниваем ее к нулю



def get_update(): #функция получения обновлений от сервера телеграм
    url = URL + 'getupdates' #урл для получения обновлений
    r = requests.get(url) #получение ответа от сервера
    # print(r.json())
    return r.json() # возвращение данных в формате словаря пайтон



def get_message(): # функция получения сообщения от пользователя
    data = get_update() # словарь из функции get_update
    last_object = data['result'][-1] # последний объект в словаре data
    current_update_id = last_object['update_id'] # действующий id 
    global last_update_id #объявляем использование глобальной переменной
    if last_update_id != current_update_id: #если значение глобальной переменной не равно значению действующей выполняем действия
        last_update_id = current_update_id #приравниваем глобальную переменную к действующему айди
        chat_id = last_object['message']['chat']['id'] #получаем чат айди
        message_text = last_object['message']['text'] #получаем текст сообщения
        message = {
            'chat_id': chat_id,
            'message_text': message_text
        } # сформировали словарь с чат айди и текстом сообщения
        return message #возвращаем сформированный словарь
    return None #если не выполняется условие возвращаем ноне


def send_message(chat_id, message_text='Секундочку'): #функция отправки сообщения пользователю аргементы чат айди и текст со значением по умолчанию
    url = URL + f'sendmessage?chat_id={chat_id}&text={message_text}' #формируем урл с сообщением для ответа пользователю
    requests.get(url) #получаем ответ от сервера
    print(url) #принтим для проверки


def main(): #главная функция выполнения
    currency = ['btc', 'ltc', 'dash', 'doge', 'yovi', 'eth', 'lsk'] #список криптовалют 
    while True: #запускаем бесконечный цикл
        answer = get_message() #получаем последнее сообщение пользователя
        if answer != None: #проверяем что бы сообщение не было равно None
            chat_id = answer['chat_id'] #получаем текущий чат айди
            text = answer['message_text'].lower() #получаем текст текущего сообщения и приводим его к нижнему регистру
            if text in currency: #проверяем наличие текста сообщения в списке криптовалют
                send_message(chat_id, get_btc(text)) #отправляем необходимые данные пользователю согласно сформированному урлу
            else:
                continue # если данные не совпдают продолжаем выполнение цикла
        # sleep(2)




if __name__ == "__main__": #точка входя для запуска из консоли
    main()

