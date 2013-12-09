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
