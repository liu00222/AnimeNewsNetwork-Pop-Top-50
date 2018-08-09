# Anime News Network
library(RCurl)
library(XML)

# Define the http header
header = c(
  "User-Agent"="Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
  "Accept"="text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Language"="en-us",
  "Connection"="keep-alive",
  "Accept-Charset"="GB2312,utf-8;q=0.7,*;q=0.7"
)

# Simulate the access
url = "https://www.animenewsnetwork.com/encyclopedia/ratings-anime.php?top50=popular"
webpage = getURL(url,httpheader=header)

# Manage the html tree structure
pagetree = htmlTreeParse(webpage,encoding="UTF-8", error=function(...){}, useInternalNodes = TRUE,trim=TRUE)

# Locate the node
xpath = getNodeSet(pagetree, "//td//a[@href]/text()")
info = sapply(xpath,xmlValue) 
info