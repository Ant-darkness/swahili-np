
# Swahili NLP

Python utilities for Swahili text preprocessing.

## Features

- Retrieve Swahili stopwords
- Remove stopwords from text

## Usage

```python
from swahili_nlp import get_stopwords, remove_stopwords

stopwords = get_stopwords()

text = "Mimi ninapenda kujifunza Kiswahili na Python"

print(remove_stopwords(text))
```

## Data sources

The baseline stopwords list is based on:
https://github.com/stopwords-iso/stopwords-sw

Please see the source repository for its license
and attribution requirements.
