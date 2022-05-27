# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 22:29:20 2017

@author: Humphrey
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 22:53:42 2017

@author: Humphrey
"""

import pandas as pd
# import csv
# import requests
from bs4 import BeautifulSoup

###################
from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe')

totalReview = pd.DataFrame()
for i in range(5):  # Number of pages plus one
    url = "http://www.productreview.com.au/p/eden-brae-homes/" + str(i + 1) + ".html?rating=1"
    browser.get(url)
    print(url)

    reviewReadMore = browser.find_elements_by_class_name('review-read-more')
    for x in range(0, len(reviewReadMore)):
        if reviewReadMore[x].is_displayed():
            reviewReadMore[x].click()

    commentReadMore = browser.find_elements_by_class_name('comment-read-more')
    for x in range(0, len(commentReadMore)):
        if commentReadMore[x].is_displayed():
            commentReadMore[x].click()

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    #####################
    # page = requests.get("http://www.productreview.com.au/p/metricon.html?pr_front_review_filter%5Bbuild_location%5D=Queensland&rating=1&sort=&filter_action=filter#reviews")
    # soup = BeautifulSoup(page.content, 'html.parser')
    body = soup.find("body")
    headerParent = body.find_all("p", class_="review-labels")
    header = [ft.get_text() for ft in headerParent]

    # print(baa.prettify())

    titleParent = body.find_all("h3", itemprop="name")
    title = [pt.get_text() for pt in titleParent]

    comments = [sd.get_text() for sd in body.find_all("div", class_="review-overall")]

    threadParent = soup.find("div", class_="reviews")
    thread = [t.get_text() for t in threadParent.find_all("div", class_="discussion")]

    eql = len(comments) - len(header)
    for i in range(eql):
        header.append("No header")  # to make sure array sizes are equal

    header = [x.replace('\n', ' ').replace('\r', '') for x in header]
    title = [x.replace('\n', ' ').replace('\r', '') for x in title]
    comments = [x.replace('\n', ' ').replace('\r', '') for x in comments]
    thread = [x.replace('\n', ' ').replace('\r', '') for x in thread]

    review = pd.DataFrame({
        "aheader": header,
        "btitle": title,
        "comments": comments,
        "thread": thread
    })

    frames = [totalReview, review]
    totalReview = pd.concat(frames, ignore_index=True)

totalReview.to_csv(r'C:\Users\Humphrey\Desktop\WebScrape\Terrible\edenbraehomesTerribleReview.csv')