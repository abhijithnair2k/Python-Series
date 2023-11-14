
from newspaper  import Article
import nltk
nltk.download('punkt')

url = input('enter the url')
# print(url)
article = Article(url)
article.download()
article.parse()
author=article.authors
print(author)
pub = article.publish_date
article.nlp()
keywords= article.keywords
summmary = article. summary
print("keywords:k" ,keywords)
print( "summary" ,summmary)








