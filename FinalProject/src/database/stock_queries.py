# STOCK BASE TABLE QUERIES
stock_base_table_query = """CREATE TABLE IF NOT EXISTS stock_base (
                            ticker TEXT PRIMARY KEY,
                            name TEXT NOT NULL,
                            last_price REAL NOT NULL);"""

insert_stock_base_query = """INSERT INTO stock_base(ticker, name, last_price)
                                VALUES(?, ?, ?);"""

view_all_base_stock_query = """SELECT * FROM stock_base;"""

# RECENT EARNINGS QUERIES
recent_earnings_table_query = """CREATE TABLE IF NOT EXISTS recent_earnings (
                                    ticker TEXT PRIMARY KEY,
                                    earnings REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_recent_earnings_query = """INSERT INTO recent_earnings(ticker, earnings, rank)
                                        VALUES(?, ?, ?);"""

view_all_recent_earnings_query = """SELECT * FROM recent_earnings;"""

# PAST YEAR EARNINGS QUERIES
past_year_earnings_table_query = """CREATE TABLE IF NOT EXISTS past_year_earnings (
                                    ticker TEXT PRIMARY KEY,
                                    earnings REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_past_year_earnings_query = """INSERT INTO past_year_earnings(ticker, earnings, rank)
                                        VALUES(?, ?, ?);"""

view_all_past_year_earnings_query = """SELECT * FROM past_year_earnings;"""

# P/E RATIO QUERIES
pe_ratio_table_query = """CREATE TABLE IF NOT EXISTS pe_ratio (
                                    ticker TEXT PRIMARY KEY,
                                    ratio REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_pe_ratio_query = """INSERT INTO pe_ratio(ticker, ratio, rank)
                                        VALUES(?, ?, ?);"""

view_all_pe_ratio_query = """SELECT * FROM pe_ratio;"""

# 5 YEAR REV QUERIES
five_year_rev_table_query = """CREATE TABLE IF NOT EXISTS five_year_rev (
                                    ticker TEXT PRIMARY KEY,
                                    rev REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_five_year_rev_query = """INSERT INTO five_year_rev (ticker, rev, rank)
                                        VALUES(?, ?, ?);"""

view_all_five_year_rev_query = """SELECT * FROM five_year_rev;"""

# 5 YEAR EARNINGS QUERIES
five_year_earnings_table_query = """CREATE TABLE IF NOT EXISTS five_year_earnings (
                                    ticker TEXT PRIMARY KEY,
                                    earnings REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_five_year_earnings_query = """INSERT INTO five_year_earnings (ticker, earnings, rank)
                                        VALUES(?, ?, ?);"""

view_all_five_year_earnings_query = """SELECT * FROM five_year_earnings;"""

# 5 YEAR DIVIDEND QUERIES
five_year_div_table_query = """CREATE TABLE IF NOT EXISTS five_year_div (
                                    ticker TEXT PRIMARY KEY,
                                    div REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_five_year_div_query = """INSERT INTO five_year_div (ticker, div, rank)
                                        VALUES(?, ?, ?);"""

view_all_five_year_div_query = """SELECT * FROM five_year_div;"""

# DIVIDEND YIELD QUERIES
div_yield_table_query = """CREATE TABLE IF NOT EXISTS div_yield (
                                    ticker TEXT PRIMARY KEY,
                                    div REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_div_yield_query = """INSERT INTO div_yield (ticker, div, rank)
                                        VALUES(?, ?, ?);"""

view_all_div_yield_query = """SELECT * FROM div_yield;"""

# PRICE/BOOK QUERIES
price_book_table_query = """CREATE TABLE IF NOT EXISTS price_book (
                                    ticker TEXT PRIMARY KEY,
                                    ratio REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_price_book_query = """INSERT INTO price_book (ticker, ratio, rank)
                                        VALUES(?, ?, ?);"""

view_all_price_book_query = """SELECT * FROM price_book;"""

# PRICE/SALES QUERIES
price_sales_table_query = """CREATE TABLE IF NOT EXISTS price_sales (
                                    ticker TEXT PRIMARY KEY,
                                    ratio REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_price_sales_query = """INSERT INTO price_sales (ticker, ratio, rank)
                                        VALUES(?, ?, ?);"""

view_all_price_sales_query = """SELECT * FROM price_sales;"""

# MARKET CAP QUERIES
market_cap_table_query = """CREATE TABLE IF NOT EXISTS market_cap (
                                    ticker TEXT PRIMARY KEY,
                                    market_cap REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_market_cap_query = """INSERT INTO market_cap (ticker, market_cap, rank)
                                        VALUES(?, ?, ?);"""

view_all_market_cap_query = """SELECT * FROM market_cap;"""

# VOLUME QUERIES
volume_table_query = """CREATE TABLE IF NOT EXISTS volume (
                                    ticker TEXT PRIMARY KEY,
                                    volume REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_volume_query = """INSERT INTO volume (ticker, volume, rank)
                                        VALUES(?, ?, ?);"""

view_all_volume_query = """SELECT * FROM volume;"""

# INCOME QUERIES
income_table_query = """CREATE TABLE IF NOT EXISTS income (
                                    ticker TEXT PRIMARY KEY,
                                    income REAL NOT NULL,
                                    rank INT NOT NULL);"""

insert_income_query = """INSERT INTO income (ticker, income, rank)
                                        VALUES(?, ?, ?);"""

view_all_income_query = """SELECT * FROM income;"""
