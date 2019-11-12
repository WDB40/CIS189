"""
Program: file_driver.py
Author: Wes Brown
Last date modified: 11/11/19

Purpose: Testing the csv file reading for the county class
"""

import csv
from Module12.src.County import County


def read_csv_file(file_path):
    counties = {}

    with open("..\\files\\Iowa 2010 Census Data Population Income.csv") as my_file:
        csv_reader = csv.reader(my_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue

            try:
                county = County(row[1], row[0], row[2], row[3], row[4], row[5], row[6])
                counties[county.name] = county
            except TypeError:
                print(f"Skipped County: {row[1]}")

    return counties


def average_household_size(data_set, county_name):
    county = data_set.get(county_name)
    return county.population / county.num_households


def total_population(data_set):
    total = 0
    for key, county in data_set.items():
        total += county.population

    return total


if __name__ == '__main__':
    des_moines_counties = read_csv_file("..\\files\\Iowa 2010 Census Data Population Income.csv")
    print(f"Average Household Size in Dallas County: {average_household_size(des_moines_counties, 'Dallas'):.2f}")
    print(f"Total Iowa Population: {total_population(des_moines_counties)}")
