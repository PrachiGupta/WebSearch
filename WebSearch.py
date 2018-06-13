from newspaper import Article
import nltk

# Get the keywords from an url
def getKeyWordsFromUrl(url):
    article = Article(url)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()
    return article.keywords


#sample to extract keywords from a url
if __name__ == '__main__':
    url = "https://www.tutorialspoint.com/python/python_functions.htm"
    keywords = getKeyWordsFromUrl(url)
    print(keywords)
