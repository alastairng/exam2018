def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742
    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]
    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]
    """ 
    file_path = "./babynames/" + file_name
    with open(file_path) as f:
        baby_data = f.readlines()
        baby_data = [x.strip() for x in baby_data] 
    
    formatted_baby_data = []
    for data_point in baby_data:
        data_list = data_point.split(",")
        formatted_baby_data.append(data_list)

    return formatted_baby_data


def total_births(year):
    """
    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    file_name = "yob" + str(year) + ".txt"
    baby_data = process_file(file_name)
    total_births = 0
    for birth in baby_data:
        total_births += int(birth[2])
    return total_births


def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    file_name = "yob" + str(year) + ".txt"
    baby_data = process_file(file_name)

    total_births_with_that_name = 0
    for birth in baby_data:
        if birth[1] == gender:
            if birth[0] == name:
                total_births_with_that_name += int(birth[2])
    
    proportion = total_births_with_that_name/total_births(year)
    proportion = proportion * 100
    proportion = "{0:.2f}".format(round(proportion,2))
    return proportion
    


def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    year_range = range(1880, 2011)
    birth_dict = {}
    value_dict = {}
    for year in year_range:
        birth_dict[year] = proportion(name, gender, year)
    
    year_with_the_highest_percentage_of_births_with_name = max(birth_dict.keys(), key=(lambda k: birth_dict[k]))


    value_dict["year"] = year_with_the_highest_percentage_of_births_with_name
    value_dict["percentage"] = proportion(name, gender, year_with_the_highest_percentage_of_births_with_name)
    string = 'The highest proportion of births with the name' + ' ' + str(name) + ' ' + 'was' + ' ' + str(value_dict["year"]) + " with a percentage of " + str(value_dict["percentage"]) + "%"

    return string

def main():
    print(highest_year("John", "M"))
    print(highest_year("Sarah", "F"))
    print(highest_year("Zachary", "M"))
    print(highest_year("Maggie", "F"))
    print(highest_year("Alex", "M"))
    print(highest_year("Alastair", "M"))


if __name__ == '__main__':
    main()

