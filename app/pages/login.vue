<template>
    <main>
        <div class="hero-body">
            <div class="container has-text-centered">
                <div class="column is-4 is-offset-4">
                    <p class="subtitle has-text-grey">Please login to proceed.</p>
                    <div class="box">
                        <figure class="avatar">
                        </figure>
                        <form>
                            <b-field label="Email">
                                <b-input v-model="email"></b-input>
                            </b-field>

                            <b-field label="Password">
                                <b-input type="password" password-reveal v-model="password"></b-input>
                            </b-field>

                            <button class="button" @click.prevent="loginWithCredentials">
                                <b-icon icon="key"></b-icon>
                                <span>Login with credentials</span>
                            </button>

                            <br />
                            <br />

                            <button class="button login-button" style="background-color:#176bef" @click.prevent="loginWithGoogle">
                                <b-icon icon="google"></b-icon>
                                <span>Login with Google</span>
                            </button>

                            <button class="button login-button" style="background-color:#f65314" @click.prevent="loginWithMicrosoft">
                                <b-icon icon="windows"></b-icon>
                                <span>Login with Office365</span>
                            </button>

                            <button class="button login-button" style="background-color:#0077b5" @click.prevent="loginWithLinkedin">
                                <b-icon icon="linkedin"></b-icon>
                                <span>Login with LinkedIn</span>
                            </button>
                        </form>
                    </div>
                    <p class="has-text-grey">
                        <a href="#">Sign Up</a> &nbsp;·&nbsp;
                        <a href="#">Forgot Password</a> &nbsp;·&nbsp;
                        <a href="#">Need Help?</a>
                    </p>
                </div>
            </div>
        </div>
    </main>
</template>

<style scoped>
.login-button {
    margin-top: 13px;
    min-width: 200px;
    color: white;
}
</style>


<script>
import { LOGIN } from '@/store/user';
import { CREDENTIALS_LOGIN_PROVIDER, GOOGLE_LOGIN_PROVIDER, LINKEDIN_LOGIN_PROVIDER, FACEBOOK_LOGIN_PROVIDER } from '@/store/user/loginProviders';

export default {
  data () {
    return {
      email: '',
      password: '',
    };
  },
  methods: {
    loginWithCredentials(email, password) {
        if (this.$store.state.user.loggedIn) this.$router.push("/");
        this.$store.dispatch(LOGIN, { provider: CREDENTIALS_LOGIN_PROVIDER, credentials: { email, password }});
    },
    loginWithGoogle() {
        if (this.$store.state.user.loggedIn) this.$router.push("/");
        this.$store.dispatch(LOGIN, { provider: GOOGLE_LOGIN_PROVIDER });
    },
    loginWithMicrosoft() {
        this.loginWithGoogle();
    },
    loginWithLinkedin() {
        this.loginWithGoogle();
    }
  }
};
</script>
