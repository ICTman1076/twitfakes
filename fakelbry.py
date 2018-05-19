from tweepy import API, OAuthHandler
import json
import string
printable = set(string.printable)

config={}
with open("config/data.json") as f:
    config=json.loads(f.read())
with open("config/auth.json") as f:
    authdata=json.loads(f.read())

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section

auth = OAuthHandler(authdata['consumer_key'], authdata['consumer_secret'])
auth.set_access_token(authdata['access_token'], authdata['access_token_secret'])
authdata={}
authdata="authdata's been wiped. Don't try to gain access this way!"

api = API(auth)

def checkfake(u):
    html="<h2><a href='https://twitter.com/"+u.screen_name+"' target='_blank'>"+u.screen_name+"</a></h2>"
    try:
        if u.screen_name != config['official']:
            retweets=0
            safe=True
            print(u.screen_name)
            userposts=api.user_timeline(u.id)
            for j in userposts:
                for k in config['pointsmeanprizes']:
                    if k in j.text.lower():
                        if j.text[:4] == "RT @" and config['ignoreretweets']:
                            retweets+=1
                        else:
                            print("^^ POSSIBLE SCAMMER! ^^")
                            print(j.text)
                            html+="<p><b>DETECTED:</b> "+j.text+"</p>"
                            safe=False
            if retweets<0:
                html+="<p>Number of retweets including keywords: "+str(retweets)+"</p>"
            if safe:
                html+="<p>Seems to be ok.</p>"
    except:
        print("Acc is private or other issue")
        html+="<p>There was issues getting the account's data - Account is probably private.</p>"
    return html

while True:
    cmd=input("home> ")
    with open("ratelimits.json","w") as f:
        f.write(json.dumps(api.rate_limit_status()))
    if cmd == "auto" or cmd == "a":
        dealtwith=[]
        html="<h1>REPORT</h1><br/>"
        by=input("Search by [R]ecent replies or [S]earch bar?\nsrch> ").lower()
        if by=="s":
            dealtwith=[]
            for p in range(1,11):
                lbryusers = api.search_users("LBRY",20,p)
                for i in lbryusers:
                    if i in dealtwith:
                        print("Not unique")
                    else:
                        html+=checkfake(i)
                        dealtwith.append(i)
                cont=input("[N]ext page or [C]ancel/[F]inish?\npage> ").lower()
                if cont == "c" or cont == "f":
                    break
        elif by=="r":
            dealtwith=[]
            userposts=api.search("@"+config['official'],rpp=100)
            for i in userposts:
                if i.user.id in dealtwith:
                    print("Not unique")
                else:
                    html+=checkfake(api.get_user(i.user.id))
                    dealtwith.append(i.user.id)
            print("Gone through 100 tweets, the max I can do.")
        with open("report.html","w") as f:
            f.write(html.encode("ascii", errors="ignore").decode())
        print("In the same directory as you ran me in, I have created a report.html file.")
        print("It pretty-prints the results above. I recommend you use that instead of the mess above.")
    elif cmd == "manual" or cmd == "m":
        name=input("Enter their @username, without the @\nname> ")
        if name != config['official']:
            userposts=api.user_timeline(name)
            for j in userposts:
                for k in config['pointsmeanprizes']:
                    if k in j.text.lower():
                        print("^^ POSSIBLE SCAMMER! ^^")
                        print(j.text)
