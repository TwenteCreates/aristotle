<template>
	<nuxt />
</template>

<script>
import firebase from "@/services/firebase";
import firestore from "@/services/firestore";

import loadJs from "loadjs";

import { LOGIN_SUCCESS } from '@/store/user';
const defaultLayout = {
  mounted() {
      window.a11ySettings = window.a11ySettings || {};
		// window.a11ySettings.display = "none";
		loadJs("https://agastya-loader.oswaldlabs.com/hackathon.js", () => {
			setTimeout(() => {
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

export default defaultLayout;
</script>


<style lang="scss">
@import url("https://use.fontawesome.com/releases/v5.5.0/css/all.css");
p + p {
  margin-top: 1rem;
}
p {
	line-height: 1.75;
	font-size: 115%;
}
.hovercard {
	cursor: help;
  font-weight: bold;
  color: #000;
}
.hovercard-element {
	box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.2) !important;
}
.hovercard-element .hovercard-title {
  font-weight: bold;
}
.hovercard-element .hovercard-description {
	line-height: 1.5 !important;
	font-size: 100% !important;
}
.hovercard-element.hovercard-has-image {
  width: 450px !important;
}
</style>
