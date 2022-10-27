"""Word Finder: finds random words from a dictionary."""
# command will generate a random integer and  value from the given list/dictionary.

from random import randint

class WordFinder:
   
      # initialize file path  in ()
      # init word  in the file
      # init number of words
    def __init__(self, filename_path):
        self.words = []
        self.filename_path = filename_path
        self.num_of_words_reads = 0

        # self. read (words file from the file path)
        self.read_file(filename_path)
        # after initializing function returns file path and number of words
    def __repr__(self):
        return f"<WordFinder file path='{self.filename_path}' num words reads={self.num_of_words_reads}>"
   # func return if file not found with notice
   # func will also read the word file
    def read_file(self, filename_path):

        try:
            # file in read mode
            files = open(filename_path, 'r', closefd=True)
        except FileNotFoundError:
            print(f" File '{filename_path}' not available.")
            return

        # counter holder for the words
        word_counter = 0
        for file_data in files:
            # strip ()removes or truncates the given characters from the beginning
            # and the end of the original string.
            self.words.append(file_data.strip('\n').strip())
            word_counter +=  1

        self.num_of_words_reads = word_counter
        print(f" number of words {word_counter}  word")
        # file is closed after number of words is read
        files.close()
       # func return random integer values per randint
    def random(self):
        return self.words[randint(0, (self.num_of_word() - 1))]

    def num_of_word(self):
        return self.num_of_words_reads


class SpecialWordFinder(WordFinder):
    
       # let initialize number of blank word and ignored words
    def __init__(self, filename_path):

        self.num_of_ignored_words = 0
        self.num_of_blank_lines = 0
 # super(). function is used to give access to methods and properties
 # of a parent or sibling class
 # it is giving acces to init class from line 36
        super().__init__(filename_path)
     # funtion() self return from  init functions above
    def __repr__(self):
        return (f"<SpecialWordFinder file path='{self.filename_path}' " +
                f"num of words reads={self.num_of_words_reads} " +
                f" words ignored (start with #)={self.num_of_ignored_words} " +
                f" num of blank lines={self.num_of_blank_lines}>")
        # func reads word file and print
    def read_file(self, filename_path):

        try:
            files = open(filename_path, 'r', closefd=True) 
        except FileNotFoundError:
            print(f"File '{filename_path}' is not available.")
            return
         # counter holders
        counter_word = 0
        counter_ignored = 0
        counter_blank_line = 0
         #words holder
        word_holder = None
        for file_data in files:
            word_holder = file_data.strip('\n').strip()
            # After puting the strings of words  files let validate
            #validate word holder and append to words reads
            if (len(word_holder) > 0):
                if (word_holder[0] != "#"):
                    self.words.append(word_holder)
                    counter_word += 1
                else:
                    counter_ignored += 1
            else:
                counter_blank_line += 1

        self.num_of_words_reads = counter_word
        self.num_of_ignored_words = counter_ignored
        self.num_of_blank_lines = counter_blank_line

        print(f"{counter_word} words ")

        files.close()
