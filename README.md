# Rust Item & Skin Scraper
A quick and dirty scraper that fetches items and their skins.

## How To Use
Ensure you have Python installed and then do the following:

```
pip install -r requirements.txt
python main.py
```

Then a file called `output.json` should appear containing the items and their skins.

## Known Issues
If a section is added underneath the current skins section on the scraped site,
then the scraper will likely fail.
