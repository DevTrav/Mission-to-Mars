# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set excecutable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# HTML parser setup
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# JPL Space Images Featured Images
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# Mars Facts
# Visit Mars facts URL
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)

# Scrape Mars profile table with DataFrame
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

df.to_html()

# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Find and click the full image button
# Find the hemisphere image element 
hemisphere_image_elem = browser.find_by_css('a.product-item img')

# For loop to iterate through image links
for i in range(4):
    hemisphere_dict = {}

    # Click thourgh to next hemisphere
    hemisphere_image_elem[i].click()

    # Grab href of image
    sample_link = browser.find_by_text('Sample').first

    # Save image to dictionary
    hemisphere_dict['image_url'] = sample_link['href']

    # grab title of hemisphere
    hemisphere_image_title = browser.find_by_css('div.cover h2.title').text

    # Save title to dictionary
    hemisphere_dict['img_title'] = hemisphere_image_title
    
    # Append hemisphere_image_urls list 
    hemisphere_image_urls.append(hemisphere_dict)

    #Click back to homepage
    browser.back()
# # Click Sample link to full image
hemisphere_image_urls

# Quit browswer after scrape
browser.quit()