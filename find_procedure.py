import glob
import os.path

##  INSERT
##  APPLICATION_SETUP
##  A400M
##  0.0
##  2.0

migrations = 'Migrations'
files = glob.glob(os.path.join(migrations, "*.sql"))

while True:
    request = input('Введите строку: ')
    files_list = []
    number_of_files = 0
    for file in files:
        with open(file, 'r') as f:
            if request in f.read():
                print(file)
                number_of_files += 1
                files_list.append(file)
    print('Всего: {}\n'.format(number_of_files))
    files = files_list

        

