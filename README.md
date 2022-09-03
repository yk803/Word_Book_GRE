# Word_Book_GRE

This repository is designed for building up one's own vocabulary book. You can use the jupyter notebook to add new words to the "book." You can also search for words in the book you create.

## How to use it

First download the code to the local machine by entering the following code in terminal:

```
git clone https://github.com/yk803/Word_Book_GRE.git
```

Next, open the jupyter notebook (need to have jupyter notebook installed on the computer!) and follow the instructions to add new words).


To look up for a word, run the following line in terminal by replacing `WORD` with the actual word you are looking for. This line of code is also attached at the end of the jupyter notebook:

```
python word_search.py WORD
```

(Note: only add the exclamation mark at the front when executing in jupyter notebook)

## TODO
- [ ] Add number of counts for words not remembered
- [ ] Make words that already exist modifiable (instead of overwriting it)
- [ ] List all words in the vocabulary book in a sorted way
