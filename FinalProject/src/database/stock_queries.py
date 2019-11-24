# STOCK BASE TABLE QUERIES
stock_base_table_query = """CREATE TABLE IF NOT EXISTS stock_base (
                            ticker TEXT PRIMARY KEY,
                            name TEXT NOT NULL,
                            last_price REAL NOT NULL);"""

insert_stock_base_query = """INSERT INTO stock_base(ticker, name, last_price)
                                VALUES(?, ?, ?);"""

view_all_base_stock_query = """SELECT * FROM stock_base;"""

