"""
Contains the orchestration for the Gen Con Event Wishlist Visualiser in Streamlit

    Currently uses a hard-coded set of test data from 2024 as a source of events for the visualisation
"""

import streamlit as st
import rawWishlist
import EventListParsing

## switch to go between different test modes
# options are; hardcoded, textbox
mode = "hardcoded"

# get the two pages of wishlist
if mode == "hardcoded":
    # populate from the hardcoded data
    wishlistPageOne = rawWishlist.pageOne
    wishlistPageTwo = rawWishlist.pageTwo
elif mode == "textbox":
    # take from the text boxes
    wishlistPageOne = None
    wishlistPageTwo = None

# build the list of event lists by parsing each wishlist page
pageOneListOfEventLists = EventListParsing.wishlistTextToListOfEventLists(wishlistPageOne)
pageTwoListOfEventLists = EventListParsing.wishlistTextToListOfEventLists(wishlistPageTwo)
# combine the lists into one
listOfEventLists = pageOneListOfEventLists + pageTwoListOfEventLists

# get a list of event dicts
listOfEventDicts = EventListParsing.listOfEventListsToListOfEventDicts(listOfEventLists)

# add event hours to the event dicts
listOfEventDicts = EventListParsing.addEventHours(listOfEventDicts)

# create a dict of lists, one for each hour where there's an event
visualiserDict = EventListParsing.createWishlistVisualiserDict(listOfEventDicts)

# create an HTML table from the visualiser dict
visualiserHTML = EventListParsing.createHTMLVisualisation(visualiserDict)

# # use the table to create an HTML page
# htmlPage = EventListParsing.createHTMLPage(visualiserHTML)

# # create an html document
# htmlFilepath = EventListParsing.writeToHTML(htmlPage)

# display the frame
st.html(visualiserHTML)