<template>
	<main>
		<h1><router-link class="button is-large is-block is-primary" to="/learn/2/1">Student &ndash; Study</router-link></h1>
		<h1><router-link class="button is-large is-block is-primary" to="/teacher">Teacher &ndash; Analytics</router-link></h1>
		<h1><a target="_blank" class="button is-large is-block is-primary" href="https://hackathon.anandchowdhary.com/admin/">Teacher &ndash; CMS</a></h1>
		<h1><router-link class="button is-large is-block is-primary is-disabled" to="/">Management &ndash; Reports</router-link></h1>
		<h1><router-link class="button is-large is-block is-primary" to="/duo">DUO &ndash; Reports</router-link></h1>
	</main>
</template>

<style lang="scss">
main {
	padding: 1rem;
}
.button {
	margin-bottom: 1rem;
}
.is-disabled { 
	opacity: 0.5;
}
</style>
