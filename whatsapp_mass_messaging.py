"""

A Python code to to automate sending mass whatsapp messages.
The list of phone numbers is stored in moblie_no_list in list
 format.
The phone numbers are imported from test_numbers.csv file.
To automate web processes selenium is used. Make sure to install
 chrome web drivers to allow selenium to automate the web proces.
"""

__author__ = "Gustavo Martinez Licona"
__copyright__ = ""
__credits__ = ["Gustavo Martinez Licona"]
__license__ = "Apache License 2.0"
__version__ = "1.3.0"

from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv

message_text = ""

with open('hindi_message.txt') as hindi_file:
    for text in hindi_file:
        message_text += text
#  número de veces que quieres que se envíe el mensaje
no_var = ""
no_of_message = 1

# la lista de números de teléfono puede ser de cualquier longitud
moblie_no_list = []

# obtener el número de móvil del archivo csv
# colocar la lista de numeros
with open('prospectos.csv', 'r') as csvfile:
    moblie_no_list = [int(row[0])
                      for row in csv.reader(csvfile, delimiter=';')]
i = 52
newlist = [str(i) + str(v) for v in moblie_no_list]

for i in range(0, len(newlist)):
    newlist[i] = int(newlist[i])
# imprime l lista obtenida
print(newlist)




def element_presence(by, xpath, time):
    '''
    determina la presencia de controladores web
    en este caso el chromeDriver
    '''
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)


def is_connected():
    '''
    Regresa verdadero si el ping a www.google.com
    en el puerto 80 se ealiza correctamente
    '''
    try:
        # conectar con el host -- nos dice si el host es realmente alcanzable
        socket.create_connection(("www.google.com", 80))
        return True
    except BaseException:
        is_connected()


driver = webdriver.Chrome(executable_path="chromedriver")
driver.get("http://web.whatsapp.com")
# tiempo de espera para escanear el código en segundos
sleep(10)




def send_whatsapp_msg(phone_no, text):
    '''
    send_whatsapp_msg() acepta 2 argumentos - phone_no y texto entero y cadena respectivamente.
    Para los argumentos de las palabras clave, utilice send_whatsapp_msg(phone_no= ,test='').
    Se conecta a la web de whatsapp y toma precauciones para los números de móvil erróneos.
    Llama al método isConnected antes de esta función.
    '''

    driver.get(
        "https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no)
    )
    try:
        driver.switch_to_alert().accept()

    except Exception as e:
        pass

    try:
        element_presence(
            By.XPATH,
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
            30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message

        for x in range(no_of_message):
               # text
            txt_box.send_keys(text)
            txt_box.send_keys("\n")
            # IAMGE 1
            attachment_box = driver.find_element_by_xpath('//div[@title = "Adjuntar"]')
            attachment_box.click()
            image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            image_box.send_keys("/Users/gustavomartinezlicona/Documents/python/automatized_whatsapp_excel/imagen1.jpeg")
            sleep(3)
            send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
            send_button.click()
            attachment_box.send_keys(Keys.ENTER)
            #bajar el sleep a 5 , se hizo con 15 para velocidad de internet bajo
            sleep(3)
             # IAMGE 2
            attachment_box = driver.find_element_by_xpath('//div[@title = "Adjuntar"]')
            attachment_box.click()
            image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
            image_box.send_keys("/Users/gustavomartinezlicona/Documents/python/automatized_whatsapp_excel/imagen2.jpeg")
            sleep(3)
            send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
            send_button.click()
            attachment_box.send_keys(Keys.ENTER)
           #bajar el sleep a 5 , se hizo con 15 para velocidad de internet bajo
            sleep(3)
    except Exception as e:
        print("Invailid phone no :" + str(phone_no))


def main():
    '''
    Itera el número de móvil y lo envía
    a la funcion send_whatsapp_msg
    '''

    for moblie_no in newlist:
        try:
            send_whatsapp_msg(phone_no=moblie_no, text=message_text)

        except Exception as e:

            sleep(10)
            is_connected()


'''
print("functions- main, element_presence, is_connected, send_whatsapp_msg")
print("Docs")
print(main.__doc__)
print(element_presence.__doc__)
print(is_connected.__doc__)
print(send_whatsapp_msg.__doc__)
'''

if __name__ == '__main__':
    main()
