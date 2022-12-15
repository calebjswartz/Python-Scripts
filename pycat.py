import hashlib
from PyInquirer import prompt

list = []



# get user input
def choose_hash():
    questions = [
{
    'type': 'list', 
    'name': 'hash_choice',
    'message': 'Choose the hash algorithm to be used.',
    'choices': ['MD5', 'SHA1', 'SHA224', 'SHA256','SHA384', 'SHA512']
},
{
    'type': 'input',
    'name': 'sample',
    'message': 'Paste the hash here: '
}
]
    answer = prompt(questions,)
    hash_type = answer["hash_choice"]
    sample = answer["sample"]
    match(hash_type, sample)

def make_list():
    with open("rockyou.txt", "r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            list.append(line.rstrip('\n'))

def match(hash_type, sample):
    if hash_type == 'MD5':
        for i in list:
            test = hashlib.md5(i.encode('utf-8')).hexdigest()
            if test == sample:
                print("Match found:")
                print(i)
    elif hash_type == 'SHA1':
        for i in list:
            test = hashlib.sha1(i.encode('utf-8')).hexdigest()
            if test == sample:
                print(i)
    elif hash_type == 'SHA224':
        for i in list:
            test = hashlib.sha224(i.encode('utf-8')).hexdigest()
            if test == sample:
                print("Match found:")
                print(i)
    elif hash_type == 'SHA256':
        for i in list:
            test = hashlib.sha256(i.encode('utf-8')).hexdigest()
            if test == sample:
                print(i)
    elif hash_type == 'SHA384':
        for i in list:
            test = hashlib.sha384(i.encode('utf-8')).hexdigest()
            if test == sample:
                print("Match found:")
                print(i)
    elif hash_type == 'SHA512':
        for i in list:
            test = hashlib.sha512(i.encode('utf-8')).hexdigest()
            if test == sample:
                print("Match found:")
                print(i)


make_list()
choose_hash()

