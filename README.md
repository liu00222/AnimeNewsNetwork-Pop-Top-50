# AnimeNewsNetwork-Pop-Top-50

_by << liu00222 >>_

This is a simple example of web scraping. I used both R and Python3 to illustrate how the related packages in these languages work. 

In the Python version, I just used some basic functions in BeautifulSoup and requests. I also export the data to a .csv file for later use. Also, since the URLs of the items are included in the source code, by iteratively making requests to each URL, I am able to dive deeper into these URLs to grab more information of each item, e.g. their directors, casts, creators, starting date, etc. This would make the features of each item richer and make the further analysis on the data be in-depth. 

In the R version, it makes use of RCurl and XML packages and has some good use of their functions to load the source code of the target page, and then search for the pattern that we aim at. From lines 6 to 12, I defined the http header. Then I simulated the access at lines 15 to 16, which just downloaded the sources code of the target. Then I modified the structure of the page tree to make the data stucture simpler to use. Finally, in the last 3 lines, I use the appropriate regular expression to find the location of the target data and then store them in the object called "info". In the last part, I just made use of the packaged functions and the searching efficiency is somewhat low, but it was enough for the small number of data. 
