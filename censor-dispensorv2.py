# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["personality matrix",  "learning algorithm", "learning algorithms", "sense of self","she", "self-preservation", "her", "herself"]
negative_words = ["concerned", "out of control", "behind", "dangerous", "danger", "alarming", "alarmed", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
list_of_words_to_censor = negative_words + proprietary_terms

email_four_lower = email_four.lower()
for word in list_of_words_to_censor:
    if word in email_four_lower:
        index_of_word = email_four.index(word)
        while word in email_four:
            censored_word = ""
            for i in range(len(word)):
                if word[i] == " ":
                    censored_word += " "
                else:
                    censored_word += "#" 
            email_four_lower = email_four_lower.replace(word, censored_word)
            email_four = email_four.replace(word, censored_word)
email_word_list = [word for word in email_four.split(" ")]
idx = 0
print(email_four)
for word in email_word_list:
    if '#' in word:
        pre_word = email_word_list[idx-1]
        post_word = email_word_list[idx+1]
        censored_word = ""
        for i in range(len(pre_word)):
            if pre_word[i] == " ":
                censored_word += " "
            else:
                censored_word += "#" 
        email_four = email_four.replace(pre_word, censored_word)
        for i in range(len(post_word)):
            if post_word[i] == " ":
                censored_word += " "
            else:
                censored_word += "#" 
        email_four = email_four.replace(post_word, censored_word)
        idx+=1
    idx+=1


print(email_four)



