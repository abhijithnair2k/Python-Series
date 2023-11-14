from textblob import TextBlob



blob= TextBlob("this is my city.ANd I love it all from my heart")
sw = ("man","woman","he")
pw = ("ants","dog","peacock")

print(blob.detect_language())




