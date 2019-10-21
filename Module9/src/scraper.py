"""
Program: scraper.py
Author: Wes Brown
Last date modified: 10/20/19

Purpose: Scraping a web page
"""

import requests

if __name__ == '__main__':
    url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=202001&Campus=4'
    response = requests.get(url)
    html = response.content
    file_out = open("requestResult.txt", "w+")
    file_out.writelines(str(html))
    file_out.close()
