import firebase from './firebase';

const firestore = firebase.firestore();

const settings = { timestampsInSnapshots: true };

firestore.settings(settings);

export default firestore;
