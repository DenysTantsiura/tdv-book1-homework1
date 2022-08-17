#...!
'''Задача 1
Создайте собственную программу «Адресная книга», 
работающую из командной строки и позволяющую просматривать, 
добавлять, изменять, удалять или искать контактные
данные ваших знакомых. Кроме того, эта информация также 
должна сохраняться на диске для последующего доступа.
Задача 2
Реализуйте команду replace. Эта команда заменяет одну 
строку другой в списке переданных ей файлов.'''

import os, sys, pickle

class ContactItem():
    def __init__(self):
        self.fields = []
    
    def add(self, field_item):
        self.fields.append(field_item)  

    def delete(self, idx):
        idx = int(idx)
        self.fields.pop(idx)

    def update(self, idx, value):
        idx = int(idx)
        self.fields[idx] = value

class DataField(ContactItem):  #### DataField:
    field_description = "General"

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.field_description}:{self.value}"

class FirstNameField(DataField):   
    field_description = "Name"   

class PhoneField(DataField):  
    field_description = "Phone"         

# developer1 = Developer()
# developer1.add(FirstNameField("Vlad"))
# developer1.add(CityField("Kyiv"))

def FunP1_tryOpenFile(varPathFile, storedlist = []):
    if os.path.isfile(varPathFile):
        None
        # f = open(varPathFile, 'rb')
        # storedlist = pickle.load(f) # загружаем объект из файла
    else:
        print('Unable to find ',varPathFile,' file')
        print('Free-fill file will be created')
        # varAnsAFile = open(varPathFile,'w', encoding="utf-8")
        # varAnsAFile.close()
        with open(varPathFile, "ab") as varWordsFile:
            #varWordsFile.write("hello")
            #storedlist = []
            pickle.dump(storedlist, varWordsFile)
    return varPathFile #storedlist

def FunCorrector1(var_answer0 = None):
    try:
        var_answer0 = int(input())
    except ValueError:
        print("incorrectly input\nPlease try again (or 0 for exit):")
        var_answer0 = FunCorrector1(var_answer0)
    return var_answer0

def FunViewer():
    developer1 = FunCOpener()[0]
    for i in developer1:
        print(i.fields[0])
    #print(MContactList)#time!


    FunMyMenu()###### time to change
    return 3

def FunCreator(var_nsw: list):
    print("You must input Name, and Phone\n")
    Name = input("Enter the Name: ")#add try!
    phone = input("Enter the phone: ")#add try!
    developer1 = var_nsw ##.fields
    if type(developer1) != type(ContactItem()):
        developer1 = ContactItem()
    developer1.add(FirstNameField(Name))
    developer1.add(PhoneField(phone))
    with open(var_nsw[1], "ab") as varWordsFile:
        #varWordsFile.write("hello")
        #storedlist = []
        pickle.dump(developer1, varWordsFile)
    print(var_nsw[0])##time
    print(developer1)##time
    print(var_nsw[0] + [developer1])##time
    return 1

def FunCOpener():
    MContactList = FunP1_tryOpenFile('ABook.txt')
    print(MContactList)#time!
    print(type(MContactList))#time!
    f = open(MContactList, 'rb')
    storedlist = pickle.load(f) # загружаем объект из файла
    print(storedlist, 'ABook.txt')##time
    return [storedlist, 'ABook.txt'] #MContactList

# f = open(shoplistfile, 'rb')
# storedlist = pickle.load(f) # загружаем объект из файла
#    return 3

def FunCensor(var_nsw = 3, var_type = 0):
    # if var_nsw == 0:
    # sys.exit()
    while var_nsw != 0:
        if var_type == 0:
            if var_nsw == 1:
                var_nsw = FunViewer()
            elif var_nsw == 2:
                var_nsw = FunCreator(FunCOpener())
            else:
                print("incorrectly input\nPlease try again (or 0 for exit):")
                var_nsw = FunCensor(FunCorrector1(var_nsw))
    else:
        sys.exit()
    # return var_nsw

def FunMyMenu():
    print("Menu:\n1) Find info\n2) Addition new contact\n0) Exit\n")
    var_answer0 = FunCorrector1()
    FunCensor(var_answer0)


def FuncInit1():
    print("Hello! Welcome to simple program address-book\n \
        Set your choice what to do:")
    FunMyMenu()


def main():
    FuncInit1()

if __name__ == "__main__":
    main()

# developer1 = {'Name': 'Denys',  'City': 'Kyiv', 'Skill': 'Python', 'Rate': 600,'Phone': '+380631234573'}
# developer2 = {'Name':'Peter','City': 'Kyiv','Skill': 'Python','Rate': 1800,'Phone': '+380631234567'}
# developer3 = {'Name': 'Vlad',  'City': 'Kyiv', 'Skill': 'Python', 'Rate': 1300, 'Phone': '+380631234570'}
# developer4 = {'Name': 'Ivan',  'City': 'Kyiv', 'Skill': 'Python', 'Rate': 2800, 'Phone': '+380631234572'}
# developer5 = {'Name': 'Alex',  'City': 'Lviv', 'Skill': 'Python', 'Rate': 4800, 'Phone': '+380631234574'}

# devs = [developer1, developer2, developer3, developer4, developer5]


# def get_rate_stat(developers):
#     rates = []
#     stat = {"mean": None, "min": None, "max": None, "item_number": 0}
    
#     for developer in developers:
#         rate = developer["Rate"]
#         rates.append(rate)

#     stat.update(
#         {
#          'mean': sum(rates),   
#          'min': min(rates),   
#          'max': max(rates),  
#          'item_number': len(rates)  
#         }
#     )
#     return stat

# for i,k in get_rate_stat(devs):
#     print(k)