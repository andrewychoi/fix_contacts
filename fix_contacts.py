import csv
import string

def fix_contacts(filename = "sanitized_google.csv"):

    with open('sanitized_google.csv', 'rb') as readfile:
        contact_reader = csv.reader(readfile, delimiter = ",")

        with open('to_import.csv', 'wb') as writefile:
            contact_writer = csv.writer(writefile, delimiter = ",")
            first = True
            for row in contact_reader:
                if first:
                    # weird encoding errors
                    row[0] = "Name"
                    row[1] = "First Name"
                    row[3] = "Last Name"
                    contact_writer.writerow(row)
                    first = False                


                # if no total name, then ignore
                if not row[0]:
                    continue
                # if no first name,
                if not row[1]:

                    tokens = string.split(row[0])
                    if len(tokens) == 2:
                        row[1] = tokens[0]
                        row[3] = tokens[1]
                        
                        # remove prior groups
                        row[26] = ''

                        contact_writer.writerow(row)



if __name__ == "__main__":
    fix_contacts()

def sanitize(filename = "google.csv"):
    fi = open(filename, 'rb')
    data = fi.read()
    fi.close()
    fo = open('sanitized_google.csv', 'wb')
    fo.write(data.replace('\x00', ''))
    fo.close()
