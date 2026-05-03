"""
Contains the orchestration for the Gen Con Event Wishlist Visualiser in Streamlit
"""

import streamlit as st
import rawWishlist
import EventListParsing

# set up a title & some explanation
st.title("Gen Con Wishlist Visualiser")
st.text("""Creates a visualisation of a Gen Con Event Wishlist, so that you can see how event priorities will interact. The intention here is to make it easy to see those circumstances where one event 'blocks' others, so that they can be ordered in a way that allows for backup events.
        
The visualiser will skip Wednesday unless there are events, and will skip hours before 8am unless there are events.""")

## switch to go between different modes
mode = st.menu_button(label="Mode: Test or Live", options=["Test (hardcoded)", "Live (textbox)"], help="Selects Live or Test modes; Mostly here so that I don't break things while experimenting")

# get the two pages of wishlist if at all possible
if mode == None:
    # there has been no selection yet, so set wishlist pages to None just in case
    wishlistPageOne = None
    wishlistPageTwo = None
elif mode == "Test (hardcoded)":
    # populate from the hardcoded data
    wishlistPageOne = rawWishlist.pageOne
    wishlistPageTwo = rawWishlist.pageTwo
    # tell the user about it
    st.text("Populating using a wishlist from 2024, to show how it works")
elif mode == "Live (textbox)":
    # add a label for the text box section
    st.header("Wishlist Information Goes Here", divider=True)
    # add some instructions
    st.text("Copy-Paste from your wishlist into the text areas below, priorties 1-25 in the first are & 26-50 in the second; If you select from the middle of the word 'prority' & down to the end of the time of the last event on the list, that should do the job")
    # take from the text boxes
    wishlistPageOne = st.text_area(label="Wishlist Page One", help="Copy-Paste into here from page 1 of your wishlist, priorties 1-25; If you select from the middle of the word 'prority' & down to the end of the time of the last event on the list, that should do the job")
    wishlistPageTwo = st.text_area(label="Wishlist Page Two", help="Copy-Paste into here from page 2 of your wishlist, priorties 26-50; If you select from the middle of the word 'prority' & down to the end of the time of the last event on the list, that should do the job")

## there may not yet be a mode selection, so only do something if mode has a value
if mode is not None:
    ## if there's nothing in the text boxes, don't draw the table, just display a message
    if (wishlistPageOne is None or len(wishlistPageOne)==0) and (wishlistPageTwo is None or len(wishlistPageTwo)==0):
        # the text boxes are empty
        st.header("Wishlist Visualisation Will Only Be Created When There Is Wishlist Data", divider=True)
    else:
        # add a header
        st.header("Wishlist Visualisation", divider=True)
        
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

        # display the table
        st.html(visualiserHTML)