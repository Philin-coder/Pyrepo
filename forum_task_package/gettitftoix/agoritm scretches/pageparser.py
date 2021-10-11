
# import shutil  # no
# import bs4  # no
# import sys  # no
# from bs4 import BeautifulSoup  # no
# import os
# from urllib.request import urlopen  # no

# from email.mime.multipart import MIMEMultipart  #
# from email.mime.base import MIMEBase  #
# from email import encoders  #
# import lxml.html  #
# import time  #

# def m_parser(url, my_filename):
#     f = my_html = urlopen(url)
#     sp = BeautifulSoup(my_html, "html.parser")
#     lnk = sp.findAll("a", class_="playlist-btn-down")
#     os.mkdir(f_name)
#     os.chdir(os.get_cwd() + '\\' + f_name + '\\')
#     # char = "'"
#     for lt in lnk:
#         lt = str(lt)
#         lt = lt.replace('"', ' ')
#         lt = lt.replace('<a class=', ' ')
#         lt = lt.replace('playlist-btn-down no-a_j_a_xy', '')
#         lt = lt.replace('\'', '')
#         lt = lt.replace('target= _blank  title= скачать >(скачать)</a>', ' ')
#         lt = lt.replace('download', 'listen')
#         lt = lt.replace('href=', ' ')
#         linklist.append(lt)
#         print(linklist)
#     with open(my_filename + '.' + fl_ext2, 'w', encoding='utf-8') as fp:
#         print(*linklist, file=fp, sep="\n")
#         fp.close()
#     return linklist
#
#
# def reader(what_to_read):
#     with open(what_to_read + '.' + f_ext2, 'r', encoding='utf-8') as fp1:
#         play_list = []
#         f_str = ''
#         play_list = fp1.readline()
#         print('список песен')
#         for c in range(len(play_list)):
#             time.sleep(2)
#             f_str = f_str.replace(f_str, play_list[c])
#             print(f_str)
#
#
# if __name__ == '__main__':
#     f_name = str(input("название папки" + ' '))
#     my_filename = str(input("введите имя файла" + ' '))
#     what_to_read = my_filename
#     linklist = []
#     m_parser(url, my_filename)
#     reader(what_to_read)
