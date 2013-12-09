RPi-Twitter-GetUserTimeline-Tutorial-Python
===========================================

Some simple demo code that shows use of get_user_timeline() Twitter API function used to control RPi

This code borrows some material from http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/

Install Twython
===============
<pre class="code-text-only" style="display: none;">
<code>sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install twython</code></pre>

Register Twitter App
====================
In order to use the Twitter API – that is, the REST interface that we’ll use to post new Tweets and generally interact with Twitter outisde of the twitter website – we’ll need to register a new app.

Do that from this link, https://dev.twitter.com/apps/new – you needn’t specify a callback URL, and just make up a website if you want.

<img src ="http://main.makeuseoflimited.netdna-cdn.com/wp-content/uploads/2013/08/new-twitter-app.jpg">

You’ll see something resembling this once you’re done – these keys are unique to you.

<img src ="http://main.makeuseoflimited.netdna-cdn.com/wp-content/uploads/2013/08/twitter-app.jpg">

By default, the app is set to read-only, so we won’t be able to publish tweets without changing that to Read and Write. Go to the Settings tab and change the Application type.

<img src ="http://main.makeuseoflimited.netdna-cdn.com/wp-content/uploads/2013/08/readwrite-access.jpg">

Once saved, head back to the Details tab and click the button at the bottom to create an OAuth access token – this gives your application access to your own Twitter account. Refresh, and leave the page open for later – we’ll need to copy paste some of those keys in a minute.

<img src ="http://main.makeuseoflimited.netdna-cdn.com/wp-content/uploads/2013/08/access-token.jpg">
