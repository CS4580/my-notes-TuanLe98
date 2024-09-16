"""Download data from our server"""
SERVER_URL ='http://icarus.cs.weber.edu/~hvalle/cs4580/data/'
import pandas as pd
import requests
import os

def download_file(url, file_name):
    response = requests.get(url)
    
    
    pass

def unzip_file(file_name):
    pass

def main():
    """Driven function"""
    if len(sys.argv)<2:
        print("Usage: python download <data_file>")
        sys.exit(1)


    data01 = 'pandas01Data.zip'
    download_file(SERVER_URL,data01)
    unzip_file(data)

if __name__=='__main__':
    main()
