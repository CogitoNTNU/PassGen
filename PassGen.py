from random import randint, shuffle, sample
import argparse

def main():
    spCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", ":", ";", "<", ">", "?", "/", "~", "|"]
    wordList = []
    with open("filtered.txt", "r") as file:
        for line in file:
            wordList.append(line.strip())
            
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", help="Number of words to generate default is 4", type=int, default=4)
    parser.add_argument("-n", help="Number of numbers to generate default is 2", type=int, default=2)
    parser.add_argument("-s", help="Number of special characters to generate default is 2", type=int, default=2)
    parser.add_argument("-c", help="Minimum number of capital letters to generate default is 1, larger values than w will get same result as w", type=int, default=1)
    parser.add_argument("-i", help="Number of iterations to generate passwords default is 1", type=int, default=1)

    args = parser.parse_args()
    for i in range(args.i):
        words = [wordList[x] for x in sample(range(len(wordList)), args.w)]
        numbers = [str(randint(0, 9)) for y in range(args.n) ] 
        characters = [spCharacters[randint(0, len(spCharacters) - 1)] for z in range(args.s) ]
        
        # start by capitalizing random words
        if args.c > 0 and args.c <= args.w:
            for i in sample(range(len(words)), args.c):
                words[i] = words[i].capitalize()
        else:
            words = [word.capitalize() for word in words]
            
        # combine all the lists and shuffle them
        password = words + numbers + characters
        
        # for readability, shuffle the password such that each word is split by at least one number, special character or the next word has a capital letter
        while True:
            shuffle(password)
            # mark the indexes of the words
            wordIndexes = [i for i in range(len(password)) if len(password[i]) > 1]
            # last word doesnt need to be checked
            count = 0
            for i in range(len(wordIndexes) - 1):
                # if the next word is not bordering the next word
                if wordIndexes[i] + 1 not in wordIndexes:
                    count += 1
                # if the next word bordering next word
                else:
                    # and the next word is capitalized
                    if password[wordIndexes[i+1]][0].isupper():
                        count += 1
                
            # all checked words pass the test escape the loop
            if count == len(wordIndexes) - 1:
                break
            
        print("".join(password))

if __name__ == "__main__":
    main()