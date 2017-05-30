import re, urllib.request

def getHtml(url):
	return urllib.request.urlopen(url).read().decode('utf-8').replace('\n', '')

class AliExpressItem(object):
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

	def cache(key):
		def decorator(func):
			def wrapper(self, *args, **kwargs):
				if not self.isInItemInfo(key):
					self.itemInfo[key] = func(self, *args, **kwargs)
				return self.itemInfo[key]
			return wrapper
		return decorator

	def openUrl(self):
		self.parsedHTML = getHtml(self.url)

	def openGalleryUrl(self):
		self.parsedGallery = getHtml(self.itemInfo['gallery-url'])

	def isInItemInfo(self, key):
		return key in self.itemInfo

	@cache(key='id')
	def getId(self):
		return re.findall('/([0-9]*?).html.*?', self.url)[0]

	@cache(key='name')
	def getName(self):
		return re.findall('<h1 class="product-name".*?\>(.*?)</h1>', self.parsedHTML)[0]

	@cache(key='price')
	def getPrice(self):
		priceBlock = re.findall('<div class="p-price-content.*?>(.*?)</div>', self.parsedHTML)[0]
		return ' - '.join(re.findall('[0-9\.]+', priceBlock))

	@cache(key='rating')
	def getRating(self):
		return re.findall('<span class="percent-num">(.*?)</span>', self.parsedHTML)[0]

	@cache(key='orders')
	def getOrders(self):
		return int(re.findall('<span class="order-num" id="j-order-num">([0-9]+)', self.parsedHTML)[0])

	@cache(key='gallery-url')
	def getGalleryUrl(self):
		return self.url.replace('/item/', '/item-img/')

	@cache(key='images-url')
	def getGalleryImages(self):
		self.getGalleryUrl()
		self.openGalleryUrl()

		block = re.findall('<ul class="new-img-border">(.*?)</ul>', self.parsedGallery)[0]
		return re.findall('<img src="(.*?)".*?>', block)

	@cache(key='image-url')
	def getImageUrl(self):
		return re.findall('<div class="ui-image-viewer-thumb-wrap" data-role="thumbWrap">.*?<img.*?src="(.*?)".*?</a></div>', self.parsedHTML)[0]

	def downloadImage(self, url='', filename='photo.jpg'):
		if not url:
			url = self.getImageUrl()

		urllib.request.urlretrieve(url, filename)
