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

## Licensing

The licensed used for the is the Adaptive Public License. You may see it in full in the `LICENSE.txt` file. Here is a summary:

### You may:
- Distibute and modify this project
- Use this project commercially and/or privately
- Place a warranty on this project

### You MUST:
- Include the License AS-IS in LICENSE.txt
- Include this notice at the beginning of all source code files:
```
THE LICENSED WORK IS PROVIDED UNDER THE TERMS OF THE ADAPTIVE PUBLIC LICENSE ("LICENSE") AS FIRST COMPLETED BY
ICTman1076. ANY USE, PUBLIC DISPLAY, PUBLIC PERFORMANCE, REPRODUCTION OR DISTRIBUTION OF, OR PREPARATION OF 
DERIVATIVE WORKS BASED ON, THE LICENSED WORK CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS LICENSE AND ITS TERMS,
WHETHER OR NOT SUCH RECIPIENT READS THE TERMS OF THE LICENSE. "LICENSED WORK" AND "RECIPIENT" ARE DEFINED IN THE
LICENSE. A COPY OF THE LICENSE IS LOCATED IN THE TEXT FILE ENTITLED "LICENSE.TXT" ACCOMPANYING THE CONTENTS OF 
THIS FILE. IF A COPY OF THE LICENSE DOES NOT ACCOMPANY THIS FILE, A COPY OF THE LICENSE MAY ALSO BE OBTAINED AT
THE FOLLOWING WEB SITE: https://ictman1076.github.io/twitfakes

Software distributed under the License is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either
express or implied. See the License for the specific language governing rights and limitations under the License.
```
- Disclose the source code
- State any significant changes made to the source code
- Give credit to the author, ICTman1076 (https://ictman1076.github.io). It would be nice if you would credit other major
contributors, too, or even link to this repository or the official website.

### You MAY NOT:
- Hold any contributor liable for damages
- Use contributor's names, trademarks or logos without written permission - i.e., this license does NOT license you to any
trademarks owned or licensed to the contributors, nor that of LBRY, inc.
