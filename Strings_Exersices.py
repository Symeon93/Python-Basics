'''
In the particular exersice we go through the basic manilulations of strings, this includes defining functions
that find substrings within given strings or rearranging  given strings. Immutability of strings has been taken into
consideration
'''


def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False


def common_letters(string_one, string_two):
    my_list = []
    for char in string_one:
        if (char in string_two) and (char not in my_list):
            my_list.append(char)
    return my_list


print(common_letters("python", "ruby on rails"))

print(contains("Python", "Pyt"))


def username_generator(first_name, last_name):
    if len(first_name) < 3:
        user_name = first_name
    else:
        user_name = first_name[0:3]
    if len(last_name) < 4:
        user_name += last_name
    else:
        user_name += last_name[0:4]
    return user_name


def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i - 1]
    return password


def password_gen(username):
    password = ""
    for i in range(-len(username), 0):
        password += username[i + 1]
    return password


print(password_gen(username_generator("Symeon", "Paskos")))

print(password_generator(username_generator("Symeon", "Paskos")), "\n\n")

'''
In this exercise we perform all the basic methods on an initial string so to clean any inconsistencies and 
produce a readable output.
'''
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, " \
                    "Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   " \
                    "Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, " \
                    "Mr. Grumpledump's Song:Shel Silverstein:2004," \
                    " Angel Sound Mexico City:Carmen Boullosa:2013, " \
                    "In Love:Kamala Suraiyya:1965, " \
                    "Dream Variations:Langston Hughes:1994," \
                    " Dreamwood:Adrienne Rich:1987"

print(highlighted_poems, "\n")

highlighted_poems_list = highlighted_poems.split(",")

print(highlighted_poems_list, "\n")

highlighted_poems_stripped = []
for word in highlighted_poems_list:
    highlighted_poems_stripped.append(word.strip())

print(highlighted_poems_stripped, "\n")

highlighted_poems_details = []

for word in highlighted_poems_stripped:
    highlighted_poems_details.append(word.split(":"))

print(highlighted_poems_details, "\n")

titles = []
poets = []
dates = []

for word in highlighted_poems_details:
    titles.append(word[0])
    poets.append(word[1])
    dates.append(word[2])

print(titles, "\n", poets, "\n ", dates, "\n")

