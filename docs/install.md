# Installing Twitfakes

First, download all the files in the repo. Then open up a console window, and change directory to
where you extracted the files and run `pip install -r requirements.txt`.

Next, you'll need to [create a Twitter app](https://apps.twitter.com/), to get the necessary API keys. It doesn't
particularly matter what the exact details of it are, you just need to **create the app, then go to the "keys and
access tokens" tab.** You'll see the consumer key and secret. **Fill in these keys in `config/auth-example.json`.**

Now, go back to the keys and access tokens page and scroll down a bit. You'll see a section entitled "Your access
token". There should be a button to generate a token and secret. **Generate an access token and secret, then fill it
in to `config/auth-example.json`.**

Now, **rename `auth-example.json` to `auth.json`.** Authentication is now set up. Time to set up the `data.json` file.

## The `config/data.json` file

Go to `config/data.json`. You'll see a json-formatted file. Here's what each bit means:

`official` - the @username of the official account that your scanning for fake duplicates of. DON'T INCLUDE THE `@`!

`searchfor` - used in automatic scanning by searchbar - the script will search for whatever you put in there and use
the data that returns.

`pointsmeanprizes` - keywords that should return a positive. As set up currently, it scans for fake accounts advertising
(likely fake) giveaways.

`ignoreretweets` - boolean to tell the script whether or not it should include retweets with the keywords.
