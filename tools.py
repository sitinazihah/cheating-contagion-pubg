from datetime import datetime, timedelta

def main():
    pass


def get_data(filename):
    '''Opens data in filename and returns a list of values.'''

    with open (filename, 'r') as f:
        data = []
        for line in f.readlines():
            data.append(line.strip().split('\t'))
    return data


def date_format(data):
    '''Converts data from string format to datetime format when data contains
    date only without time.'''

    return datetime.strptime(data, "%Y-%m-%d")


def datetime_format(data):
    '''Converts data from string format to datetime format when data contains
    date and time.'''

    return datetime.strptime(data, "%Y-%m-%d %H:%M:%S.%f")


def count_motifs(cheaters, kills):
    '''Given two lists of formatted values, i.e. cheaters and kills,
    returns the count of victims of cheaters who started to cheat
    within 5 days of getting killed by cheaters.'''

    count = 0
    # create a dictionary that maps cheaters to dates they started cheating
    cheaters_dic = {i:j for i,j,k in cheaters}
    for j in kills:
        try:
            # if killers are active cheaters and
            # their victims became cheaters within 5 days of getting killed
            if cheaters_dic[j[1]] < j[3] and\
            j[3] < cheaters_dic[j[2]] < j[3]+timedelta(days=5):
                count += 1

        except KeyError:
            continue
    return count


if __name__ == '__main__':
    main()
