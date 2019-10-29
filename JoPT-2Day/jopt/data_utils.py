import re

def list_to_str(in_list, delimiter=','):
    return delimiter.join([str(i) for i in in_list])


def csv_str_to_list(csv_str, delimiter=','):
    return csv_str.split(delimiter)


def convert_to_map(seq1, seq2):
    return dict(zip(seq1, seq2))


def extract_email_parts(email_address):
    pattern = r'(\w+)@(.*)'
    match = re.match(pattern, email_address)
    if match:
        return match.groups()
    else:
        raise Exception("{} is not an email".format(email_address))
