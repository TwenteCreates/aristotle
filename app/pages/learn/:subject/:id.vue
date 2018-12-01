<template>
	<main>
		<aside>
			<div class="vertical-nav">
				<nuxt-link to="/"><i class="fas fa-chart-line"></i></nuxt-link>
				<nuxt-link to="/" class="active"><i class="fas fa-book-reader"></i></nuxt-link>
				<nuxt-link to="/"><i class="fas fa-comments"></i></nuxt-link>
				<nuxt-link to="/"><i class="fas fa-cogs"></i></nuxt-link>
			</div>
			<ul>
				<li>
					<nuxt-link to="/learn/nederlands">
						<i class="fas fa-fw fa-font"></i>
						Nederlands
					</nuxt-link>
					<ul>
						<li><nuxt-link to="/learn/nederlands/1">Lesson 1</nuxt-link></li>
						<li><nuxt-link to="/learn/nederlands/2">Lesson 2</nuxt-link></li>
						<li><nuxt-link to="/learn/nederlands/3">Lesson 3</nuxt-link></li>
					</ul>
				</li>
				<li>
					<nuxt-link to="/learn/engels">
						<i class="fas fa-fw fa-font"></i>
						Engels
					</nuxt-link>
					<ul>
						<li><nuxt-link to="/learn/engels/1">Lesson 1</nuxt-link></li>
						<li><nuxt-link to="/learn/engels/2">Lesson 2</nuxt-link></li>
						<li><nuxt-link to="/learn/engels/3">Lesson 3</nuxt-link></li>
					</ul>
				</li>
				<li>
					<nuxt-link to="/learn/wiskunde">
						<i class="fas fa-fw fa-calculator"></i>
						Wiskunde
					</nuxt-link>
					<ul>
						<li><nuxt-link to="/learn/wiskunde/1">Multiplication</nuxt-link></li>
						<li><nuxt-link to="/learn/wiskunde/2">Multiplication tables</nuxt-link></li>
					</ul>
				</li>
				<li>
					<nuxt-link to="/learn/aardrijkskunde">
						<i class="fas fa-fw fa-globe-africa"></i>
						Aardrijkskunde
					</nuxt-link>
					<ul>
						<li><nuxt-link to="/learn/aardrijkskunde/1">Lesson 1</nuxt-link></li>
						<li><nuxt-link to="/learn/aardrijkskunde/2">Lesson 2</nuxt-link></li>
						<li><nuxt-link to="/learn/aardrijkskunde/3">Lesson 3</nuxt-link></li>
					</ul>
				</li>
				<li>
					<nuxt-link to="/learn/geschiedenis">
						<i class="fas fa-fw fa-landmark"></i>
						Geschiedenis
					</nuxt-link>
					<ul>
						<li><nuxt-link to="/learn/geschiedenis/1">Lesson 1</nuxt-link></li>
						<li><nuxt-link to="/learn/geschiedenis/2">Lesson 2</nuxt-link></li>
						<li><nuxt-link to="/learn/geschiedenis/3">Lesson 3</nuxt-link></li>
					</ul>
				</li>
			</ul>
		</aside>
		<nav :class="`${increasing ? 'is-increasing' : ''}`">
			🏆
			<strong>{{points}}</strong>
		</nav>
		<div class="content" style="text-align: center" v-if="loading">
			<img alt="Loading..." src="https://cdn-images-1.medium.com/max/1600/1*8NJgObmgEVhNWVt3poeTaA.gif">
		</div>
		<div class="content" v-else>
			<h1>{{details.name}}</h1>
			<div class="summary-text" v-html="marked(details.summary)" />
			<iframe :src="`https://www.youtube.com/embed/${details.video}`" />
			<div v-if="!isHidden" :class="`card is-answer card-content has-background-white-bis ${isCorrect ? 'is-correct' : ''} ${isHidden ? 'is-invisible' : ''}`">
				<span class="tag is-danger">Quick question</span>
				<p style="margin-top: 0.5rem; margin-bottom: 0.5rem">{{details.question}}</p>
				<div style="margin-top: 1rem">
					<button :class="`button is-link${details.correct_answer === 0 ? ' correct' : ''}`" @click.prevent="details.correct_answer === 0 ? checkAnswer() : wrongAnswer()">{{details.answer0}}</button>
					<button :class="`button is-link${details.correct_answer === 1 ? ' correct' : ''}`" @click.prevent="details.correct_answer === 1 ? checkAnswer() : wrongAnswer()">{{details.answer1}}</button>
					<button :class="`button is-link${details.correct_answer === 2 ? ' correct' : ''}`" @click.prevent="details.correct_answer === 2 ? checkAnswer() : wrongAnswer()">{{details.answer2}}</button>
					<button :class="`button is-link${details.correct_answer === 3 ? ' correct' : ''}`" @click.prevent="details.correct_answer === 3 ? checkAnswer() : wrongAnswer()">{{details.answer3}}</button>
				</div>
			</div>
			<div v-if="isHidden && isCorrect" style="margin-top: 3rem">
				<button class="button is-link is-large is-block" @click.prevent="nextTopic">Next topic for 🏆 35 &rarr;</button>
			</div>
		</div>
		<div class="progress">
			<div class="progress-value" :style="`width: ${progressPercent}%`"></div>
		</div>
	</main>
