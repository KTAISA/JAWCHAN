__author__ = 'JAWASSMACPRO'

#main 4chan API app

import requests


def boardLIST():
    base_url = 'https://a.4cdn.org/boards.json'
    jawLIST = requests.request('get', base_url).json()
    print(jawLIST)
    bLIST = jawLIST['boards']

    for i in range(len(bLIST)):
        genre = bLIST[i]
        print('Board Name: {} | /{}' .format(genre['title'], genre['board']))

def boardPOSTS():
    base_url = 'https://a.4cdn.org/g/1.json'
    jawchan = requests.request('get', base_url).json()

    #print(jawchan)
    threads = jawchan['threads']
    #print(threads)
    print(len(threads))

    for i in range(len(threads)):
        #print(threads[i])
        POSTS = threads[i]['posts']

        print(POSTS[0]['no'])
        print(POSTS[0]['now'])
        print(POSTS[0]['com'])
        print(POSTS[0]['replies'])

def menu():
    print('------------------------------------------------')
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

