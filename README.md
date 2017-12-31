# Bot-Dylan
An LSTM recurrent neural net model trained to write song lyrics in the style of Bob Dylan. The model is trained on all of Dylan's lyrics which were scraped from bobdylan.com.  

"lyricScraper.py" is the script which does the scraping and outputs the results into "dylan_lyrics.txt".  

"dylanLyricGenerator.py" trains a multi-layered LSTM using the scraped lyrics. After each epoch, it outputs some example "fake" lyrics given a "seed" of a few words of input.  

"output.txt" shows what the output should look like.
