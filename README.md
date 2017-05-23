[![Code Health](https://landscape.io/github/PowerSlime/AliExpressItem/master/landscape.svg?style=flat)](https://landscape.io/github/PowerSlime/AliExpressItem/master)
<img src="https://raw.githubusercontent.com/PowerSlime/AliExpressItem/master/logo.png" alt="AliExpressItem by PowerSlime"><br>
# AliExpressItem
<p>It's my simple parser for lot on AliExpress... With him you can get some information about item without using any tokens and accounts.</p>

# Requiremets 
<p>You should use <b>Python 3</b><br>
Libraries: <b>re, urllib</b></p>

# How to use
<pre>
<code>import Ali
item = Ali.AliExpressItem(url)
item.METHOD()</code></pre>


# AVIABLE METHODS
<ul>
	<li>getId</li>
	<li>getName</li>
	<li>getPrice</li>
	<li>getRating</li>
	<li>getOrders</li>
	<li>getImageUrl</li>
	<li>getGalleryUrl</li>
	<li>getGalleryImages</li>
	<li>downloadImage([url][,filename])</li>
</ul>

# P.S.
<p>So... This code is shitty a little :) But... If anyone need to get product's info from an AliExpress <b>product's</b> page - I'll be happy, if you will use my lib ;)</p>
<p><b>Thanks</b></p>
