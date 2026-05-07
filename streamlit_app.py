"""
Contains the orchestration for the Gen Con Event Wishlist Visualiser in Streamlit
"""

import streamlit as st
import EventListParsing

# set up a title & some explanation
st.title("Gen Con Wishlist Visualiser")
st.text("""Creates a visualisation of a Gen Con Event Wishlist, so that you can see how event priorities will interact. The intention here is to make it easy to see those circumstances where one event 'blocks' others, so that they can be ordered in a way that allows for backup events.
        
The visualiser will skip Wednesday unless there are events, and will skip hours before 8am unless there are events.""")

# add a label for the text box section
st.header("Wishlist Information Goes Here", divider=True)
# add some instructions
st.text("Copy-Paste from your wishlist page into the text areas below, priorities 1-25 in the first area & 26-50 in the second; If you just hit Ctrl+A to select the whole webpage, Ctrl+C to copy the whole webpage, and Ctrl+P to paste it, that should do the job")

# take from the text boxes
wishlistPageOne = st.text_area(label="Wishlist Page One", help="Copy-Paste page 1 of your wishlist, priorties 1-25, into here")
wishlistPageTwo = st.text_area(label="Wishlist Page Two", help="Copy-Paste page 2 of your wishlist, priorties 26-50, into here")

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

    # display a button to show the table HTML for copying
    if st.button("Click Here For Table HTML") == True:
        # display the table HTML as a text item
        st.text(visualiserHTML)