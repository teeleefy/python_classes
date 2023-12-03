"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
    def __init__(self, file):
        'Scans a file that has one word per line, and gives a total count of words. Returns a random word.'
        self.file = file
        self.list = []
        self.count= 0
    
        def word_count(self):
            myfile = open(self.file, 'r')
            myline = myfile.readline()
            while myline:
                self.count+=1
                self.list.append(myline)
                myline=myfile.readline()
            myfile.close()
            return print(f"There are {self.count} lines in this file")
        
        word_count(self)

    def random(self):
        from random import randint
        my_random_word = self.list[randint(0,self.count-1)]
        return print(my_random_word)


class RandomWordFinder(WordFinder):
     'Provides count of words in document excluding blank lines and words that start with "#"'
     def __init__(self, file):
          super().__init__(file)
     
     def new_random(self):
        # print(self.list)
        for word in self.list:
            if (word.strip() == "") or word.startswith("#"):
                self.list.remove(word)
                self.count-=1
        # print(self.list)
        random_word = super().random()
        
wf = WordFinder("words.txt")
wf.random()
wf.random()
wf.random()
wf.random()

vf = RandomWordFinder('veggies.txt')
vf.new_random()
vf.new_random()