for i in range(len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

'''
In this exercise we take a set of transactions and clean the initial to bring it into a consistent human 
readable form. Then we simply find the total amount of sales performed as well as the amount sold in 
each category.
 
'''

daily_sales = \
    """Edith Mcbride   ;,;$1.21   ;,;   white ;,; 
    09/15/17   ,Herbert Tran   ;,;   $7.29;,; 
    white&blue;,;   09/15/17 ,Paul Clarke ;,;$12.52 
    ;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell   
    ;,;   $5.13   ;,; white   ;,; 09/15/17,
    Eduardo George   ;,;$20.39;,; white&yellow 
    ;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,;   
    purple ;,;09/15/17 ,Stacy Vargas;,; $1.85   ;,; 
    purple&yellow ;,;09/15/17,   Shaun Brock;,; 
    $17.98;,;purple&yellow ;,; 09/15/17 , 
    Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, 
    Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
    Carroll Boyd;,; $14.51;,;   purple&blue   ;,;   
    09/15/17   , Teresa Carter   ;,; $19.64 ;,; 
    white;,;09/15/17   ,   Jacob Kennedy ;,; $11.40   
    ;,; white&red   ;,; 09/15/17, Craig Chambers;,; 
    $8.79 ;,; white&blue&red   ;,;09/15/17   , Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 
    09/15/17   ,   Marvin Morgan;,;   $16.49;,; 
    green&blue&red   ;,;   09/15/17 ,Marjorie Russell 
    ;,; $6.55 ;,;   green&blue&red;,;   09/15/17 ,
    Israel Cummings;,;   $11.86   ;,;black;,;  
    09/15/17,   June Doyle   ;,;   $22.29 ;,;  
    black&yellow ;,;09/15/17 , Jaime Buchanan   ;,;   
    $8.35;,;   white&black&yellow   ;,;   09/15/17,   
    Rhonda Farmer;,;$2.91 ;,;   white&black&yellow   
    ;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green 
    ;,;09/15/17,Rufus Malone;,;$4.70   ;,; green&yellow 
    ;,; 09/15/17   ,Hubert Miles;,;   $3.59   
    ;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,;$5.66   ;,; green&yellow&purple&blue 
    ;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,;   
    black   ;,;   09/15/17 , Audrey Ferguson ;,; 
    $5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; 
    $17.13;,; black&blue;,;   09/15/17,   Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   ,
    Ernesto Hunt ;,; $13.91   ;,;   black&purple ;,;   
    09/15/17,   Shannon Chavez   ;,;$19.26   ;,; 
    yellow;,; 09/15/17   , Sammy Cain;,; $5.45;,;   
    yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50   
    ;,;   yellow;,;   09/15/17, Ruben Jones   ;,; 
    $14.56 ;,;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red
    ;,; 09/15/17   ,   Rene Hardy   ;,; $20.22   ;,; 
    black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67   
    ;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,;   
    $8.31;,;   black&red ;,;   09/15/17,   Stacey Payne 
    ;,;   $15.70   ;,;   white&black&red ;,;09/15/17   
    ,   Tanya Cox   ;,;   $6.74   ;,;yellow   ;,; 
    09/15/17 , Melody Moran ;,;   $30.84   
    ;,;yellow&black;,;   09/15/17 , Louise Becker   ;,; 
    $12.31 ;,; green&yellow&black;,;   09/15/17 ,
    Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 
    ,Justin Blake ;,; $22.46   ;,;white&yellow ;,;   
    09/15/17,   Beverly Baldwin ;,;   $6.60;,;   
    white&yellow&black ;,;09/15/17   ,   Dale Brady   
    ;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
    Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17  
    ,Sonja Barnett ;,; $14.22 ;,;white&black;,;   
    09/15/17, Angelica Garza;,;$11.60;,;white&black   
    ;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; 
    white&black&red ;,;09/15/17   ,   Rex Hudson   
    ;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs 
    ;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
    Hannah Pratt;,;   $22.61   ;,;   purple&yellow   
    ;,;09/15/17,Gayle Richards;,;$22.19 ;,; 
    green&purple&yellow ;,;09/15/17   ,Stanley Holland 
    ;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   ,
    Terrance Saunders ;,;   $23.70  ;,;green&yellow&red 
    ;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; 
    red   ;,;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; 
    green&red ;,;   09/15/17   ,Irving Patterson 
    ;,;$19.55 ;,; green&white&red ;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,;09/15/17, 
    Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
    Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , 
    Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17   
    ,Josephine Keller ;,;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 ,
    Ignacio Parks;,;$14.70   ;,; white&red ;,;09/15/17 
    , Beatrice Newman ;,;$22.45   ;,;white&purple&red 
    ;,;   09/15/17, Andre Norris   ;,;   $28.46   ;,;   
    red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,;   
    black&red;,; 09/15/17,   Javier Bailey   ;,;   
    $24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 ,   
    Abraham Maxwell;,; $6.81   ;,;green;,;   09/15/17   
    ,   Traci Craig ;,;$0.65;,; green&yellow;,; 
    09/15/17 , Jeffrey Jenkins   ;,;$26.45;,; 
    green&yellow&blue   ;,;   09/15/17,   Merle Wilson 
    ;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin   
    ;,;$8.74   ;,; purple&black   ;,;09/15/17 ,  
    Leonard Guerrero ;,;   $1.86   ;,;yellow  
    ;,;09/15/17,Lana Sanchez;,;$14.75   ;,; yellow;,;   
    09/15/17   ,Donna Ball ;,; $28.10  ;,; 
    yellow&blue;,;   09/15/17   , Terrell Barber   ;,; 
    $9.91   ;,; green ;,;09/15/17   ,Jody Flores;,; 
    $16.34 ;,; green ;,;   09/15/17,   Daryl Herrera 
    ;,;$27.57;,; white;,;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 ,   
    Rogelio Gonzalez;,; $9.51;,;   white&black&blue   
    ;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; 
    green;,;   09/15/17,Owen Ward;,; $21.64   ;,;   
    green&yellow;,;09/15/17,Malcolm Morales ;,;   
    $24.99   ;,;   green&yellow&black;,; 09/15/17 ,   
    Eric Mcdaniel ;,;$29.70;,; green ;,; 09/15/17 
    ,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 
    , Leticia Manning;,;$15.70 ;,; green&purple;,; 
    09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 
    09/15/17,Lewis Glover;,;   $13.66   ;,;   
    green&white;,;09/15/17,   Gail Phelps   ;,;$30.52   
    ;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris 
    ;,;   $22.66   ;,; green&white&blue;,;09/15/17"""

# ------------------------------------------------
# Start coding below!


print(daily_sales, "\n\n")

daily_sales_replaced = daily_sales.replace(";,;", "_")

print(daily_sales_replaced, "\n\n")

daily_transactions = daily_sales_replaced.split(",")

print(daily_transactions, "\n\n")

daily_transactions_split = []

for word in daily_transactions:
    daily_transactions_split.append(word.split("_"))

print(daily_transactions_split, "\n\n")

transactions_clean = []
transactions_inner = []

for word in daily_transactions_split:
    for my_string in word:
        transactions_inner.append(my_string.strip())
    transactions_clean.append(transactions_inner)
    transactions_inner = []

print(transactions_clean, "\n\n")

customers = []
sales = []
thread_sold = []

for word in transactions_clean:
    customers.append(word[0])
    sales.append(word[1])
    thread_sold.append(word[2])

print(customers, "\n\n", sales, "\n\n", thread_sold, "\n\n")

total_sales = 0

for word in sales:
    new_word = float(word.strip("$"))
    total_sales += new_word

print(total_sales, "\n\n")

thread_sold_split = []

for word in thread_sold:
    if "&" not in word:
        thread_sold_split.append(word)
    else:
        thread_sold_split.append(word.split("&")[0])
        thread_sold_split.append(word.split("&")[1])

print(thread_sold_split, "\n\n")


def color_count(color):
    counter = 0
    for i in range(len(thread_sold_split)):
        if color == thread_sold_split[i]:
            counter += 1
    return counter


print(color_count("white"))

colors = ["red", "yellow", "green", "white", "black", \
          "blue", "purple"]

for word in colors:
    print("The number of thead sold of color {} is {}".format(word, color_count(word)))

# Exersice 1
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


# Write your unique_english_letters function here:
def unique_english_letters(word):
    uniques = 0
    for letter in letters:
        if letter in word:
            uniques += 1
    return uniques


# Uncomment these function calls to test your tip function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))


# should print 4


# Exersice 2
# Write your count_char_x function here:
def count_char_x(word, x):
    occurrences = 0
    for letter in word:
        if letter == x:
            occurrences += 1
    return occurrences


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))


