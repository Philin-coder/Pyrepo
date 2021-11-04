import os


class Deposit(object):
    """
        :param naim: имя.
        :param nom_s: серия,номер паспорта.
        :param sum_year: сумма вклада в год.
        :param y_r: Год.
        """

    def __init__(self, naim, nom_s, sum_year, y_r):
        self.naim = naim
        self.nom_s = nom_s
        self.sum_year = sum_year
        self.y_r = y_r

    def __repr__(self):
        if isinstance(self.naim, str) and isinstance(self.nom_s, int) and isinstance(self.sum_year,
                                                                                     float) and isinstance(self.y_r,
                                                                                                           int):
            return repr(f'{self.naim, self.nom_s, self.sum_year, self.y_r}').__str__().replace('\"', '')
        else:
            raise TypeError('Передан неверный тип данных')

    def gen_cont(self) -> [list]:
        """
        :return: список полей классы.
        """
        fields = [self.naim, self.nom_s, self.sum_year, self.y_r]
        if isinstance(fields, list):
            return fields
        else:
            raise TypeError('wrong  data type')

    @staticmethod
    def write_to_file(file_name: str, f_ext: str, ls_data: list) -> str:
        """
        :param file_name: имя файла.
        :param f_ext: расширение.
        :param ls_data:  Данные, которое будут записаны в файл.
        :return: Данные, которое будут записаны в файл.
        """
        if isinstance(f_ext, str) and isinstance(ls_data, list) and f_ext == 'txt':
            with open(file_name + '.' + f_ext, 'a', encoding='utf-8') as fp:
                print(ls_data, file=fp, sep="\n")
            stat_code = 'file_created'
            return stat_code
        else:
            raise ValueError('Файл имеет неверное расширение')

    @staticmethod
    def file_reader(file_name: str, f_ext: str) -> list:
        """
        :param file_name:Имя файла.
        :param f_ext: расширение.
        :return: Данные, которое будут считаны из файла.
        """
        if os.path.exists(file_name + '.' + f_ext):
            try:
                with open(file_name + '.' + f_ext, 'r', encoding='utf-8') as fp:
                    data = fp.readlines()
                print(data)
                stat_code = 'file_read'
                return stat_code
            except FileNotFoundError:
                raise FileNotFoundError('Файл не найден')
        else:
            raise FileNotFoundError('это  не файл')

    @staticmethod
    def sorting(data: list) -> list:
        """
        :param data: исходный список
        :return: отсортированный список.
        """

        if data is not None:
            s_data = sorted(data)
            for i in range(len(s_data)):
                j = i
                while s_data[j - 1] > s_data[i] and j > 0:
                    s_data[j] = s_data[j - 1]
                    j -= 1
                    s_data[j] = s_data[i]
                return s_data
        else:
            raise TypeError('Передан неверный тип данных')
