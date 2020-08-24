// Initialize and add the map
function initMap() {
	var locations = {{ offices }}
	var i;
	for (i = 0; i <= locations.length; i++) {
		var loc = {lat: locations[i]["latitude"], lng: locations[i]["longitute"]}
		var map = new google.maps.Map(
			document.getElementById('map'+i), {zoom:4, center: loc});
                var marker = new google.maps.Marker({position: loc, map: map});
	}
}
