MONTHS_IN_YEARS = 12


def convert_to_months(months):
    years = months / MONTHS_IN_YEARS
    return years


if __name__ == '__main__':
    age_in_months = input("Enter the age in months (3-72)")
    age_in_years = convert_to_months(int(age_in_months))
    print(str(age_in_months) + " months is equal to " + str(age_in_years) + " years.")
