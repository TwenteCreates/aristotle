<template>
	<main>
		<figure class="image is-128x128">
			<img class="is-rounded" :src="`https://platform.oswaldlabs.com/v1/profile-picture/${user.email}`"/>
		</figure>
		<h2>{{user.displayName}}</h2>
		<button class="button is-primary" @click="logout">Log out</button>
	</main>
</template>

<style></style>

<script>
import { LOGOUT } from '@/store/user';

export default {
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
