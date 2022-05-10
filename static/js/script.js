'use strict';

let target = document.getElementById('target');
let map;
const marker = [];
const infoWindow = [];
let homePosition = { lat: 35.06097411828546, lng: 137.11560426263384 };
let tapped_marker = 0
let superTarget = document.querySelectorAll(`[id^='superID']`);
const superIDList = [];

for (const i of superTarget) {
    const superIDID = i.id;
    superIDList.push(superIDID);
    console.log(superIDID);
}

for (const ID of superIDList) {
    document.getElementById(ID).style.display = 'none';
}


function initMap() {

    map = new google.maps.Map(target, {
        center: homePosition,
        zoom: 15,
        disableDefaultUI: true,
        zoomControl: true,
        clickableIcons: false,
        styles: [
            {
                'featureType': 'administrative.land_parcel',
                'elementType': 'labels',
                'stylers': [
                    {
                        'visibility': 'off'
                    }
                ]
            },
            {
                'featureType': 'poi',
                'elementType': 'labels.text',
                'stylers': [
                    {
                        'visibility': 'off'
                    }
                ]
            },
            {
                'featureType': 'poi.business',
                'stylers': [
                    {
                        'visibility': 'off'
                    }
                ]
            },
            {
                'featureType': 'poi.park',
                'elementType': 'labels.text',
                'stylers': [
                    {
                        'visibility': 'off'
                    }
                ]
            },
            {
                'featureType': 'road.local',
                'elementType': 'labels',
                'stylers': [
                    {
                        'visibility': 'off'
                    }
                ]
            }
        ]
    });

    for (let i = 0; i < marker_data.length; i++) {
        marker[i] = new google.maps.Marker({ // マーカーの追加
            position: { lat: marker_data[i]['lat'], lng: marker_data[i]['lng'] }, // マーカーを立てる位置を指定
            map: map, // マーカーを立てる地図を指定
            icon: { url: `${DJANGO_STATIC_URL}img/comment.svg`, scaledSize: new google.maps.Size(48, 24) },
            label: {
                text: marker_data[i]['price'],
                color: 'white',
                fontSize: '15px',
                fontWeight: 'bold',
            }
        });
        markerEvent(i);
    }
}


function markerEvent(i) {
    map.addListener('click', function () {
        for (const ID of superIDList) {
            document.getElementById(ID).style.display = 'none';
        }
    });

    marker[i].addListener('mouseover', function () {
        marker[i].setIcon({ url: `${DJANGO_STATIC_URL}img/comment.svg`, scaledSize: new google.maps.Size(64, 32) });
    });

    marker[i].addListener('mouseout', function () {
        marker[i].setIcon({ url: `${DJANGO_STATIC_URL}img/comment.svg`, scaledSize: new google.maps.Size(48, 24) });
    });

    marker[i].addListener('click', function () { // マーカーをクリックしたとき
        marker[i].setIcon({ url: `${DJANGO_STATIC_URL}img/comment_02.svg`, scaledSize: new google.maps.Size(64, 32) });
        tapped_marker = marker_data[i]['superID'];
        document.getElementById('number1').value = tapped_marker;
        document.getElementById("btn1").click();
    });
}