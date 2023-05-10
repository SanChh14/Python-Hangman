import os
import random
import msvcrt
import time
def cls():
    os.system('cls')
space='               '
while True:
    incorrect=('O','|','/','\\','/','\\')
    correct=[' ',' ',' ',' ',' ',' ']
    life=1
    f=open("words.txt",encoding="utf8")
    words=list()
    for x in f:
        x=x.rstrip()
        words.append(x)
    f.close()
    while True:
        line=random.randint(0,len(words))
        word=words[line]
        word=word.upper()
        if len(word)>6:
            break
    wordlen=len(word)
    known=list()
    for x in range(0,wordlen-4):
        while True:
            check=0
            y=random.randint(0,wordlen-1)
            for i in range(0,x):
                if y==known[i]:
                    check=1
            if check==0:
                break
        known.append(y)
    known.sort()
    kword="_"*wordlen
    totalalpha=list()
    for x in range(0,26):
        totalalpha.append(chr(65+x))
    while True:
        cls()
        pos=0
        for x in range(0,wordlen):
            if x == known[pos]:
                kword=kword[0:x]+word[x]+kword[x+1:wordlen]
                pos=pos+1
                if pos == len(known):
                    break
        print(space+'       HangMan')
        print(space+'       _______')
        print(space+'          |')
        print(space+'          '+correct[0])
        print(space+'         '+correct[2]+correct[1]+correct[3])
        print(space+'         '+correct[4]+' '+correct[5])
        print('\n\n')
        kwordsplit=list(kword)
        kwordsplit=' '.join(kwordsplit)
        print(space+'       '+kwordsplit)
        print('\n\n')
        print(space+'       Pick any:\n')
        print(space+'       '+' '.join(totalalpha))
        if life==7:
            print('')
            print(space+'       The answer is '+word+'\n')
            print(space+'       Game Over')
            break
        if kword==word:
            print('')
            print(space+'       Congratulations! You won.')
            break
        letter=msvcrt.getch().decode("utf-8")
        available=0
        for x in totalalpha:
            if letter == x or chr(ord(letter)-32) == x:
                available=1
        if available==1:
            for z in range(0,26):
                if letter == totalalpha[z] or chr(ord(letter)-32) == totalalpha[z]:
                    totalalpha[z]=' '
            pos=0
            found=0
            check=0
            for x in range(0,wordlen):
                if letter == word[x] or chr(ord(letter)-32) == word[x]:
                    check=0
                    for y in known:
                        if x == y:
                            check=1
                    if check==0:
                        found=1
                        known.append(x)
                        known.sort()
            if found==0:
                for x in range(0,life):
                    correct[x]=incorrect[x]
                print('')
                print(space+'       Wrong!')
                time.sleep(0.2)
                life=life+1
            else:
                print('')
                print(space+'       Correct!')
                time.sleep(0.2)
        else:
            print('')
            print(space+'       Input not available!')
            time.sleep(0.2)
    print('')
    print(space+'       Do you want to play again?(y/n)')
    again=msvcrt.getch().decode("utf-8")
    if again == 'n' or again == 'N':
        break
