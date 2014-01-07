Title: Web App Data Mining with Firebug Net Export and a dash of Python
Date: 2013-02-17 12:20
Tags: infosecdata, miningmetadata
Slug: web-app-data-mining-with-firebug-net_export-and-python
Author: William Culver
Summary: A guide to pull information from websites using browser plugins and then massaging that data into something useful with Python.

## Overview

We will be using some simple tools and some python code to capture XHR (XML Http Requests aka AJAX aka Javascript Request ) data, stream it all to a large dump file and then use some python to parse over the file, remove redundancy, scrape out all the juicy bits and then write it to a csv file which we could then put into a database ourselves. We overcome various problems along the way and what we end up with is probably a near perfect subset of a website's database beautifully reconstructed, and this demonstrates not only the extent of mine-able data that some companies' websites expose but also the ease of reconstruction using basic tools like a web browser and some python. The particular target is a map application that is supposed to show petrol station forecourt locations and some minor data on some attributes of that particular address such as fuel types sold etc, but what we will learn is that much more data and metadata is exposed.

## Background

We were recently tasked to create a large data set of petrol station forecourts. Our initial task was to compile a country wide data set of addresses but during our research we found much more data that we believe the website owner in focus did not intend to share with the world. Being a security focussed business we explored the extent of mine-able data and then notified the company of our findings with responsible disclosure. I am now sharing our findings along with a quick how to in the hopes that someone finds it helpful.
The Target

Shell UK (in fact this is their global website also) provide a nice 'Station Locator' web app which aims to help the public find a store within a vicinity of their choosing. This application is built on top of Google maps and is written by Geo.me solutions. (http://www.geo.me). The trouble is it exposes a lot more data than is provided to the end user via the application's user interface. We will show you that it is fairly trivial to harvest this data and programmatically run transforms on it. One other thing to note is that this application stores shell petrol station data for the entire world. For my purposes I was interested in the UK only but the same technique could be easily expanded to the entire globe given a lot more patience!

## Initial Analysis

A quick scroll around the map shows that at certain zoom levels, location pins showing each petroleum station at it's location. A mouse over event on this pin shows a pop up to the user showing the address and telephone number of the site. Clicking on the pin shows more detailed information such as basic services and amenities. What's interesting to note about this application is that as you zoom out there is a grouping algorithm that kicks in, that limits the amount of pins that can be displayed at any one time, presumably for overcrowding management. The pins are grouped into a single box with a single number that represents the amount of pins, as shown in the image below. Image showing the pins as mentioned above Image showing the grouping algorithm as mentioned above

## Web traffic

If we open up firebug or any other browser developer tool and take a look at the incoming XHR traffic we can see there are various things going on. At low altitude zoom levels we can see that as we pan around the application sends us a large dump of data every time we move so far off the screen that the application needs to load more pins. We can see that these are loaded in tiles similar to how google loads the underlying map data- i.e. there is an imaginary rectangle that is about twice the area of the viewport which is filled and as you scroll more than 50% of the viewport in any one direction a new XHR http request is made and a fresh tile of pins is downloaded. At higher altitude zooms the grouping algorithm kicks in and our browsers get given a lot less data (just an integer of the number of sites in each box). This of course makes sense as you would not like to download the entire worlds' data at once, but for our purposes it makes it a little harder to capture the data we want One more thing to note; another obstacle is that the grouping algorithm does not seem to be dependant on any one particular zoom level. It is purely dependant on the density of pins (petrol stations in this case) that are within the viewport. This means that for high urban areas such as London, you have to zoom in more to get the pins to show up.

## Data Analysis

Looking at the XHR response we can see that we get given a nice big JSON data set. Looking at this JSON data structure it becomes apparent quite quickly that there's a lot more stuff here than is required by the map application to function and there's various attributes of the petrol stations exposed that are not available to the end user via the user interface. Image showing a snippet of the data set we ended up with

## Data Mining
### Enter Firebug & Net Export

Okay so we know that panning around the map gives us small subsets of sites for a given map viewport regional area, and we have a rough intuition on the petrol station density that will trigger the grouping algorithm to kick in and take our data away. How can we put all this together and produce a set of data for say the whole of the UK?. This is where Net Export comes in. Net Export is a brilliant extension to Firebug by Jan Odvarko and can be found at http://www.softwareishard.com/blog/netexport/. It gives you the ability to dump to disk a series of XHR Responses in one go.

Using this tool we are able to simply pan around the map and capture all the XHR traffic that is sent back. This sounds like a tedious process but it only took me around 20 minutes to pan around the entire British Isles.

What you end up with is large JSON structured dump file of all the data. This file has a huge amount of redundancy due to the overlapping tiles nature of our panning. Mine was around 28 MiB as I was fairly conservative about my overlapping to make sure I didn't miss anything.

### A Sprinkle of python and we are done.

I wont get into the nitty gritty of python-fu as mine isn't all that great. This Gist https://gist.github.com/cedeon/6436167 shows you that it was simple enough to parse the data set completely and output a normalized csv file. Image showing the a snapshot of the final resulting csv file

## Conclusion

I didn't use the term 'Big Data' as it gets thrown around too much but in doing this exersize it's not hard to see why. In a few hours I was able to produce a full countries' worth of location data about petrol stations which include gps location, addresses, telephone numbers and a whole slew of attributes for each site that is not available to the web application itself. There are also various security risks exposed by this data set that expose meta data about the underlying database that, for responsible reasons, I don't want to get into. It's worth noting that there are various other sources online that can be cross compared with this data which reveal correlations and intersections and provide a lot more leverage to pry value out of this data set. Overall there were no real security nasties exposed by the web application but I hope this analysis goes a small part of the way to show companies that they should at least be wary of their data exposure. In this case a third party was used and it seems like a fairly lazy approach was taken when exposing the database data to the client side javascript running the web app. It's also worth noting that this extraneous data leakage is inefficient use of client browser bandwidth and server load. Furthermore there appeared to be no client restrictions in place that would stop the user from panning around the entire world in a more automated process; A simple session timer would help here.
