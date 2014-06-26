__author__ = 'JAWASSMACPRO'

#main 4chan API app

import requests
from bs4 import BeautifulSoup


def boardLIST():
    base_url = 'https://a.4cdn.org/boards.json'
    jawLIST = requests.request('get', base_url).json()
    #print(jawLIST)
    bLIST = jawLIST['boards']

    for i in range(len(bLIST)):
        genre = bLIST[i]
        print('Board Name: {} | /{}' .format(genre['title'], genre['board']))

    menu()

def boardPOSTS():
    base_url = 'https://a.4cdn.org/'
    boardPICK = str(input('Pick a board: '))
    pageNUM = str(input('Pick page number: '))
    final = base_url + boardPICK + '/' + pageNUM + '.json'
    jawchan = requests.request('get', final).json()

    #print(jawchan)
    threads = jawchan['threads']
    #print(threads)
    #print(len(threads))

    for i in range(len(threads)):
        #print(threads[i])
        POSTS = threads[i]['posts']
        print('---------------------------------------------------------------------------------')
        print(POSTS[0]['no'])
        print(POSTS[0]['now'])
        if 'com' in POSTS[0]:
            post = POSTS[0]['com']
            soup = BeautifulSoup(post)
            print(soup.get_text())
        print('Thread replies - {}' .format(POSTS[0]['replies']))

    menu()

def threadPOSTS():
    boardPICK = str(input('Pick a board: '))
    threadNUM = str(input('Pick Thread Number: '))
    base_url = 'https://a.4cdn.org/'
    final = base_url + boardPICK + '/thread/' + threadNUM + '.json'
    jawchan = requests.request('get', final).json()
    #print(jawchan)

    fullTHREAD = jawchan['posts']

    for i in range(len(fullTHREAD)):
        POSTS = fullTHREAD[i]
        print('----------------------------------------------------------------------------------')
        print('{} | {} ' .format(POSTS['no'], POSTS['now']))

        if 'com' in POSTS:
            post = POSTS['com']
            soup = BeautifulSoup(post)
            print(soup.get_text())

    menu()

def menu():
    print('------------------------------------------------')
    print('JAWCHAN')
    print('1 - Board List')
    print('2 - Board Posts')
    print('3 - Thread Review')
    print('4 - Exit')
    print('------------------------------------------------')

    u = int(input('Enter Option #: '))

    if u == 1:
        boardLIST()
    if u == 2:
        boardPOSTS()
    if u == 3:
        threadPOSTS()
    if u == 4:
        print('EXIT')
    else:
        print('FAIL')
        menu()

def main():
    print('JAWCHAN')
    print('------------------------------------------------')

    menu()

main()

