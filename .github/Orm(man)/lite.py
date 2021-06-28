from sqlalchemy import  create_engine

engine = create_engine('sqlite:///sqlite3.db')  # используя относительный путь
engine = create_engine('sqlite:////path/to/sqlite3.db')  # абсолютный путь

