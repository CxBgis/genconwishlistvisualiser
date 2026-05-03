"""
By Hours
Have a dict where each key is a one hour block, and each value is a list holding elements which are either {Priority}-{Event Name} or None

Placing an event
Working through in priority order, starting at 1

Get a list of all the 'hours' for the event
If there is no dict key for an hour, create it with an empty list
Get the maximum list length by looping through the hours; This will be the index of the event we're placing. It cannot go before an existing event because the priority would therefore not be applied, so it needs to go in the next available index value, which will be one more than the biggest index value, which will be the same as the list link for the biggest list.
For each hour list insert None values up to index-1, then insert the Priority and Event ID
Update the dict for each hour with the updated list
"""

# import re
import datetime
import os
import webbrowser

import rawWishlist


def wishlistTextToListOfEventLists(wishlistTextString):
    """
    takes the text from the Gen Con Wishlist page and turns it into a list of events,
    where each event list is a list of event elements
    """

    # set up a list to hold events & a list for the actual event
    eventsWishlist = []
    eventList = []
    # # set the code for this years events - it's inside the Game ID
    # yearCode = "26ND"
    # # set the regex match string based on that year code, so that we can identify Game IDs
    # regexMatchString = "[A-Z]{3}" + yearCode +"[0-9]+"
    # set a flag for "we have hit the actual events"
    foundTheEvents = False
    # set a variable for the priority, as it annoyingly comes before the event ID
    priority = None

    # split the page string on newline to get lines
    wishlistTextLines = wishlistTextString.split("\n")

    # work through the lines, assembling events as we go
    for line in wishlistTextLines:
        # discard lines until we hit something that looks like the header row
        if foundTheEvents == False and "\tGame ID\tTitle\t" not in line:
            continue
        # discard the header row, and set found events to true
        if foundTheEvents == False and "\tGame ID\tTitle\t" in line:
            foundTheEvents = True
            continue
        # skip the line if it's empty
        if len(line) == 0:
            continue
        # if the line starts with "Grey events have sold out" we've reached the end of the events
        if line.startswith("Grey events have sold out"):
            break
            
        # if the line contains just a number, it's the priority, and this is a new event
        if (len(line) == 1 and 0<int(line)<10) or (len(line) == 2 and 9<int(line)<51):
            # set the priority
            priority = int(line)
            # it's a new event - is there an existing event to be added to the events wishlist?
            if len(eventList) > 0:
                # append it
                eventsWishlist.append(eventList)
            # set up a new event
            eventList = []
            # add the priority
            eventList.append(priority)
            # move on to the next line
            continue
            
        # this is presumably a line with multiple tab-separated parts - split on tab to get the individual elements
        lineElements = line.split("\t")
        ## work through the elements
        for lineElement in lineElements:
            # is it an empty element?
            if lineElement is None or len(lineElement) == 0:
                # it's an empty element, so do absolutely nothing
                pass
            # in all other cases, add it to the list
            else:
                eventList.append(lineElement)
                
    # because we are using the priority to trigger writing out an event, when we run out of lines, there's still one event list left, so add that to the events wishlist
    if len(eventList) > 0:
        # append it
        eventsWishlist.append(eventList)

    # do the return
    return eventsWishlist


def listOfEventListsToListOfEventDicts(listOfEventLists):
    """
    turns the list of event lists into a list of event dicts,
    so that we have a named value for each part of the event listing
    input is expected to look like this;
    [2,
    'RPG26ND306958',
    'Westward Bound',
    'The Last Caravan, 1st Edition',
    'Saturday',
    '10:00 AM EDT',
    '4 hr',
    '$16']
    """

    # set up a list of keys, in the order they're expected
    keyList = ["Priority", "GameID", "Name", "System", "Day", "Time", "Duration", "Cost"]
    # there's a chance that there is no system for the event, so we need a different key list for that case
    systemlessKeyList = ["Priority", "GameID", "Name", "Day", "Time", "Duration", "Cost"]

    # set up a list to return
    listOfEventDicts = []

    # work through the event wishlist
    for eventList in listOfEventLists:
        # set up a dict
        eventDict = {}
        # work through the eventList items using an enumeration, matching up the list items with the keys in keylist
        for index, value in enumerate(eventList):
            # check the length of the eventlist - if it's got 8 elements, it uses the regular key list, if there are only 7, it has no system, and uses the systemless key list
            if len(eventList) == 8:
                # insert the element at index into the dict with the key corresponding to that element's index
                eventDict[keyList[index]] = value
            else:
                # insert the element at index into the dict with the key corresponding to that element's index
                eventDict[systemlessKeyList[index]] = value

        # if there isn't a System key in the dict, which is a valid situation, add an empty string for System
        if not "System" in eventDict.keys():
            eventDict["System"] = ""

        # add the event dict to the list
        listOfEventDicts.append(eventDict)

    # do the return
    return listOfEventDicts


