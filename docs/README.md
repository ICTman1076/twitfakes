# twitfakes
Get rid of those Fake Twitter Twits.

This is a simple python script to auto-detect and report back people who are potential twitter account copycats.
The config and auth file are example files, and are there to give the basic framework of the config file to make
it easier to set up. Currently, they are setup to detect fakes for [@LBRYio](https://twitter.com/LBRYio), the
account this was designed for, but you can set it up for something else.

**You can access the repository at https://github.com/ICTman1076/twitfakes** - it's open source!

## Installation

To install, go to xyz.

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

## Licensing

The licensed used for the is the Adaptive Public License. You may see it in full in the `LICENSE.txt` file. A summary is
available at xyz.
