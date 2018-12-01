<template>
	<nuxt />
</template>

<script>
import firebase from "@/services/firebase";
import firestore from "@/services/firestore";

import loadJs from "loadjs";

import { LOGIN_SUCCESS } from '@/store/user';
export default {
  mounted() {
      window.a11ySettings = window.a11ySettings || {};
		// window.a11ySettings.display = "none";
		loadJs("https://agastya-loader.oswaldlabs.com/hackathon.js", () => {
			setTimeout(() => {
				window.agastya.api();
			}, 1000);
        });

      firebase.auth().onAuthStateChanged(userProfile => {
        if (userProfile) {
            this.$store.commit(LOGIN_SUCCESS, userProfile);


            if (this.$route.path === "/login") {
                this.$router.push("/");
            }

            firestore.collection('users').doc(userProfile.uid).set({
                createdAt: new Date(),
                updatedAt: new Date(),
                creationTime: userProfile.metadata.creationTime,
                lastSignInTime: userProfile.metadata.lastSignInTime,
                name: userProfile.displayName,
                email: userProfile.email,
                photoUrl: userProfile.photoURL,
                role: 'student',
                points: 0
            }, { merge: true });
        } else {
            this.$router.push("/login");
        }
      });
  },
  methods: {
        a11y() {
			window.agastya.frame.open();
        }
  },
  data() {
    return {
      items: [
        { title: 'Home', icon: 'home', to: { name: 'index' } },
        { title: 'Inspire', icon: 'lightbulb', to: { name: 'inspire' } }
      ]
    }
  }
}
</script>
