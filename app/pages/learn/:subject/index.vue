<template>
	<div class="content" style="text-align: center">
		<img alt="Loading..." src="https://cdn-images-1.medium.com/max/1600/1*8NJgObmgEVhNWVt3poeTaA.gif">
	</div>
</template>

<script>
export default {
	data() {
		return {
			nav: []
		}
	},
	mounted() {
		this.$axios.get("https://hackathon.anandchowdhary.com/concepts")
			.then(data => {
				for (let i = 0; i < data.data.results.length; i++) {
					// console.log(data.data.results[i]);
					this.nav['c_' + data.data.results[i].category] = this.nav['c_' + data.data.results[i].category] || [];
					this.nav['c_' + data.data.results[i].category].push(data.data.results[i]);
				}
				try {
					this.$router.push(`/learn/${this.$route.params.subject}/${this.nav['c_' + this.$route.params.subject][0].id}`);
				} catch (e) {
					this.$router.push(`/learn/${this.$route.params.subject}/1`);
				}
			});
	}
}
</script>
