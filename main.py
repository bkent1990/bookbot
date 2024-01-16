class ReadFrankenstein():
        def __init__(self, file_path):
          with open(file_path) as f:
            self.file_contents = f.read()
            self.word_count = None

        def count_words(self):
         self.word_count = len(self.file_contents.split())
         return self.word_count
        
        def count_letters(self):
          letter_total = {}
          words = self.file_contents.split()
          for word in words:
             for letter in word:
                alpha = letter.lower()
                if alpha.isalpha():
                  count = letter_total.get(alpha, 0)
                  count +=1
                  letter_total[alpha] = count

          sorted_letters = dict(sorted(letter_total.items()))
          return sorted_letters
        
        def book_report(self):
               report = f"--- Begin report of books/frankenstein.txt --- \n {self.count_words()} words found in the document\n"
               for key, value in self.count_letters().items():
                  report += f"The '{key}' character was found {value} times \n"

               report += "---End Report ---"
               return report
              

def main():
   file_path = 'books/frankenstein.txt'
   read_book = ReadFrankenstein(file_path)
   #word_count = read_book.count_words()
   #letter_count = read_book.count_letters()
   book_report = read_book.book_report()
   print(book_report)
   
if __name__ == '__main__':
   main()