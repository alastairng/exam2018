import operator

def get_letter_value(letter):
    dictionary = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    dictionary2 = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    if letter in dictionary:
        return dictionary[letter]
    elif letter in dictionary2:
        return dictionary2[letter]
    else:
        return 0

def load_roster():
    with open("roster.txt") as f:
        roster = f.readlines()
    roster = [x.strip() for x in roster] 
    return roster

def load_positive_words():
    with open("positive-words.txt") as f:
        positive_words = f.readlines()
    positive_words = [x.strip() for x in positive_words] 
    return positive_words

def get_word_numeric_value(word):
    value = 0
    word = word.split(" ")[0]
    for letter in word:
        value += get_letter_value(letter)
    return value

def get_highest_value_word_in_roster(roster):
    roster_dict = {}
    for name in roster:
        roster_dict[name] = get_word_numeric_value(name) 

    highest_valued_name = max(roster_dict.items(), key=operator.itemgetter(1))[0]
    return highest_valued_name

def get_matching_words(value):
    matching_words = []
    positive_words = load_positive_words()
    for word in positive_words:
        numeric_value = get_word_numeric_value(word)
        if numeric_value == value:
            matching_words.append(word)

    if len(matching_words) == 0:
        return None
    else:
        return matching_words



def main():
    
    roster = load_roster()

    # Get the highest valued name in the roster
    highest_valued_word = get_highest_value_word_in_roster(roster)
    print("The highest valued name is " + highest_valued_word + " the value is " + str(get_word_numeric_value(highest_valued_word)))
    # Get the value of my name and see if there are matching name
    my_name = "Alastair Ng"
    my_name_value = get_word_numeric_value(my_name)
    
    # Find matching words
    matching_words = get_matching_words(my_name_value)
    print("The matching words for my name " +  my_name + " are " + str(matching_words))
    
if __name__ == '__main__':
    main()
