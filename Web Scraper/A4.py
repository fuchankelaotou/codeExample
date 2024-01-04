################################
#
# Assignment 4 - Helper Functions / Main
# Name:Mingyu Yang
# This file contains the following helper functions.  See
# each function for more details.
#
# - break_sentences_into_words( review_list )
# - clean_words( word_list )
# - remove_boring_words( boring_words_filename, restaurant_name, cleaned_words )
# - count_repeats( good_words )
# - main()
#
# TO-DO: Add your comments about what this program does.
#        Also, add all the required information to this header comment.
#
################################


################################################################
# break_sentences_into_words()
#
# This function has been written for you.  It takes a list of reviews
# (each review can be many sentences) and pulls out all the individual
# words in all the reviews.  The list of all these words is returned
# to the caller.
import csv
import string

from RTSpider import RTSpider


def break_sentences_into_words( review_list ):
    all_words = []
    for review in review_list:
        words = review.split()
        # Extract the text in turn and make each text single
        all_words = all_words + words # Note, could use: all_words.extend( words )
    return all_words

################################################################
# clean_words()
# 
# This function makes each word lower case and removes punctuation.
#
# TO-DO: Add a list comprehension to make each word lower case with the
#        string lower() method.

def clean_words( word_list ):
    lower_words = []
    for sen in word_list:
        lower_words.append(sen.lower())
    #     Make all the letters in each sentence lowercase

    # TO-DO: Write a list comprehension to make each word in word_list lower case.
    #        Store the result in the lower_words list.

    # Remove the following print (and this comment) when this when implemented.
    print( "clean_words has not been implemented yet - read the comments in the function and fix!" )

    # Remove punctuation from the words in lower_words.
    words_without_punct = [ word.translate( str.maketrans('', '', string.punctuation) ) for word in lower_words ]
    return words_without_punct

################################################################
# remove_boring_words()
#
# Call this function with 1) the name of the file containing the boring words,
# 2) a string containing the restaurant name (all lower case, no punctuation), and
# 3) the list of words to remove uninteresting words from.
# Returns a new list containing non-boring words.
#
# To-DO: Add the list comprehension specified below.

def remove_boring_words( boring_words_filename, restaurant_name, cleaned_words ):
    cleans_words=[]
    for txt in cleaned_words:
        cleans_words.extend(txt.split())
    #     Extract the processed text one by one
    # First, read in the list of words from the file of boring words:
    boring_words = []

    with open( boring_words_filename ) as file:
        for line in file:
            boring_words.append( line.strip() )
    #         Extract all the questions in the boring file and create a list

    # Also get rid of the restaurant name words as they show up a lot.
    boring_words = boring_words + restaurant_name.split()

    # Now, make a new list of words from cleaned words that are not in the
    # boring_words list.

    no_boring = [] # TO-DO: Change this line to a list comprehension that filters out boring words

    for x in cleans_words:
        flag = 0
        for y in boring_words:
            if y==x:
                flag=1
        if flag == 0:
            no_boring.append(x)
    #         Eliminate all boring words

    # Remove the following print line (and this comment) after implementing...
    print( "remove_boring_words has not been implemented yet - read the comments in the function and fix!" )

    return no_boring


################################################################
# count_repeats()
#
# Takes in a list of words and returns a dictionary that
# contains contains the number of times each word occurred in the list.
#
# TO-DO: Add code requested below.

def count_repeats( good_words ):
    word_counts = {}

    # TO-DO: Add code here to turn the list of good_words into a dictionary
    # of each word and the number of times it is repeated in good_words

    print( "count_repeats has not been implemented yet - read the comments in the function and fix!" ) 
    # remove the above print() line when implemented

    for i in good_words:
        if good_words.count(i) >= 1:
            word_counts[i] = good_words.count(i)
    #         Extract all the interesting words


    return word_counts

################################################################
#
# main()
#
# Given a URL, get the reviews, clean them, and count word repeats.
# Finish by printing all the review words with enough repeats.
#
# Update the sections of code below marked with TO-DO!

def main():

    # Find your own urls...
    base_url = "https://www.yelp.com/biz/the-willow-bistro-murray"
    # base_url="https://www.yelp.com/biz/marthas-restaurant-murray"

    a = RTSpider(base_url)
    # Used in import class
    page_count = a.get_number_of_review_pages()
    page = a.get_reviews(page_count)
    print("Pages:", page_count)
    page = clean_words(page)
    # Use the set function
    restaurant_name = "QDOBA Mexican Eats"
    page = remove_boring_words('boring_words.txt', restaurant_name, page)
    word_count_dict = count_repeats(page)
    print(word_count_dict)

    # Remove words that do not appear often enough from the dictionary
    # (Note: What does the following line of code do, and how does it work?)

    reduced = { key: value for (key, value) in word_count_dict.items() if value > 5 }
    # Use only words that appear more than five times

    # Print it out in a form the word cloud software wants
    Final=[]

    # Remove the following for loop/print statement when your code is working.
    # It is here to help with debugging.
    for key in reduced: 
        print( str( word_count_dict[key] ) + ", " + str( key ) )
        Final.append([str(word_count_dict[key]) , str(key)])
    #     Import text into dictionary
    # TO-DO:
    # Open a file named "results.csv".  Store each entry in the dictionary in that file,
    # line by line (in the form: count, word.  Eg: 45, tasty).
    #
    #   Pseudo code:
    #   - Open the file
    #   - Loop over the dictionary keys
    #   -    Write the value, key to the file
    #   - Close the file when the loop is done.
    with open('1234.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerows(Final)
#         Extract the contents of the dictionary to 1234 CSV file


################################################################

if __name__ == "__main__":
    main()

