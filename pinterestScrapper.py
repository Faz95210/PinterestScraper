from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import re
from urllib.request import urlopen
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
import glob

# dirrectory where to save files with info
directory_path = '_results_files'

# path to chrome driver
#browser = webdriver.Chrome('/Users/vasily/Documents/00_PYTHON/InstaScrapper/chromedriver')
browser = webdriver.Firefox()

# print(len(links))

# how many pages scrap
n_pages = 70
# list of hashtags / usernames
name_list = ['tattoo sketch', 'tattoo geometry', 'tattoo flash', 'tattoo design', 'tattoo ideas', 'tattoo drawings', 'tattoo sketches', 'tattoo minimal']
#name_list = ['liwenliang']
# , 'selfiestick', 'selfiequeen'
# save info each ... (in case of bad connection orsome error during scrapping better do not wait till last / 
# also easier to stop script if you want without loosing all data)
save_after = 100


def scrollPage(name, n_pages = 1, save_after=100):

    # read the file with images we already parsed (use list_dir.py to create ths file first)
    shortcodes = pd.read_csv('shortcodes.csv')

    #do not replace already existing files
    cur_file = 0
    files = glob.glob("{}/{}_*".format(directory_path,name), recursive=True)
    print("FILES with {} - {}".format(name,len(files)))
    cur_file = len(files)

    result=pd.DataFrame()

    print("PAGE     : 0")

    Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.execute_script("document.body.style.zoom='zoom 50%'")
    '''
    source = browser.page_source
    data=bs(source, 'html.parser')
    body = data.find('body')
    for link in body.findAll('img'):
        q = link.get('srcset')
        q = q.split(', ')
        q = q[-1]
        #print(q)
        q = q.split(' ')[0]
        m = shortcodes.isin([q]).any()
        cols = m.index[m].tolist()

        new = pd.DataFrame([q], columns=['shortcode'])
            
        # if not
        if len(cols) == 0:
            result = result.append(new)
        else:
            print('{}   {}  Already parsed'.format(i, q))

    result = result.drop_duplicates(subset = 'shortcode')
    result.to_csv('{}/{}_{}.csv'.format(directory_path, name, cur_file))
    print('-' * 30)
    print("FILE SAVED     : {}_{}.csv".format(name, cur_file))
    cur_file += 1

    result=pd.DataFrame()
    '''
    time.sleep(5) 

    if n_pages > 1:
        for i in range(n_pages-1):
            print("PAGE     : {}".format(i+1))
            Pagelength = browser.execute_script("window.scrollTo(document.body.scrollHeight/2, document.body.scrollHeight);")

            time.sleep(2) 

    source = browser.page_source
    data=bs(source, 'html.parser')
    body = data.find('body')
    for link in body.findAll('img'):

        n = 0

        try:

            q = link.get('srcset')
            q = q.split(', ')
            q = q[-1]
            q = q.split(' ')[0]
            m = shortcodes.isin([q]).any()
            cols = m.index[m].tolist()

            new = pd.DataFrame([q], columns=['shortcode'])
            
            # if not
            if len(cols) == 0:
                result = result.append(new)
                n += 1

                if n > save_after:
                    result = result.drop_duplicates(subset = 'shortcode')
                    result.to_csv('{}/{}_{}.csv'.format(directory_path, name, cur_file))
                    print('-' * 30)
                    print("FILE SAVED     : {}_{}.csv".format(name, cur_file))
                    cur_file += 1
                    result=pd.DataFrame()
                    n = 0
            else:
                print('{}  Already parsed'.format(q))

        except:
            pass

    result = result.drop_duplicates(subset = 'shortcode')
    result.to_csv('{}/{}_{}.csv'.format(directory_path, name, cur_file))
    print('-' * 30)
    print("FILE SAVED     : {}_{}.csv".format(name, cur_file))
    cur_file += 1
    result=pd.DataFrame()

    

def pinterestScrapper( name_list, n_pages, save_after=100):
    
    for name in name_list:
        print(' ')
        print('-' * 30)
        print("PARSING NAME     : {}".format(name))
        hashtag = name
        browser.get('https://www.pinterest.com/search/pins/?q='+hashtag)
        
        scrollPage(name, n_pages, save_after)
            
pinterestScrapper( name_list, n_pages, save_after)