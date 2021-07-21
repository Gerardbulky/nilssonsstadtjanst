$(document).ready(function initMap() {
      // Map Options
      var options = {
        zoom: 7,
        center: { lat: 59.7294, lng: 13.2354 },
      };
      // initialising the map
      var map = new google.maps.Map(document.getElementById("map"), options);


      // Calling Add Markers
      addmarker({
        coords: { lat: 59.1327, lng: 12.9301 },
        content:
          '<div><h6><bold>säffle</bold></h6><a href="tel:0720107276">0720107276</a><br><a target="_blank" href="#">gerardbulky@gmail.com</a></div>',
        infoPopup: "<h6><bold>säffle</bold></h6><p>👍 click the icon </p>",
      });
      addmarker({
        coords: { lat: 59.4022, lng: 13.5115 },
        content:
          '<div><h6><bold>karlstad</bold></h6><a href="tel:0724427070">0724427070</a><br><a target="_blank" href="#">gerardbulky@gmail.com</a></div>',
        infoPopup: "<h6><bold>karlstad</bold></h6><p>👍 click the icon </p>",
      });

      // Adding MAP Markers Function
      function addmarker(props) {
        var marker = new google.maps.Marker({
          position: props.coords,
          map: map,
        });

        // Adding InfoWindow upon clicking
        if (props.content) {
          var infoWindow = new google.maps.InfoWindow({
            content: props.content,
          });
          marker.addListener("click", function () {
            infoWindow.open(map, marker);
          });
        }
        // Adding Info PopUp upon hovering
        if (props.infoPopup) {
          var infoPopup = new google.maps.InfoWindow({
            content: props.infoPopup,
          });
          marker.addListener("mouseover", function () {
            infoPopup.open(map, marker);
          });
          marker.addListener("mouseout", function () {
            infoPopup.close(map, marker);
          });
        }
      }

    })