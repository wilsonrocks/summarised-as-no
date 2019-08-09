# @summarisedasno

## running
```
  python scrape.py
```

## about

Since reading [http://smbc-comics.com/comic/2010-11-26], I've always been annoyed by articles with a question title that can be summarised as No.

I decided to make a twitter account to highlight them.

This is the script used to source articles for the [https://twitter.com/summarisedasno] account.

It's written in python and uses Beautiful Soup and the requests library.

It scrapes a number of websites, looks for links with a ? symbol at the end of the text, and which start with certain words (do, does, has, etc.)

It then emails them to me, where I curate them before adding the worthwhile ones to Buffer to be tweeted out. It also tracks which urls have been sent in a sqlite database to avoid duplication.



## improvements

Feedback, pull requests welcome.

Maybe one day, it will use MACHINE LEARNING to decide what to tweet itself and I can hand over completely to it?