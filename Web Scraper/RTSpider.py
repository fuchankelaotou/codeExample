#! /usr/bin/python3

################################
#
# TO-DO: Add your comments detailing what this
#        class does... Also include all necessary
#        header comment fields (eg: your name)
#
################################

import requests
from bs4 import BeautifulSoup

################################################################
# Make the Yelp spider (a program that gathers data
# from the world wide web (web - spider, get it?).

class RTSpider:

    ############################################################
    # Constructor: takes in the URL that this Spider will parse.
    #
    def __init__( self, base_url ):
        self.base_url=base_url
        # assign the base_url to an instance variable of the same name

    ############################################################
    # Determines the number of review pages available for the give URL.
    #
    # TO-DO: Given the base url, write code to find the number of pages.
    # Break this into a few steps:
    #     1. Get the HTML text from the base_url
    #     2. Make a BeautifulSoup object from that text
    #     3. Use the find method on the HTML tag you think has the text with the page count
    #     4. Work to just get the number
    #            - Think about splitting the text into words
    #            - Figure out where the number is
    #            - Make sure to convert it to an int.
    #
    def get_number_of_review_pages( self ):
        r = requests.get(self.base_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        page = soup.find_all("span", {"class": "css-1e4fdj9"})
        # Extract the code containing the number of pages in the web address
        for str in page:
            p=str.text.find('of')
            # Through analysis, the judgment of determines the number of pages. Use find 'of' to determine the number of pages
            if p!= -1:
                page_count=int(str.text[p+3:])
        #         There are no necessary numbers before of, which should be deleted



        # TO-DO: Add code to figure out the page count

        ###########################################################################
        # !!!*** IMPORTANT ***!!!
        # Name:Mingyu Yang
        # Use these 3 lines of code while debugging... Read in the HTML page from
        # the yelp_example.html file.  This way you don't need to be hitting the
        # yelp web server over and over (while debugging) and thus won't risk 
        # getting your IP address blocked.
        #
        # sample_file = open( "yelp-example.html", "r" )
        # sample = sample_file.read() # Load the HTML into the variable "sample"
        # soup = BeautifulSoup( sample, "html.parser" ) # Create a "soup" of the data from that file.
        #
        # Note, you can and should use this same approach in the get_reviews()
        # method below.
        #
        ###########################################################################

        # Remove following print() statement (and this line) when code has been implemented.
        print("get_number_of_review pages has not been implemented yet!")

        return page_count

    ############################################################
    # Loads all pages that contain reviews (there will be approximately 10 a page)
    # and returns all the reviews in a list. [Note, each item in the list
    # will contain a complete review (multiple sentences).]
    #
    # TO-DO:
    # Make a list containing each review as an item in the list.
    # This code loops over all the pages, making a URL for the current page.
    # Take the URL, get the HTML, and make a BeautifulSoup object, then
    # use the find_all method to get the reviews, add the review text to the review_list.
    #
    def get_reviews(self, page_count):
        review_list = []
        page_counter = 0

        while page_counter < page_count:
            # TO-DO: set extra_url to proper text after base_url
            # including the number corresponding to the page/review count
            extra_url = "?start=" + str(10*int(page_counter))
            # Start10 / 20 / 30 in the URL will affect the number of pages, so match them separately
            full_url = self.base_url + extra_url
            r = requests.get(full_url)
            soup = BeautifulSoup(r.text, 'html.parser')
            page = soup.find_all("span", {"class": "raw__09f24__T4Ezm", "lang": "en"})
            # This is the code that contains comments in the URL code information. Extract it separately
            for content in page:
                review_list.append(content.text)
            # TO-DO: Add code here to get all the reviews on the page
            # print("get_reviews has not been implemented yet!")  # remove this line after implementing
            print("acquiring page " + str(page_counter+1) + "/" + str(page_count))  # remove this line after implementing
            page_counter += 1
        # The comments in each page are calculated page by page


        return review_list

