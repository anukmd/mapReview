# mapReview

Packages to install

Selenium with 'pip3 install selenium'
BeautifulSoup with 'pip3 install beautifulsoup4'

ChromeDriver
- Download relevant chromedriver version from here - https://sites.google.com/a/chromium.org/chromedriver/downloads
- Add to PATH (Ubuntu move to /usr/bin via commands below)
-  unzip chromedriver_linux64.zip
-  sudo mv chromedriver /usr/bin/chromedriver 
-  sudo chmod +x /usr/bin/chromedriver 


Scrollable Div 
- This gets updated by Google frequently. So needs to be updated if code is throwing an error on line 47.
- Go to any google location -> click on reviews -> on reviews page find the scrollable element -> 'inspect' -> right click on div element -> 'Copy-'CopyXpath'-> replace the path in line 47
