import os


def scan_dir(path):
    file_count = 0
    catalog_count = 0
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_count += 1
        else:
            catalog_count += 1
            scan_dir(file_path)
    print('[', path, ']\n\t', 'files: %s' % file_count, 'catalogs: %s' % catalog_count)


if __name__ == '__main__':
    scan_dir(path=os.getcwd())
