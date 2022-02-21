# PinterestScraper
 
Use Firefox (geckodriver) for selenium, Chromedriver crash with Pinterest. Also cant get high resolution image without login in pinterest. Cant dig deep (pinterest stoop scroll page), but enough to get few thouthand pictures by tag.

# How to

Download the geckodriver from https://github.com/mozilla/geckodriver/releases

copy it in your path (eg: `/usr/local/bin/` on mac)

Install the dependencies by running `pip install -r requirements.txt`

Run list-dir.py to collect all scrapped files in shortcodes.xls (to prevent for dublicates)

Run PinterestScraper.py (in file can setup list of hashtags to scrap and how many pages)

After PinterestScraper.py finish run savePhotos.py to save photos in the defined folder.

Dont forget to create directories for scrapping (_result_files, _scrapped) or the name defined in files
