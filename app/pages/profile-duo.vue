
<template>
    <main>
        <section class="hero is-info is-bold">
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
            <div class="field">
                <label class="label">Display name</label>
                <div class="control has-icons-left">
                    <input class="input" type="text" placeholder="Text input" :value="user.displayName">
                    <span class="icon is-small is-left">
                        <i class="fas fa-user"></i>
                    </span>
                </div>
            </div>

            <div class="field">
                <label class="label">Email</label>
                <div class="control has-icons-left">
                    <input class="input" type="email" placeholder="Email input" :value="user.email">
                    <span class="icon is-small is-left">
                        <i class="fas fa-envelope"></i>
                    </span>
                </div>
            </div>


            <div class="field">
                <label class="label">About</label>
                <div class="control">
                    <textarea class="textarea" placeholder="Textarea"></textarea>
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <label class="checkbox">
                    <input type="checkbox">
                    I agree to the <a href="#">terms and conditions</a>
                    </label>
                </div>
            </div>

            <div class="field is-grouped">
                <div class="control">
                    <button class="button is-link is-info">Submit</button>
                </div>
            </div>
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
  layout: 'duo',
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
