# AI Boggle Solver ✅
boggle solver powered by artificial intelligence! ⚡

Boggle is a game played on a 5 by 5 grid of letter where the purpose is to find as many connected words.

![A boggle game board](./media/boggle.jpg "A boggle game board")

A connected words is a sequence of contiguous letter touching in all possible 8 direction forming a word where letters cannot repeat!

There is a time limit for how long you have to find the maximum amount of words (2min). 

Players get points for every unique word they get compared to the others. The longer the word the more point!


## Current State - Dynamic Programming + Trie
Currently here is what the program needs to be run:
- run `sudo snap install curl`
- run `./setup.sh` which will download an [english dictionary]((https://github.com/dwyl/english-words/blob/master/words_alpha.txt))
- run `python3 -m venv .venv`
- run `source ./.venv/bin/activate`
- run `pip install -r requirements.txt`
- run `python src/main.py BOGGLE_FILE` which will brute force find all the words

the `BOGGLE_FILE` needs to have the same format as the one in the `assets/` folder:
```
n,y,r
n,o,a
o,r,s
```

## License
MIT