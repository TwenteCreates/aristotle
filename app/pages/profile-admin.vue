<template>
    <main>
        <section class="hero is-primary is-bold">
            <div class="hero-body">
                <div class="container">
                    <div class="columns">
                        <div class="column is-2">
                            <figure class="image is-128x128">
                                <img class="is-rounded" :src="user.photoURL"/>
                            </figure>
                        </div>
                        <div class="column">
                            <h1 class="title">
                                {{user.displayName}}
                            </h1>
                            <h2 class="subtitle">
                                {{user.email}}
                            </h2>
                            <a class="button is-primary is-inverted is-outlined" @click="logout">
                                <span class="icon is-small">
                                    <i class="fas fa-sign-out-alt"></i>
                                </span>
                                <span>Log out</span>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="container profile-container">
        </section>
    </main>
</template>

<style lang="scss" scss>
.profile-container {
    padding-top: 1rem;
}
</style>

<script>
import { LOGOUT } from '@/store/user';

export default {
  layout: 'admin',
  computed: {
	  user () {
		  return this.$store.state.user.profile;
	  }
  },
  methods: {
	  logout () {
		  this.$store.dispatch(LOGOUT);
	  }
  }
};
</script>
