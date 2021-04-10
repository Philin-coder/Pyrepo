# Создать абстрактный класс «Издание» с методами, позволяющими вывести на экран информацию об издании, 
# а также определить является ли данное издание искомым. Создать производные классы: 
# Книга (название, фамилия автора, год издания, издательство), 
# Статья (название, фамилия автора, название журнала, его номер и год издания), 
# Электронный ресурс (название, фамилия автора, ссылка, аннотация) со своими методами вывода информации на экран. 
# Создать каталог (массив) из n изданий, вывести полную информацию из каталога, а также организовать поиск изданий 
# по фамилии автора.
 
from abc import ABC, abstractmethod
 
 
class Publication(ABC):
    
    @abstractmethod
    def get_info(self):
        print('Информация об издании...')
        
    def search(self, author):
        if author.lower() in self.author.lower():
            return True
        return False
 
 
class Book(Publication):
    
    def __init__(self, title, author, year_of_publication, publisher):
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.publisher = publisher
        
    def get_info(self):
        return ('Книга: "{}"\nАвтор: {}\nГод издания: {}\nИздательство: {}'.
              format(self.title, self.author, self.year_of_publication, self.publisher))
 
 
class Article(Publication):
    
    def __init__(self, title, author, magazine_title, magazine_number, year_of_publication):
        self.title = title
        self.author = author
        self.magazine_title = magazine_title
        self.magazine_number = magazine_number
        self.year_of_publication = year_of_publication
        
    def get_info(self):
        return ('Статья: "{}"\nАвтор: {}\n:Журнал "{}", {} за {} год'.
              format(self.title, self.author, self.magazine_title, self.magazine_number, self.year_of_publication))
 
 
class ElectronicResource(Publication):
    
    def __init__(self, title, author, url, annotation):
        self.title = title
        self.author = author
        self.url = url
        self.annotation = annotation
        
    def get_info(self):
        return ('Электронный ресурс: "{}"\nАвтор: {}\nСсылка: {}\nАннотация:\n{}'.
              format(self.title, self.author, self.url, self.annotation))
 
publications = []
 
publications.append(Book("Зов Ктулху", "Лавкрафт", "2020", "АСТ"))
publications.append(Book("Посторонний. Миф о Сизифе. Калигула", "Камю", "2015", "АСТ"))
 
publications.append(Article("Не SQL единым. Часть 1: в дебри key/value", 
                            "Сухов", 
                            "Системный администратор", 
                            "1-2 (110-111)", "2012"))
publications.append(Article("ERP-системы сегодня: кризис жанра или новые возможности?", 
                            "Жилин", 
                            "БИТ. Бизнес & Информационные технологии", 
                            "01 (104)", "2021"))
 
annotation = "Рассматривается возможность и условия возникновения локальных неоднородностей в \
пространстве Вселенной, а также их влияние на взаимодействие космических объектов."
url = "https://cyberleninka.ru/article/n/ustoychivye-lokalnye-neodnorodnosti-v-prostranstve-vselennoy/viewer"
publications.append(ElectronicResource("Устойчивые локальные неоднородности в пространстве Вселенной", 
                                       "Шахулов", 
                                       url, 
                                       annotation))
 
annotation = "Привет, я работаю инженером в КРОК, где у нас есть своя SD-WAN-лаборатория. И когда \
заказчик приходит с вопросами вроде «А вот у меня в сети сейчас всё работает так, а как это будет \
работать, если я захочу перейти на SD-WAN? И будет ли работать вообще?» мы можем быстро собрать \
нужную схему, оттестировать и показать."
publications.append(ElectronicResource("Аналитика в SD-WAN – как она выглядит и зачем нужна?", 
                                       "Сигачев", 
                                       "https://habr.com/ru/company/croc/blog/551648/", 
                                       annotation))
 
for publication in publications:
    print(publication.get_info())
    print()
    
search_word = "Камю"
print('Результаты поиска по запросу "{}": '.format(search_word))
for publication in publications:
    if publication.search(search_word):
        print(publication.get_info())
        print()