</template>

<script>
import hovercard from "hovercard";
import marked from "marked";
import "@/node_modules/hovercard/build/index.css";
export default {
	data() {
		return {
			loading: true,
			points: 42,
			details: {},
			progressPercent: 0,
			isCorrect: false,
			increasing: false,
			isHidden: false
		}
	},
	computed: {
		user() {
			return this.$store.state.user.profile;
		}
	},
	mounted() {
		this.setup();
	},
	methods: {
		setup() {
			this.loading = true;
			this.$axios.get("https://hackathon.anandchowdhary.com/concepts/?id=" + this.$route.params.id)
				.then(data => {
					this.details = data.data.results[0];
					this.loading = false;
					setTimeout(() => {
						["natural numbers", "real numbers", "Mathematicians", "commutative", "Rational numbers", "Complex numbers", "quaternions", "Babylonians"].forEach(importantTerms => {
							document.querySelector(".summary-text").innerHTML = document.querySelector(".summary-text").innerHTML.replace(importantTerms, `<span class="hovercard">${importantTerms}</span>`);
						});
						setTimeout(() => {
							const card = new hovercard();
							card.setup();
						}, 1);
					}, 1);
				});
			window.onscroll = val => {
				let h = document.documentElement, 
				b = document.body,
				st = "scrollTop",
				sh = "scrollHeight";
				this.progressPercent = (h[st]||b[st]) / ((h[sh]||b[sh]) - h.clientHeight) * 100;
			}
		},
		nextTopic() {
			const path = this.$route.path;
			this.$router.push("/learn/" + this.$route.params.subject + "/" + (parseInt(this.$route.params.id) + 1));
		},
		marked(md) {
			if (!md) return;
			return marked(md);
		},
		wrongAnswer() {
			alert("Try again!");
		},
		checkAnswer() {
			console.log("ABC");
			this.isCorrect = true;
			const newPoints = this.points + 30;
			setTimeout(() => {
				const interval = setInterval(() => {
					if (newPoints === this.points) {
						this.increasing = false;
						clearInterval(interval);
					} else {
						this.points++;
						this.increasing = true;
					}
				}, 50);
				setTimeout(() => {
					this.isHidden = true;
				}, 1000);
			}, 1000);
		}
	}
}
</script>


<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css?family=Lora");
.progress {
	position: fixed;
	left: 300px; right: 0;
	top: 0;
	height: 0.25rem;
	background-color: whitesmoke;
	border-radius: 0;
	.progress-value {
		position: absolute;
		left: 0;
		background-color: rgb(27, 98, 212);
		top: 0; bottom: 0;
	}
}
aside {
	position: fixed;
	background-color: whitesmoke;
	width: 300px;
	top: 0; bottom: 0;
	left: 0;
}
nav {
	background-color: whitesmoke;
	position: fixed;
	right: 1rem;
	top: 1.25rem;
	padding: 0.5rem 1rem;
	transition: 1s;
	border-radius: 0.25rem;
	&.is-increasing {
		right: 5em;
		top: 5em;
		background-color: yellow;
		transform: scale(2);
	}
}
.content {
	width: 700px;
	position: absolute;
	left: 50%;
	padding: 5rem 0;
	margin-left: -235px;
}
h1 {
	font-family: "Lora";
	font-weight: normal;
	font-size: 300%;
}
iframe {
	width: 100%;
	border: 0;
	margin: 2rem 0;
	height: 390px;
}
p + .card {
	margin-top: 3rem;
}
.button {
	transition: 1s;
}
.is-answer {
	overflow: hidden;
	position: relative;
	transition: 1s;
	max-height: 500px;
	&::before {
		content: "Correct!";
		position: absolute;
		color: #fff;
		left: 50%; top: 50%;
		transition: 1s;
		opacity: 0;
		transform: translate(-50%, -70%);
		font-size: 150%;
		z-index: 3;
	}
	&.is-invisible {
		opacity: 0;
		max-height: 1px;
	}
}
.is-correct {
	overflow: hidden;
	.button.correct {
		z-index: 2;
		background-color: #2ecc71;
		transform: scale(30) translateY(10px);
	}
	&::before {
		opacity: 1;
	}
}
.vertical-nav {
	background-color: rgba(0, 0, 0, 0.1);
	position: absolute;
	left: 0; top: 0;
	bottom: 0;
	a {
		display: block;
		width: 70px;
		height: 70px;
		line-height: 70px;
		color: rgba(0, 0, 0, 0.5);
		font-size: 24px;
		text-align: center;
		&.active {
			background-color: whitesmoke;
		}
	}
}
aside ul {
	li {
		margin-left: 70px;
		a {
			display: block;
			color: inherit;
			padding: 1rem;
			text-decoration: none;
			&.nuxt-link-active,
			&.nuxt-link-active + ul,
			&.nuxt-link-active + ul a {
				background-color: #fff;
			}
			&.nuxt-link-active + ul {
				display: block;
				padding-bottom: 1rem;
				li a {
					padding: 0 1rem;
					&.nuxt-link-exact-active {
						font-weight: bold;
					}
				}
			}
		}
		ul {
			display: none;
			li {
				margin-left: 0;
			}
		}
		i {
			margin-right: 0.25rem;
		}
	}
}
</style>
