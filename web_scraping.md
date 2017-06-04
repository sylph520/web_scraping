# Python Web Scraping
## Chapter 1. Introduction and basics
### Web Scraping Procedure

- Retrieving HTML data from a domain name
- Parsing that data for target information
- Storing the target information
- Optinally, moving to another page to repeat the process

### Connecting Reliably

`html=urlopen("http://www.pythonscraping.com/pages/page1.html")`

- probable errors
  - page not found on the server(HTTP error)
  - server not found(return None object)

```python
### HTTP error
try:
html=urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
print(e)
#return null, break, or do some other "Plan B"
else:
#program continues. Note: If you return or break in the
#exception catch, you do not need to use the "else" statement

### server not found
if html is None:
    print("URL is not found")
else:
    #program continues
```

```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
	print("Title could not be found")
else:
	print(title)
```

### `urllib` library

- `urlopen`()

  ```python
  from urllib.request import urlopen()#get the html
  #html.read() get the HTML content of the page
  #  HTML content -> BeautifulSoup object
  # bsObj = BeautifulSoup(html.read())
  ```


### BeautifulSoup library

#### findAll, find

```python
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywords)
```

- tag: tag name (or tag name list)
- attributes: python dict pairs
- recursive: default set to true
- text: match based on the text content of the tags(text = "example")
- limit: find x items from the page.
- keywords(example_tag_name = "example_attr")

#### get_text()

strips all tags from the document you are working with and returns a string containing the text only.

#### BeautifulSoup Objects

- BeautifulSoup objects(bsObj)
- Tag objects(retrieved in lists or by calling find and findAll on a bsObj)
- NavigableString objects(used to represent text within tags, rather than the tags themselves)
- Comment object(used to find HTML comments in comment tags, eg: <!--like this one-->)

#### Navigation Trees

##### children and descendants

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
for child in bsObj.find("table",{"id":"giftList"}).children:#  .descendants
	print(child)
```

##### next_siblings , previous_siblings

```python
# The BeautifulSoup next_siblings() function makes it trivial to collect data from
# tables, especially ones with title rows:
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
	print(sibling)
```

##### parent, parents

```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"
}).parent.previous_sibling.get_text())
```

### Regular Expressions and BeautifulSoup

```python
from urllib.request
import urlopenfrom bs4
import BeautifulSoupimport re
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
images = bsObj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
	print(image["src"])
```

### Accessing Attributes and lambda expressions

`myTag.attrs, eg: myImgTag.attrs['src']`

```python
soup.findAll(lambda tag: len(tag.attrs) == 2)

returns：
<div class="body" id="content"></div>
<span style="color:red" class="title"></span>
```

### lxml library and HTML Parser library

### Chapter2. Starting to Crawling



