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
