def read_csv(filename: str) -> list:
    """
    
    This function takes in the name of a csv (string) and
    returns the header and the data of the file.

    Parameters
    ----------
    filename: str
        Name of file

    Returns
    ----------
    list, list
    
    list
        Header containing the column labels (from the first
        row)
    
    list
        Nested list of data from CSV

    Examples
    ----------
    >>> read_csv("grades.csv")
    ['grade', 'score']
    [['A', '70'],
     ['B', '60'],
     ['C', '55'],
     ['D', '50'],
     ['E', '45'],
     ['S', '40'],
     ['U', '0']]
    """
    with open(filename, "r") as f:
        header = f.readline().strip().split(',')
        data = []
      
        for line in f:
            newline = line.strip().split(',')
            newline[0] = int(newline[0])
            newline[3] = int(newline[3])
            data.append(newline)

    return header, data


def filter_gender(enrolment_by_age: list, sex: str) -> list:
    """
    
    This function takes a list of data and a string sex and
    returns a list of records where the value in the
    "sex" column matches string sex

    Parameters
    ----------
    enrolment_by_age: list
        list of records

    sex: str
        sex that is being looked for

    Returns
    -------
    list
        list of records where the value in the "sex"
        column matches string sex, excluding the sex column

    Examples
    --------
    >>> mf_enrolment = filter_gender(enrolment_data, "MF")
    >>> mf_enrolment
    [[1984, '17 YRS', 8710],
     [1984, '18 YRS', 3927],
     [...],
     [...],
     ...]
     
    >>> filter_gender(records, "Mr Surya")
    []
    """
    list = []
    for line in enrolment_by_age:
        if line[2] == sex:
            del line[2]
            list.append(line)
    return list


def sum_by_year(enrolment: list) -> list:
    """

    This function takes in a list of records and adds up the enrolment for each
    year, regardless of age. It returns a nested list where each list contains 2
    integers, year and total_enrolment.

    Parameters
    ----------
    enrolment: list
        list of records

    Returns
    -------
    list
        nested list where each list comprises two integers, year and total_enrolment

    Examples
    --------
    >>> enrolment_by_year = sum_by_year(mf_enrolment)
    >>> enrolment_by_year
    [[1984, 21471],
     [1985, 24699],
     [...],
     [...],
     ...]
    """
    current_year = enrolment[0][0]
    sum = [[current_year, 0]]
    for line in enrolment:
        if current_year == line[0]:
            sum[-1][1] += line[-1]
        else:
            current_year = line[0]
            sum.append([current_year, line[-1]])
    return sum


def write_csv(filename: str, header: list, data: list) -> int:
    """

    This function writes header and data to filename in CSV format and returns
    the number of lines written.

    Parameters
    ----------
    filename: str
        Name of file to be written into

    header: list
        Header of CSV file

    data: list
        Contents to be written into CSV file

    Returns
    -------
    int
        Number of lines written

    Examples
    --------
    >>> filename = 'total-enrolment-by-year.csv'
    >>> header = ["year", "total_enrolment"]
    >>> write_csv(filename, header, enrolment_by_year)
    35
    """
    with open(filename, "w") as f:
        header = ','.join(header) + '\n'
        loop = len(data[0])
        f.write(header)
        for line in data:
            for i in range(loop):
                line[i] = str(line[i])
            line = ",".join(line) + '\n'
            f.write(line)
          
    return len(data) + 1