def addEventHours(listOfEventDicts):
    """
    calculates which hour blocks each event occupies, and puts them in a list in the event dict
    events taking fractional hours are assumed to take the whole hour block,
    so 2h 30m fills three hours, and 15m fills one hour
    hour 0 is Wednesday 00:00, hour 24 is Thursday 00:00
    input dicts are expected to look like this;
    [{'GameID': 'RPG24ND260320',
    'Name': 'Psychic Trash Detectives',
    'Day': 'Friday',
    'Duration': '3 hr',
    'Cost': '$8',
    'System': 'Psychic Trash Detectives, 1st Edition',
    'Time': '10:00 AM EDT',
    'Priority': 1}]
    """

    # set up a list of day names, to make calculating the hour easier - we can multiply the index of the day by 24 to get the offset for the hours
    dayList = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # work through the eventsWishlist
    for eventDict in listOfEventDicts:
        ## figure out the starting hour
        # get the hour offset from daylist - take the index of the day, multiply by 24, and use as the base value for the hour
        #   we'll add the hour of the day on afterwards to get the final value
        #   for multi-hour events, this is the _first_ hour of the event
        day = eventDict["Day"]
        startingHour = dayList.index(day) * 24

        # get the hour by using strptime to create the time object from the time, then strftime to get just the hour
        #   we're expecting the time to be in the format '10:00 AM EDT'
        timeObject = datetime.datetime.strptime(eventDict["Time"], '%I:%M %p EDT')
        eventHourString = timeObject.strftime('%H')
        # convert eventHourString into an integer, and add to startingHour - the conversion takes care of any leading zero for us
        startingHour = startingHour + int(eventHourString)

        ## figure out which hours are taken up by this event - the event should be of the form "X hr", but might have a minutes value after it, or might just be minutes if it's a very short event
        ## first, figure out the duration in hours
        # does " hr" appears in the duration?
        if " hr" in eventDict["Duration"]:
            # split on " hr"
            durationSplit = eventDict["Duration"].split(" hr")
            # take the first element as an integer
            duration = int(durationSplit[0])
            # if the second element is anything other than an empty string, there's something else in the duration, so add one
            if len(durationSplit[1]) > 0:
                duration = duration + 1
        else:
            # this is a very short event, so it gets the default duration of 1
            duration = 1

        ## next, generate a list of all the hours occupied by this event
        # we can use a range to do this - the end value isn't included in the range, so a one-hour event will only have a one-element list
        hoursOccupied = list(range(startingHour, startingHour + duration))
        # add the hours occupied to the dict
        eventDict["HoursOccupied"] = hoursOccupied

    # do the return
    return listOfEventDicts


def createWishlistVisualiserDict(listOfEventDicts):
    """
    creates a dict where each key is an hour, and each value is a list for the events taking place in that hour
    this is the final structure of the table, so None values are fine, as they're there for spacing purposes
    output will looks lomething like this;
    {"36": [{event dict}, None, {event dict}]}
    it's a dict because there will be a lot of completely empty hours, so why store data that's not needed?
    """

    # set up the visualiser dict
    visualiserDict = {}

    ## work through the list of event dicts
    for eventDict in listOfEventDicts:
        # get the list of hours occupied by the event
        hoursOccupiedList = eventDict["HoursOccupied"]

        ## make sure the hours exist in the dict - if any hour on that list doesn't exist in the dict, create it with an empty list
        for hour in hoursOccupiedList:
            if not str(hour) in visualiserDict.keys():
                visualiserDict[str(hour)] = []

        ## we need the maximum length of any hour list from the dict which occurrs in the occupied hours - this gives us the index at which we can insert this event
        # set up a maximum length variable
        maximumListLength = 0
        # work through hoursOccupiedList, checking each hour in the visualiser dict
        for hour in hoursOccupiedList:
            # get the length of the list for that hour
            listLength = len(visualiserDict[str(hour)])
            # if this list is longer than our previous maximum, update it
            if listLength > maximumListLength:
                maximumListLength = listLength
        
        ## we now have the longest length of any of the occupied lists - because the indexes start at zero, this means we also have the index at which we can insert this event dict into each list
        # work through hoursOccupiedList again
        for hour in hoursOccupiedList:
            # get the list
            hourListFromVisualiser = visualiserDict[str(hour)]
            # add None values to it until it's at our maximum length
            while len(hourListFromVisualiser) < maximumListLength:
                hourListFromVisualiser.append(None)
            # now add the event dict
            hourListFromVisualiser.append(eventDict)

    # do the return
    return visualiserDict


