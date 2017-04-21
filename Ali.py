import re, urllib.request

def getHtml(url):
	return urllib.request.urlopen(url).read().decode('utf-8').replace('\n', '')

class AliExpressItem:
	'''
	import Ali
	item = Ali.AliExpressItem(url)
	item.METHOD()

	AVIABLE METHODS: getId, getName, getPrice, getRating, getOrders, getImageUrl, getGalleryUrl, getGalleryImages, downloadImage([url][,filename])
	'''
	def __init__(self, url):
		self.url = url
		self.galleryUrl = ''

		self.parsedHTML = ''
		self.parsedGallery = ''
		self.itemInfo = {}

		self.openUrl()
	
	def openUrl(self):
		self.parsedHTML = getHtml(self.url)

	def openGalleryUrl(self):
		self.parsedGallery = getHtml(self.galleryUrl)

	def isInItemInfo(self, key):
		return key in self.itemInfo

	def getId(self, key='id'):
		if not self.isInItemInfo(key):
			self.itemInfo[key] = re.findall('/([0-9]*?).html.*?', self.url)[0]

		return self.itemInfo[key]

	def getName(self, key='name'):
		if not self.isInItemInfo(key):
			self.itemInfo[key] = re.findall('<h1 class="product-name".*?\>(.*?)</h1>', self.parsedHTML)[0]

		return self.itemInfo[key]

	def getPrice(self, key='price'):
		if not self.isInItemInfo(key):
			priceBlock = re.findall('<div class="p-price-content.*?>(.*?)</div>', self.parsedHTML)[0]
			self.itemInfo[key] = ' - '.join(re.findall('[0-9\.]+', priceBlock))

		return self.itemInfo[key]

	def getRating(self, key='rating'):
		if not self.isInItemInfo(key):
			self.itemInfo[key] = re.findall('<span class="percent-num">(.*?)</span>', self.parsedHTML)[0]
		return self.itemInfo[key]

	def getOrders(self, key='orders'):
		if not self.isInItemInfo(key):
			self.itemInfo[key] = re.findall('<span class="order-num" id="j-order-num">([0-9]+)', self.parsedHTML)[0]
		return self.itemInfo[key]

	def getGalleryUrl(self):
		if not self.galleryUrl:
			self.galleryUrl = self.url.replace('/item/', '/item-img/')

		return self.galleryUrl

	def getGalleryImages(self, key='images-url'):
		if not self.parsedGallery:
			self.getGalleryUrl()
			self.openGalleryUrl()

		if not self.isInItemInfo(key):
			block = re.findall('<ul class="new-img-border">(.*?)</ul>', self.parsedGallery)[0]
			self.itemInfo[key] = re.findall('<img src="(.*?)".*?>', block)

		return self.itemInfo[key]

	def getImageUrl(self, key='image-url'):
		if not self.isInItemInfo(key):
			self.itemInfo[key] = re.findall('<div class="ui-image-viewer-thumb-wrap" data-role="thumbWrap">.*?<img.*?src="(.*?)".*?</a></div>', self.parsedHTML)[0]

		return self.itemInfo[key]

	def downloadImage(self, url='', filename='photo.jpg'):
		if not url: url = self.getImageUrl(self.url)
		urllib.request.urlretrieve(url, filename)
