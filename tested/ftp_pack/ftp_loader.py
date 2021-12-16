import ftplib


def ftp_func(host: str, user: str, pass_w: str, filename: str):
    """
    Загрузка файла на фтп
    :param host: имя хосинга
    :param user: имя пользователя
    :param pass_w: пароль
    :param filename:имя файла
    :return:код состояния код состояния(успешна ли отправка).
    Образец вызова ftp_func(host='my_host', user='root', pass_w='pass_w', filename='my.png')
    """
    if isinstance(host, str) and isinstance(user, str) and isinstance(pass_w, str) and isinstance(filename,
                                                                                                  str) and host != '' \
            and user != '' and pass_w != '':
        con = ftplib.FTP(host, user, pass_w)
        fp = open(filename, "rb")
        con.storbinary("ST" + filename, fp)
        con.close()
        stat_code = 'file_loaded'
        return stat_code

    else:
        raise TypeError('передан неверный тип данных')
