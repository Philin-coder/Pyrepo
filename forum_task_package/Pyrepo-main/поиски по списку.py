def filtren():
    mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']
    zolushka = list(filter(lambda x: x == 'мак', mixed))
    print(zolushka)


if __name__ == '__main__':
    filtren()
