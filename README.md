# twitfakes
Get rid of those Fake Twitter Twits.

This is a simple python script to auto-detect and report back people who are potential twitter account copycats.
The config and auth file are example files, and are there to give the basic framework of the config file to make
it easier to set up. Currently, they are setup to detect fakes for [@LBRYio](https://twitter.com/LBRYio), the
account this was designed for, but you can set it up for something else.

## Installation

First, you'll need to [create a Twitter app](https://apps.twitter.com/), to get the necessary API keys. It doesn't
particularly matter what the exact details of it are, you just need to **create the app, then go to the "keys and
access tokens" tab.** You'll see the consumer key and secret. **Fill in these keys in `config/auth-example.json`.**

Next, go back to the keys and access tokens page and scroll down a bit. You'll see a section entitled "Your access
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

## Running the script

This runs in the command lime. The first prompt is `home> ` - this accepts the commands:

Command  | Description                       | aliases
-------- | --------------------------------- | -------
`auto`   | Start the autoscanning wizard     | `a`
`manual` | Start the scan-by-username wizard | `m`

The wizard from thereonin is self-explanatory - when presented with an option, use the letter in square brackets, e.g. in

```
Search by [R]ecent replies or [S]earch bar?
```

you woud respond with `R` to scan by recent replies, or `S` to scan by search.
