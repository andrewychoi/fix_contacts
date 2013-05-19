import csv
import string

def find_problems(filename = "google.csv"):

    with open(filename, 'rb') as readfile:
        contact_reader = csv.reader(readfile, delimiter = ",")

        for row in contact_reader:

            # if no total name, then ignore
            if not row[0]:
                continue
            # if no first name,
            if not row[1]:

                tokens = string.split(row[0])
                if len(tokens) == 2:

                    print row
                    row[1] = tokens[0]
                    row[3] = tokens[1]
                    
                    # remove prior groups
                    row[26] = ''



if __name__ == "__main__":
    find_problems()

def sanitize(filename = "google.csv"):
    fi = open(filename, 'rb')
    data = fi.read()
    fi.close()
    fo = open('sanitized_google.csv', 'wb')
    fo.write(data.replace('\x00', ''))
    fo.close()
