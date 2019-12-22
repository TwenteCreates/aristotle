![Aristotle](/aristotle-logo.png)

Aristotle is an accessible e-learning platform for Provincie Limburg, built at Brighthack 2018 in Heerlen.

**🥇 Award**: Winner of the "Education" category with a €12,500 award

[**Read case study →**](https://anandchowdhary.com/projects/aristotle)

## 💻 Demo

The demo was last updated in November 2018, so some APIs might not be online anymore.

[View live demo](https://aristotle-beta.web.app) or [**watch pitch video**](https://www.youtube.com/watch?v=223RTMXXtxc)

![Aristotle screenshot](/aristotle-screenshot.png)

## 🛠️ Development

The [`app`](/app) directory contains a Vue.js webapp built using Nuxt.js and the [`api`](/api) directory contains the Dockerized backend with RESTful APIs written in Python using Django, deployed to Firebase and an EC2 running Caprover respectively.

### Frontend

To build the frontend, head to the directory using `cd app` and install dependencies:

```
npm install
```

Run the frontend on http://localhost:3000:

```
npm run dev
```

Firebase is used to deploy the frontend to https://aristotle-beta.web.app, built using:

```
npm run generate
```

### Backend

The [Dockerfile](/api/Dockerfile) is used by Caprover to build and deploy the app.

## 👥 Contributors

[![Profile pictures of contributors on GitHub](https://services.anandchowdhary.now.sh/api/github-contributors?repo=c-r-e-a-t-e/aristotle)](https://github.com/c-r-e-a-t-e/aristotle/graphs/contributors)

## 📄 License

- Code: [MIT](/LICENSE)
- Logo and assets: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