# should print 1

# Exersice 3
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
    splits = word.split(x)
    return (len(splits) - 1)


# Uncomment these function calls to test your  function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))


# should print 1

# Exersice 4
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return word[start_ind + 1:end_ind]
    return word


# Uncomment these function calls to test your tip function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))


# should print "apple"


# Exersice 5
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return (word[start_ind + 1:end_ind])
    return word


# Uncomment these function calls to test your tip function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))


# should print "apple"

# Exersice 6
# Write your check_for_name function here:
def check_for_name(sentence, name):
    return name.lower() in sentence.lower()


# Uncomment these function calls to test your function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))


# should print False

# Exercise 7

# Write your every_other_letter function here:
def every_other_letter(word):
    every_other = ""
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other


# Uncomment these function calls to test your tip function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))


# should print

# Exercise 8
# Write your reverse_string function here:
def reverse_string(word):
    reverse = ""
    for i in range(len(word) - 1, -1, -1):
        reverse += word[i]
    return reverse


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))


# should print

# Exercise 9
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    return word2[0] + word1[1:] + " " + word1[0] + word2[1:]


# Uncomment these function calls to test your tip function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))


# should print b a

# Exercise 10
# Write your add_exclamation function here:
def add_exclamation(word):
    while (len(word) < 20):
        word += "!"
    return word


# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn


'''
Caesar's cipher: 
Cryptography/encryption is a methodology broadly used to protect privacy of the end users. An early and simple 
Cryptographic method is Caesar's cipher. In this context the letter of the initial message are shifted by a common value 
called the offset. The offset is in general not known in advance. So here we will try to define a function (decoder)
that will take an initial decrypted message and turn into human read form (i.e. crack the code behind). We also 
define another function (encoder) that will decrypt a human readable message into what may seem completely fuzzy. 
'''

alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "


def decoder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message


def coder(message, offset):
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message


coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk " \
                "ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

# let's try to decode the above message
print("\n\n")
for i in range(0, 25):
    print("offset: " + str(i))
    print("\t", decoder(coded_message, i), "\n")


