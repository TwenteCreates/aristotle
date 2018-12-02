const pkg = require('./package')

module.exports = {
  mode: 'spa',

  /*
  ** Headers of the page
  */
  head: {
    title: 'Artistotle',
    htmlAttrs: {lang: 'nl'},
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  /*
  ** Customize the progress-bar color
  */
  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
  ],

  /*
  ** Plugins to load before mounting the App
  */
  plugins: [],

  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://github.com/nuxt-community/axios-module#usage
    '@nuxtjs/axios',
    // Doc: https://buefy.github.io/#/documentation
    'nuxt-buefy',
    // Doc: https://pwa.nuxtjs.org,
    '@nuxtjs/pwa',
  ],
  /*
  ** Axios module configuration
  */
  axios: {
    // See https://github.com/nuxt-community/axios-module#options
  },

  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {

    }
  },
    env: {
        firebaseConfig: {
            apiKey: "AIzaSyBl76MZk1_KBU0oFrR57vRLdMnCYRZKaHk",
            authDomain: "aristotle-beta.firebaseapp.com",
            databaseURL: "https://aristotle-beta.firebaseio.com",
            projectId: "aristotle-beta",
            storageBucket: "",
            messagingSenderId: "759606146433"
        },
    },
    manifest: {
        name: 'Aristotle - Your personal tutor',
        short_name: 'Aristotle',
        background_color: "#fff",
        lang: 'nl'
    }
}