def createQuickAndDirtyVisualisation(visualiserDict):
    """
    creates a list of strings, one for each hour, with either an empty space or a priority number
    this is to build a very crude visualisation for testing
    """

    # set up the list of strings
    listOfStrings = []

    # work through all of the hours
    for hour in range(0, 24*5):
        # is the hour in visualiser dict?
        if str(hour) in visualiserDict.keys():
            ## we're going to build up a string representing this list, with a double-space for None and a space-padded priority where there's an event
            # set up the string
            stringRepresentation = ""
            # get the list
            hourList = visualiserDict[str(hour)]
            # work through the list
            for element in hourList:
                # is element None or is there an event dict?
                if element is None:
                    # add two spaces
                    stringRepresentation = stringRepresentation + "  "
                else:
                    # get the priority
                    priority = element["Priority"]
                    # turn it into a string
                    priorityString = str(priority)
                    # if it's only one character, pad it out to two
                    if len(priorityString) == 1:
                        priorityString = " " + priorityString
                    # add it to string representation
                    stringRepresentation = stringRepresentation + priorityString

                # now we put in one more space for formatting
                stringRepresentation = stringRepresentation + " "

            # append to the list of strings
            listOfStrings.append(stringRepresentation)

        else:
            # the hour isn't present, so append an empty string and move on
            listOfStrings.append("")

    # do the return
    return listOfStrings


