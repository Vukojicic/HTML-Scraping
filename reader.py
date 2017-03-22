#!/usr/bin/python -tt

import sys

def sort_by_value(item):
    return item[-1]

def build_dict(filename):
    f = open(filename, 'rU')
    words = f.read().split()
    count = {}

    for word in words:
        word = word.lower()
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    f.close()

    return count

def print_words(filename):
    dict = build_dict(filename)

    for word in sorted(dict.keys()):
        print word, dict[word]

def print_top(filename):
    count = build_dict(filename)
    i = 0

    items = sorted(count.items(), key=sort_by_value, reverse=True)
    for item in items[:20]:
        print item[0] + ': ' + str(item[1]) + ' times'
        i += 1

def write_f(filename):
	f = open("New.txt" , "a")
	dict = build_dict(filename)

	for word in dict:
		f.write(word + ": " +str(dict[word]) + ' times' + '\n')

	f.close()


def write_s(filename):
	f=open("Newsorted.txt" , "a")
	dict = build_dict(filename)

	items = sorted(dict.items(), key=sort_by_value, reverse=True)
	i=0

	for item in items:
		f.write(item[0] + ': ' + str(item[1]) + ' times' + '\n')
		i += 1

	f.close()




def main():
    if len(sys.argv) != 3:
        print 'usage: ./reader.py { --writesorted | --write | --count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
      print_words(filename)
    elif option == '--topcount':
      print_top(filename)
    elif option == '--write':
    	write_f(filename)
    elif option == '--writesorted':
    	write_s(filename)
    else:
      print 'unknown option: ' + option

    sys.exit(1)

   

if __name__ == '__main__':
    main()
