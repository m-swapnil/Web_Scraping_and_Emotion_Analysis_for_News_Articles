# News Mining and Analysis

This project demonstrates how to mine news articles from the web, process the text, and extract meaningful insights using Python. The script performs text extraction, tokenization, sentiment/emotion analysis, and visualizations such as bar charts and word clouds.

---

## Features

- Scrape and process news articles using URLs.
- Extract and save article text, summary, and keywords.
- Clean and tokenize text data.
- Perform frequency analysis of tokens.
- Generate visualizations:
  - Bar charts for word frequencies.
  - Word clouds for overall, positive, and negative words.
- Perform emotion mining using `text2emotion`.
- Extract and visualize emotions present in the article.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.7 or above
- Required libraries:
  ```bash
  pip install newspaper3k text2emotion pandas matplotlib wordcloud scikit-learn nltk
  ```
- Stopword, positive, and negative word text files available at specific file paths.

---

## File Structure

```plaintext
.
|-- news_mining_analysis.py  # Main script
|-- News2804.txt            # Processed article text (generated at runtime)
|-- article51.txt           # Additional article output (optional)
```

---

## Script Workflow

### 1. **Scraping News Articles**
- The script uses `newspaper3k` to scrape articles from URLs.
- Extracted data includes the title, text, summary, and keywords.

### 2. **Text Processing**
- The text is cleaned to remove non-alphabetic characters.
- Tokenization is performed, and stopwords are removed.

### 3. **Frequency Analysis**
- Frequencies of tokens are calculated and visualized using bar charts.

### 4. **Word Clouds**
- Word clouds are generated for:
  - Overall words
  - Positive words (using a predefined list)
  - Negative words (using a predefined list)

### 5. **Emotion Mining**
- Uses `text2emotion` to capture emotions such as Happy, Angry, Surprise, Sad, and Fear.
- Bar charts display the intensity of emotions in the article.

---

## Configuration

1. Update the article URL(s) in the script:
   ```python
   url = 'https://timesofindia.indiatimes.com/...'
   ```

2. Ensure the following text files are available at specified paths:
   - Stopwords: `D:\Data\textmining\stop.txt`
   - Positive words: `D:\Data\textmining\positive-words.txt`
   - Negative words: `D:\Data\textmining\negative-words.txt`

---

## Usage

### Run the script
```bash
python news_mining_analysis.py
```

### Output
- Processed article text is saved in `News2804.txt`.
- Bar charts and word clouds are displayed during execution.
- Emotion analysis results are visualized.

---

## Example Visualizations

- **Bar Chart:** Token frequencies for the most frequent words.
- **Word Clouds:** Visual representation of word frequencies.
- **Emotion Analysis:** Bar chart for emotions in the text.

---

## References
- [Newspaper3k Documentation](https://newspaper.readthedocs.io/en/latest/)
- [Text2Emotion Documentation](https://pypi.org/project/text2emotion/)

---

## License
This project is licensed under the MIT License.
