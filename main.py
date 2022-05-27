
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import bs4
import pandas as pd


def get_review_summary(result_set):
    rev_dict = {'Review Rate': [],
                'Review Time': [],
                'Review Text': []}
    for result in result_set:
        review_rate = result.find('span', class_='kvMYJc')["aria-label"]
        review_time = result.find('span', class_='rsqaWe').text
        review_text = result.find('span', class_='wiI7pd').text
        rev_dict['Review Rate'].append(review_rate)
        rev_dict['Review Time'].append(review_time)
        rev_dict['Review Text'].append(review_text)

    return (pd.DataFrame(rev_dict))


def mainFunc():
    driver = webdriver.Chrome()

    # London Victoria & Albert Museum URL
    # url = 'https://www.google.com/maps/place/Victoria+and+Albert+Museum/@51.4966392,-0.17218,15z/data=!4m5!3m4!1s0x0:0x9eb7094dfdcd651f!8m2!3d51.4966392!4d-0.17218'
    # url = 'https://www.google.com/maps/search/bicycle+store/@51.5026862,-0.1430242,13z/data=!3m1!4b1'
    url ='https://www.google.com/maps/place/Flinders+Street+Railway+Station/@-37.8182711,144.9670618,17z/data=!3m1!4b1!4m5!3m4!1s0x6ad642b6af832249:0xe39e415e49a7c44e!8m2!3d-37.8182711!4d144.9670618'
    driver.get(url)

    #find review count
    page1 = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    # find text eg:'1,776 reviews' and take only '1,776'
    reviewCount = page1.find('button', class_='DkEaL')["aria-label"].split(" ")[0]
    # remove ',' and convert to int
    total_number_of_reviews = int(reviewCount.replace(',', '')) if ',' in reviewCount else int(reviewCount)
    # total_number_of_reviews = 1776

    #go to page with reviews
    driver.find_element(By.CLASS_NAME, "DkEaL").click()

    # Scroll as many times as necessary to load all reviews
    for i in range(0, (round(total_number_of_reviews / 10 - 1))):
    # for i in range(0,3):
        scrollable_div = driver.find_element(by=By.XPATH, value='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',scrollable_div)
        time.sleep(1)

    #get all reviews by class name
    review_class = 'jftiEf L6Bbsd fontBodyMedium'
    response = bs4.BeautifulSoup(driver.page_source, 'html.parser')
    reviews = response.find_all('div', class_=review_class)

    # add reviews to a dict
    rev_dict = get_review_summary(reviews)
    print(rev_dict)

    rev_dict.to_csv('Output/Reviews.csv')

    time.sleep(3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mainFunc()


