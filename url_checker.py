import requests
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

def fetch_and_process_content(url):
    """Fetch website content and preprocess."""
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    text_content = ' '.join(tag.string.strip() for tag in soup.find_all(text=True) if tag.parent.name not in ['script', 'style'] and tag.string.strip())
    return preprocess_text(text_content)

def preprocess_text(text):
    """Preprocess text by removing stopwords and stemming."""
    stemmer = SnowballStemmer('english')
    stop_words = set(stopwords.words('english'))
    text = text.lower()
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    tokens = word_tokenize(text)
    stemmed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    return ' '.join(stemmed_tokens)

def check_for_offensive_keywords(text):
    """Check text for offensive keywords and return them."""
    offensive_keywords = [
        'abuse', 'aggression', 'angry', 'annoy', 'assault', 'attack', 
        'bad', 'bastard', 'beast', 'bigot', 'bitch', 'bully', 'cancer', 
        'cocksucker', 'crap', 'cunt', 'damn', 'degenerate', 'demon', 
        'dick', 'douchebag', 'drunk', 'evil', 'fail', 'faggot', 
        'foul', 'freak', 'fuck', 'fucking', 'garbage', 'gay', 
        'ghetto', 'hate', 'hateful', 'horrible', 'hostile', 'idiot', 
        'ignorant', 'ill', 'immoral', 'incompetent', 'insult', 
        'intimidation', 'jerk', 'kill', 'killing', 'liar', 'loser', 
        'manipulate', 'moron', 'murder', 'nasty', 'neglect', 'obscene', 
        'offensive', 'outrage', 'pervert', 'piss', 'prick', 'punk', 
        'rape', 'racist', 'retard', 'rude', 'sadistic', 'scum', 
        'slap', 'slur', 'slut', 'stupid', 'sucker', 'troll', 
        'turd', 'twat', 'vandal', 'vile', 'violence', 'violent', 
        'weirdo', 'whore', 'wimp', 'wretched', 'zealot', 'hate speech',
        'bigotry', 'intolerance', 'misogyny', 'sexism', 'homophobia', 
        'xenophobia', 'harassment', 'disrespect', 'derogatory', 
        'profanity', 'slander', 'dox', 'toxic', 'discrimination', 
        'obnoxious', 'defame', 'disparage', 'victimize', 'malicious'
    ]
    
    found_keywords = [keyword for keyword in offensive_keywords if keyword in text]
    return found_keywords

def main():
    url = input("Enter a URL: ")
    if url:
        processed_text = fetch_and_process_content(url)
        offensive_words = check_for_offensive_keywords(processed_text)
        if offensive_words:
            print("Offensive Words Found:")
            print(', '.join(offensive_words))  # Print only the offensive words
        else:
            print("No offensive words found.")

if __name__ == '__main__':
    main()
