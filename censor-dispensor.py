# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_words = ["she", "self-preservation", "her", "herself"]
proprietary_terms = ["personality matrix",  "learning algorithm", "learning algorithms", "sense of self"]
negative_words = ["concerned", "behind", "dangerous", "danger", "alarming", "alarmed", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
negative_terms = ["out of control"]
list_of_words_to_censor = proprietary_words + negative_words + negative_terms + proprietary_terms

class Word:
    def __init__(self, word, sentence, position, censor=False):
        self.word_lower = word.lower()
        self.word = word
        if len(word)>0:                                 #check if the word is not '\n'
            self.capital_test = word[0].isupper()
        else:
            self.capital_test = False                   #if word is '\n', it doesn't have attribute 'capital'
        self.position = position
        self.sentence_num = sentence

    def get_next_word(self, position):
        return self.position + 1

def create_Words(list):
    sentence_count = 0
    class_word_list = []
    sentence_list = list.pop(0).split(" ")
    for sentence in list:
        sentence_list = sentence.split(" ")
        pos_count = 0
        for word in sentence_list:
            if '\n' in word:
                two_split_words = word.split('\n')
                class_word = Word(two_split_words[0], sentence_count, pos_count)
                class_word_list.append(class_word)
                pos_count +=1
                new_line_Word = Word("\n", sentence_count, pos_count)
                class_word_list.append(new_line_Word)
                pos_count+=1
                sentence_count+=1
                try:
                    class_word = Word(two_split_words[2], sentence_count, pos_count)
                    class_word_list.append(class_word)
                    pos_count+=1
                except IndexError:
                    pass
                continue
            class_word = Word(word, sentence_count, pos_count)
            class_word_list.append(class_word)
            pos_count+=1
        sentence_count +=1
    return class_word_list

def word_censor_function(list_of_class_words, censor_terms, censored_list=[]):
    if list_of_class_words == []:
        return censored_list    
    word_object = list_of_class_words.pop(0)
    word = word_object.word
    position = word_object.position
    word_lower = word.lower()
    for censor_words in censor_terms:
        if len(censor_words.split(' ')) > 1:
            split_terms = censor_words.split(' ')
            for censor_word in split_terms:
                print("censor: ", censor_word)
                print("word lower:" , word_lower)
                if word_lower == censor_word:
                    for i in range(len(word_lower)):
                        if word[i] == " ":
                            word = word.replace(word[i], " ")
                        else:
                            word = word.replace(word[i], "#")
        else:
            if word_lower == censor_words:
                for i in range(len(word_lower)):
                    if word[i] == " ":
                        word = word.replace(word[i], " ")
                    else:
                        word = word.replace(word[i], "#")
    censored_list.append(word)
    return word_censor_function(list_of_class_words, censor_terms, censored_list)

def email_to_sentences(email):
    return [line for line in email.split("\n")]

def sentence_to_wordlist(sentence):
    sentence_listified = []
    for word in sentence_listified:
        sentence_listified.append(word.split(" "))
    return sentence_listified

#email_word_list = [word for word in email_four.split(" ")]
print(email_four)
sentence_list = email_to_sentences(email_four)
class_word_list = create_Words(sentence_list)
for word in class_word_list:    #print the words in the list
    print(word.word)
    print(word.sentence_num)
    print(word.position)
#censored = word_censor_function(class_word_list, list_of_words_to_censor)
#print(' '.join(censored))



