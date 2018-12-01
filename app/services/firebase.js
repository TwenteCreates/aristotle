import firebase from '@firebase/app';
import '@firebase/firestore';
import '@firebase/auth';

var config = process.env.firebaseConfig;

firebase.initializeApp(config);

export default firebase;
