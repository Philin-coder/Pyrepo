print(posts.columns)         # вернуть список колонок
print(posts.c)               # как и post.columns
print(posts.foreign_keys)    # возвращает множество, содержащий внешние ключи таблицы
print(posts.primary_key)     # возвращает первичный ключ таблицы
print(posts.metadata)        # получим объект MetaData из таблицы
print(posts.columns.post_title.name)     # возвращает название колонки
print(posts.columns.post_title.type)     # возвращает тип колонки

