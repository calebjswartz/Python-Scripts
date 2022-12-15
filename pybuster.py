import requests
import time

WORDLIST = "wordlist.txt"

def dir_bust():
    url = input("Enter url here: ")
    start_time = time.time() # start of timer
# copy word list to memory
    word_list = []
    with open(WORDLIST, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            word_list.append(line)
# test to see if directories are present
    up_list = []
    up_counter = 0
    for item in word_list:
        test_url = "http://" + url + "/" + item
        response = requests.get(test_url)
        if response.ok:
            up_list.append(test_url)
            up_counter += 1
# display results
    print(f"{up_counter} directories found.\n")
    for item in up_list:
        print(item)        
    time_elapsed = time.time() - start_time
    print("Time elapsed: %s seconds" % format(time_elapsed, '.2f'))
        
    
dir_bust()
