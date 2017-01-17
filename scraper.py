import requests

def scrape():
    i = 0;

    start_urls = [
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Los+Angeles,+CA',
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco,+CA',
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=New+York,+NY',
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Boston,+MA',
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Dallas,+TX',
        'https://www.yelp.com/search?find_desc=Restaurants&find_loc=Seattle,+WA'
    ]
    for start_page in start_urls:
        num = 0;
        while num < 1000:
            next_page = start_page + '&start=' + str(num)
            filename = 'data/scrape_page' + str(i) + '.html'
            getWebPage(next_page, filename)
            i += 1
            num += 10

def WebPageDownload(filename, content):
    ff = open(filename, 'w')
    ff.writelines(content)
    ff.close()

def getWebPage(url, filename):
    try:
        urlpage = requests.get(url)
    except IOError:
        print "IOError"
    WebPageDownload(filename, urlpage)

scrape()