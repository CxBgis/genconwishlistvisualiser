
import streamlit as st
import rawWishlist
import EventListParsing

# build the list of event lists by parsing each page
pageOneListOfEventLists = EventListParsing.wishlistTextToListOfEventLists(rawWishlist.pageOne)
pageTwoListOfEventLists = EventListParsing.wishlistTextToListOfEventLists(rawWishlist.pageTwo)
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