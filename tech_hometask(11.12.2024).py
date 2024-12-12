#1
class Password:
    def valid(text):
        uppercase=0
        lowercase=0
        digit=0
        special charecter=0
        length=len(text)
        for i in text:
            if i.isupper():
                uppercase+=1
            elif i.islower():
                lowercase+=1
            elif i.isdigit():
                digit=1
            else:
                special charecter+=1
        if uppercase>=1 and lowercase>=1 and digit>=1 and special charecter>=1 and length>=8:
            print("Your password is Valid")
        else:
            print("Your password is Invalid")
txt=input("Enter the password:")
Password.valid(txt)
##1 the input must be in uppercase
class Password:
    def valid(text):
        uppercase = 0
        lowercase = 0
        digit = 0
        special_character = 0
        length = len(text)

        if not text[0].isupper():
            print("Your password is Invalid: The first letter must be uppercase.")
            return
        
        for i in text:
            if i.isupper():
                uppercase += 1
            elif i.islower():
                lowercase += 1
            elif i.isdigit():
                digit += 1
            else:
                special_character += 1

        if uppercase >= 1 and lowercase >= 1 and digit >= 1 and special_character >= 1 and length >= 8:
            print("Your password is Valid")
        else:
            print("Your password is Invalid")

txt = input("Enter the password: ")
Password.valid(txt)

#2
class TextProcess:
    def __init__(self,text):
        self.text=text
        self.sentencelst=[]
    def split_sentences(self):
        punctuation=['.','?','!']
        sentence=''
        for char in self.text:
            sentence+=char
            if char in punctuation:
                self.sentencelst.append(sentence.strip())
                sentence=''
        if sentence.strip():
            self.sentencelst.append(sentence.strip())
        for i in self.sentencelst:
            print(i)
    def process_sentence(self):
        for sentence in self.sentencelst:
            word_count=len(sentence.split())
            print("Sentence:",sentence,"Word Count:",word_count)
txt=input()
p=TextProcess(txt)
p.split_sentences()
p.process_sentence()
            
