from bs4 import BeautifulSoup
import json

res = open('extractions.json', 'w')
i = 0
res.write('[\n')
while i < 600:
    file = open('data/scrape_page' + str(i) + '.html', 'r')

    soup = BeautifulSoup(file, "lxml")
    lis = soup.findAll('li', 'regular-search-result')

    for ele in lis:
        data = {}
        leftPart = ele.findAll('div', 'media-story')[0]
        data['name']  = leftPart.h3.span.a.span.string
        data['rating'] = leftPart.findAll('i')[0]['title']
        data['reviews'] = leftPart.findAll('span', 'review-count')[0].string.strip()
        if len(leftPart.findAll('span', 'price-range')):
            data['price'] = leftPart.findAll('span', 'price-range')[0].string
        data['category'] = leftPart.findAll('span', 'category-str-list')[0].a.string
        rightPart = ele.findAll('div', 'secondary-attributes')[0]
        if len(rightPart.findAll('address')):
            address =  rightPart.findAll('address')[0].contents
            if len(rightPart.findAll('span', 'neighborhood-str-list')):
                data['address-alias']= rightPart.findAll('span', 'neighborhood-str-list')[0].string.strip()
            data['address-street'] = address[0].strip()
            data['address-city'] = address[-1].strip()
        data['phone'] = rightPart.findAll('span', 'biz-phone')[0].string.strip()
        json_data = json.dumps(data)
        res.write(json_data + '\n')
    file.close()
    i += 1

res.write(']')
res.close()