def createHTMLVisualisation(visualiserDict):
    """
    returns a string holding the HTML for a table showing the visualisation
    """

    # set up the list of strings - we'll use this to assemble each row separately
    listOfStrings = []
    # set up a list of days - we can use this to get the day from the serial hour
    dayList = ["Wed", "Thu", "Fri", "Sat", "Sun"]
    # set a value for the earliest reasonable start time - we use this to tidy up the table
    earliestReasonableStartTime = 8

    # work through all of the hours
    for hour in range(0, 24*5):
        ## first figure out the day & time
        # use floor division to get the index of the day by dividing by 24 & rounding down
        dayOfWeek = dayList[hour // 24]
        # use mod to get the remainder, which is the hour
        hourOfDay = hour % 24
        # turn that into a day and time string, padding the hour if needed so that 9 becomes 09:00 & 10 is 10:00
        if len(str(hourOfDay))==1:
            dayAndTime = f"{dayOfWeek}0{str(hourOfDay)}:00"
        else:
            dayAndTime = f"{dayOfWeek}{str(hourOfDay)}:00"
        
        ## now start building the table row
        # is the hour in visualiser dict?
        if str(hour) in visualiserDict.keys():
            ## we're going to build up a string representing this list, with an empty cell for None and the priority & name where there's an event
            # set up the string
            stringRepresentation = ""
            # get the list
            hourList = visualiserDict[str(hour)]
            # work through the list
            for element in hourList:
                # is element None or is there an event dict?
                if element is None:
                    # add an empty cell & a new line
                    stringRepresentation = stringRepresentation + "<td></td>\n"
                else:
                    # get the priority & name
                    priority = element["Priority"]
                    name = element["Name"]
                    # get hours occupied
                    hoursOccupied = element["HoursOccupied"]
                    # build a string for the contents of the table cell
                    cellContentsString = f"{str(priority)}<br><b>{name}</b>"
                    # add the system if there is one
                    if "System" in element.keys():
                        system = element["System"]
                        cellContentsString = f"{cellContentsString}<br><i>{system}</i>"
                    
                    ## if this is a multi-hour event, we need to do some more steps to make the cell fill multiple hours
                    # is it a single hour event?
                    if len(hoursOccupied) == 0:
                        # add it to string representation as a cell
                        stringRepresentation = stringRepresentation + f"<td>{cellContentsString}</td>" + "\n"
                    else:
                        # it's a multiple hour event - is this the first hour? does the first hour in the hours occupied list hatch the hour of the row?
                        if hoursOccupied[0] == hour:
                            # get the length of the hours occupied list
                            numberOfHours = len(hoursOccupied)
                            # add a rowspan to the cell when adding it to the string representation
                            stringRepresentation = stringRepresentation + f'<td rowspan="{numberOfHours}" style="background-color:linen;color:black;">{cellContentsString}</td>' + "\n"
                        else:
                            # it's a subsequent hour, so we can ignore it
                            pass

            # adding the day & hour at the start of the row
            stringRepresentation = f"<td>{dayAndTime}</td>" + "\n" + stringRepresentation
            # wrap the string in <tr> tags
            stringRepresentation = f"<tr>{stringRepresentation}</tr>"
            # append to the list of strings
            listOfStrings.append(stringRepresentation)

        else:
            # the hour isn't present, but we're going to check to see whether we can skip the row entirely
            # if this is on a wednesday, or it's before 8am, then we can probably skip this & make the table more tidy

            # check the day first
            if dayOfWeek == "Wed":
                # skip this one
                continue

            # check the start time
            if hourOfDay < earliestReasonableStartTime:
                # skip this one
                continue

            # append a row with just the day & hour
            listOfStrings.append(f"<tr><td>{dayAndTime}</td></tr>")

    # set up a return string by joining the list elements on a newline
    returnHTMLString = "\n".join(listOfStrings)

    # add <table> tags
    returnHTMLString = '<table style="width:100%">' + "\n" + returnHTMLString + "</table>"
    # add a style
    returnHTMLString = "<style>table, th, td {border:1px solid black;border-collapse: collapse;}</style>" + returnHTMLString

    # do the return
    return returnHTMLString


def createHTMLPage(visualiserHTML):
    """
    creates an HTML page as a string containing the passed-in table
    """

    # set up a template to wrap it in - there's probably a better way to do this
    templatePartOne = """<!DOCTYPE html>
    <html>
    <style>
    table, th, td {
    border:1px solid black;
    }
    </style>
    <body>
    <h2>Gen Con Wishlist</h2>"""
    templatePartTwo = """</body>
    </html>
    """

    # build a return string
    returnString = templatePartOne + "\n" + visualiserHTML + "\n" + templatePartTwo

    # do the return
    return returnString


def writeToHTML(htmlPage):
    """
    write out an html page to the results folder
    returns the filepath
    """

    # figure out the folderpath, based on the location of this file
    scriptFolderpath = os.path.dirname(__file__)
    resultsFolderpath = os.path.join(scriptFolderpath, "results")

    # find a valid filepath - does "test" not already exist?
    if os.path.isfile(os.path.join(resultsFolderpath, "test.html")) == False:
        htmlFilepath = os.path.join(resultsFolderpath, "test.html")
    else:
        # need to find a suffix that'll work - set up a suffix
        suffix = 1
        # keep adding numbers to the end until there's a valid name
        while os.path.isfile(os.path.join(resultsFolderpath, f"test{str(suffix)}.html")) == True:
            # not a valid name because the suffix is already in use - increment by one and try again
            suffix = suffix + 1
        # if we're at this point, we have a valid suffix = build the filepath
        htmlFilepath = os.path.join(resultsFolderpath, f"test{str(suffix)}.html")

    # write the html page out
    with open(htmlFilepath, 'w') as htmlFile:
        htmlFile.write(htmlPage)

    # return the filepath
    return htmlFilepath


# ---------- main logic starts here ----------

if __name__ == "__main__":
    # build the list of event lists by parsing each page
    pageOneListOfEventLists = wishlistTextToListOfEventLists(rawWishlist.pageOne)
    pageTwoListOfEventLists = wishlistTextToListOfEventLists(rawWishlist.pageTwo)
    # combine the lists into one
    listOfEventLists = pageOneListOfEventLists + pageTwoListOfEventLists

    # get a list of event dicts
    listOfEventDicts = listOfEventListsToListOfEventDicts(listOfEventLists)

    # add event hours to the event dicts
    listOfEventDicts = addEventHours(listOfEventDicts)

    # create a dict of lists, one for each hour where there's an event
    visualiserDict = createWishlistVisualiserDict(listOfEventDicts)

    # # create & display a quick and dirty representation to see whether it worked
    # qdVisualisation = createQuickAndDirtyVisualisation(visualiserDict)
    # for row in qdVisualisation:
    #     print(row)

    # create an HTML table from the visualiser dict
    visualiserHTML = createHTMLVisualisation(visualiserDict)

    # use the table to create an HTML page
    htmlPage = createHTMLPage(visualiserHTML)

    # create an html document
    htmlFilepath = writeToHTML(htmlPage)

    # display the document in a browser
    print(str(htmlFilepath))
    webbrowser.open_new_tab(htmlFilepath)