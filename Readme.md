A running demo can be found on http://34.243.90.71

Written with:
	Django Framework
	JS (minor)
	CSS
	Bootstrap

Content Administration performed through admin page

App Breakdown
	home: Slideshow(requires promo), 
		Latest Articles Area(requires blog), 
		Office Information with Geolocation 
		(js script is not working requires gmaps api key and testing/fix)
		Simple contact form(requires contact)
		base template with header(home,info,articles,services),footer(required by all views)
		basic info page (wip)

	blog: Add articles to be displayed in views
		Generic articles view features filter based			year, month, tag (need to make this work for multiple tags and text query matching either title or body of the articles)
		Uses easy-thumbnails,ck-editor (word editor for the body of the articles), taggit (adds tag fields to objects and used for searching through tags)

	promo: Add information about services provided and display in views.
		Each object has its own view accessible through nav bar (dropdown).The view requires the use of an appointment form included in contact application
		The django context processor has by default all objects to be able to create the header dropdown dynamcally

	contact: Models for contact and appointment form along with the necessary templates
