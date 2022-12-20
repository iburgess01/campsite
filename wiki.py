from bs4 import BeautifulSoup
import requests

url = "https://www.wikicamps.com.au/site/New+South+Wales+%2F+ACT/Campground/Tattersalls+Campground%2C+Karuah+National/66648"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


for siteName in soup.find_all('strong'):
    if siteName.parent.name == 'h2':
        name = siteName.text
       
main = soup.main
for siteType in main.find('h4'):
    type = siteType.text

for siteRating in main.find('p'):
    rating = siteRating.strip()
    

siteDiv = soup.find('div', class_='col-12 col-lg-6')
for p_element in siteDiv.find('p'):
    location = p_element
for a_element in siteDiv.find('a'):
    phone = a_element



print(name)
print(type)
print(rating)
print(location)
print(phone)
for description in main.find(id="pdesc"):
    print(description.text.strip())









#for address in soup.find_all('p'):
#    if address.parent.name == 'div':
#        print(address.text)




# ------ RETURN ALL TEXT FROM BODY IN CLEAN FORMAT ------------------------------------------------------------
# this will return all the HTML from the main section of the webpage
#main = soup.main
#print(main.prettify())


# ------ RETURN CORRECT + FORMAT ------------------------------------------------------------------------------
# this will find and return the specific text in clean format
#for name in soup.find_all('strong'):
#    if name.parent.name == 'h2':
#        print(name.text)


# ------ RETURN BASIC + FORMAT --------------------------------------------------------------------------------
# this will find and return the first h2 element in clean format
# I think we might be able to use .text.strip() to return specific text from the return?
#lists = soup.find('h2').text
#print(lists)


# ------ RETURN ALL PARAGRAPH IN BODY + FORMAT ----------------------------------------------------------------
# this will find and return all p tags in the body and return in a clean format
#body = soup.body
#for paragraph in body.find_all('p'):
#    print(paragraph.text)


# ------ RETURN ALL DIV WITH CLASS ASSIGNED -------------------------------------------------------------------
# this will find and return ALL text (in clean format) from the defined div classes. Not really what we want
#for div in soup.find_all('div', class_='col-12 col-lg-10'):
#    print(div.text)