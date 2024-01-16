def main():
    with open('books/frakenstein.txt') as f:
        file_contents = f.read()
        f.close()

if __name__ == '__main__':
   main()