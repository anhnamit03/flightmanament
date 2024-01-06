importScripts('https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js');
importScripts('https://www.gstatic.com/firebasejs/10.7.1/firebase-messaging-compat.js');

const firebaseConfig = {
    apiKey: "AIzaSyB-81olDWdH2wCEla_KTHIbWlxYdBcqK6w",
    authDomain: "flightmanagement-d989d.firebaseapp.com",
    projectId: "flightmanagement-d989d",
    storageBucket: "flightmanagement-d989d.appspot.com",
    messagingSenderId: "766444659533",
    appId: "1:766444659533:web:08aa23d67fe25bea740d04",
    measurementId: "G-0YCW8XPV91"
};

firebase.initializeApp(firebaseConfig);
const messaging = firebase.messaging();

if ('serviceWorker' in navigator) {
    navigator.serviceWorker.ready.then((registration) => {
        messaging.useServiceWorker(registration);
        console.log('Firebase Messaging Service Worker is ready.');
    }).catch((error) => {
        console.error('Error initializing Firebase Messaging Service Worker:', error);
    });
}



messaging.onBackgroundMessage((payload) => {
  try {
    console.log('[fire_ws.js] Received background message:', payload);

    // Extract notification data from the payload
    const notificationTitle = payload.data.title || 'Default Title';


    const notificationOptions = {
      body: payload.data.body || 'Default Body',
      icon: payload.data.icon || 'https://www.honda.com.vn/o-to/san-pham/honda-city/assets/imgs/message/bg_popup.jpg'
    };

    // Show the notification
    self.registration.showNotification(notificationTitle, notificationOptions);


  } catch (error) {
    console.error('Error handling background message:', error);
  }
});



self.addEventListener('push', function (event) {
  try {
      const pushData = event.data.json();

      // Access data from the 'data' field
      const notificationData = pushData.data || {};

      const options = {
          body: notificationData.body || 'Default Body',
          icon: notificationData.icon || 'https://www.honda.com.vn/o-to/san-pham/honda-city/assets/imgs/message/bg_popup.jpg',
      };

      // Log or use the additional data
      console.log('Additional Data:', notificationData);

      // Display the notification
      self.registration.showNotification(notificationData.title || 'Default Title', options);
  } catch (error) {
      console.error('Error handling push event:', error);
  }
});

