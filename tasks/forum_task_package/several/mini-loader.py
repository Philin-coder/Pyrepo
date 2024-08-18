import dropbox


def loader(tks):
    print(tks)
    tk = dropbox.Dropbox(tks)
    wf = 'working-draft.txt'  # файл
    wd = '/upload.working-draft.txt'  # на дропбокс он называется...
    fp = open(wf, 'rb')
    response = tk.files_upload(fp.read(), wd)
    print('uploaded:', response)
    fp.close()


if __name__ == '__main__':
    loader(tks='')
