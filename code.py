import os, shutil, psutil, time, logging
from stat import *
from datetime import date
import re

logging.basicConfig(level=logging.INFO, filename="C:/Users/home-pc/VSProjects/py_log.log",filemode="a",
                    format="%(asctime)s %(funcName)s %(levelname)s %(message)s")


def list_dir():
    path_to_dir = input("Введите путь: [/n]")
    try:
        file_name = os.listdir(path_to_dir)
        for f in file_name:
            f_path = path_to_dir + '\\' + f
            file_info = os.stat(f_path).st_mode
            print(f, filemode(file_info))
            logging.info('dir was read')
    except:
        print('Нет такой директории')
        logging.warning('there is no such dir')
        list_dir()


def rem_file():
    path_to_dir = input("Введите путь для удаления: [/n] ")
    if os.path.exists(path_to_dir):
        question = input('Вы точно хотите удалить файл?[Y/N] ')
        if question == 'Y':
            os.remove(path_to_dir)
            print('Вы удалили файл')
            logging.info('File was delited')
        else:
            print('Файл не был удалён')
            logging.info('File was not delited')
    else:
       print('Нет такого файла')
       logging.warning('there is no such dir')


def backup():
    path_to_dir = input("Введите путь для директории: [/n] ")
    if not os.path.exists(path_to_dir): 
        print("нет такой директории")
        logging.warning('there is no such dir')
    today = date.today()
    pattern = '\w+$'
    name = re.findall(pattern, path_to_dir)
    date_format = today.strftime("%d_%b_%Y")
    dst_dir = 'C:/Users/home-pc/Downloads/Backup/' + str(*name) +date_format
    shutil.make_archive(dst_dir, 'zip', path_to_dir)
    print('Копирование выполнено')
    logging.info('backup is done')
def memory(timer):
    a = ['w']*7
    percent = psutil.virtual_memory().percent
    while True:
        f = open('C:/Users/home-pc/Desktop/Test/memory.txt', 'a')
        # RAM
        ram_info = psutil.virtual_memory()
        a[0] = f"Total RAM: {ram_info.total / (1024 * 1024 * 1024):.2f} GB"
        a[1] = f"Available RAM: {ram_info.available / (1024 * 1024 * 1024):.2f} GB"
        a[2] = f"Used RAM: {ram_info.used / (1024 * 1024 * 1024):.2f} GB"
        a[3] = f"Percentage usage RAM: {ram_info.percent}%"
        # DISK
        disk_info = psutil.disk_usage('/')
        a[4] = f"Total Disk: {disk_info.total / (1024 * 1024 * 1024):.2f} GB"
        a[5] = f"Available Disk: {disk_info.free / (1024 * 1024 * 1024):.2f} GB"
        a[6] = f"Total Disk: {disk_info.used / (1024 * 1024 * 1024):.2f} GB"
        for i in range(len(a)):
            if i == 0:
                f.write('RAM info \n')
            elif i == 4:
                f.write('Disk info \n')
            f.write(a[i])
            f.write('\n')
        print('Данные записаны в файл memory')
        if abs(ram_info.percent - percent) > 5:
            print('Разница между RAM больше 5%')
            logging.warning('Difference between RAM is more than 5%')
            return 
        percent = ram_info.percent
        logging.info('Info was written to the file memory')
        time.sleep(timer)


print('1 - прочитать содержимое директории\n2 - удалить файл\n3 - сделать резервное копирование\n4 - узнаить информацию о системе')

a = input("What you want to do: ")
if a == '1':
    list_dir()
elif a == '2':
    rem_file()
elif a == '3':
    backup()
elif a == '4':
    timer = int(input('Введите переодичность [сек]: '))
    memory(timer)
