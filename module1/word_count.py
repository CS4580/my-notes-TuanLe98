"""Read file from web and do analysis of data"""

from urllib.request import urlopen

def count_words_from_web(file_address):
    words = 0

    with urlopen(file_address) as data:
        for line in data:
            line = line.decode('utf-8') #convert bytes to string
            line_words = line.split()
           
            for word in line_words:
                words=words+1
                
    return words
def main():
    """Driven function"""
    # TODO:Read file from web
    file_address = 'https://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    # TODO: Count number of words
    total_words = count_words_from_web(file_address)
    print(f'There are a total of {total_words} words in the file')

if __name__=='__main__':
    main()
