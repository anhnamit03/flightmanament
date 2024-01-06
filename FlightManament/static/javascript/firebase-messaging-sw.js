importScripts('https://cdnjs.cloudflare.com/ajax/libs/firebase/10.0.0/firebase-app-compat.min.js');
importScripts('https://cdnjs.cloudflare.com/ajax/libs/firebase/10.0.0/firebase-messaging-compat.min.js');

firebase.initializeApp({
  apiKey: "AIzaSyB-81olDWdH2wCEla_KTHIbWlxYdBcqK6w",
  authDomain: "flightmanagement-d989d.firebaseapp.com",
  projectId: "flightmanagement-d989d",
  storageBucket: "flightmanagement-d989d.appspot.com",
  messagingSenderId: "766444659533",
  appId: "1:766444659533:web:08aa23d67fe25bea740d04",
  measurementId: "G-0YCW8XPV91"
});

const messaging2 = firebase.messaging();

// Customize this section based on your needs
messaging2.setBackgroundMessageHandler(payload => {
  const notificationTitle = 'Background Message Title';
  const notificationOptions = {
    body: 'Background Message body.',
    icon: 'your-icon-url'
  };

  return self.registration.showNotification(notificationTitle, notificationOptions);
});
