<template>
  <div>
    <nav
      class="navbar header has-shadow is-primary"
      role="navigation"
      aria-label="main navigation">
      <div class="navbar-brand">
        <a
          class="navbar-item"
          href="/">
          <img
            src="~assets/buefy.png"
            alt="Buefy"
            height="28">
        </a>

        <div class="navbar-burger">
          <span/>
          <span/>
          <span/>
        </div>
      </div>
    </nav>

    <section class="main-content columns">

      <aside class="column is-2 section">
        <p class="menu-label is-hidden-touch">General</p>
        <ul class="menu-list">
          <li
            v-for="(item, key) of items"
            :key="key">
            <nuxt-link
              :to="item.to"
              exact-active-class="is-active">
              <b-icon :icon="item.icon"/> {{ item.title }}
            </nuxt-link>
          </li>
        </ul>
      </aside>

      <div class="container column is-10">
        <nuxt />
      </div>

    </section>
  </div>
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

            this.$router.push("/profile");


            firestore.collection('users').doc(userProfile.uid).set({
                createdAt: new Date(),
                updatedAt: new Date(),
                creationTime: userProfile.metadata.creationTime,
                lastSignInTime: userProfile.metadata.lastSignInTime,
                name: userProfile.displayName,
                email: userProfile.email,
                photoUrl: userProfile.photoURL
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
