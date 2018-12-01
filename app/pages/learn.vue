<template>
	<main>
		<aside>
			<div class="vertical-nav">
				<a href="#">1</a>
				<a href="#" class="active">2</a>
				<a href="#">3</a>
				<a href="#">4</a>
			</div>
		</aside>
		<nav :class="`${increasing ? 'is-increasing' : ''}`">
			🏆
			<strong>{{points}}</strong>
		</nav>
		<div class="content">
			<h1>Netwon&rsquo;s First Law</h1>
			<p>Newton's First Law states that an object will remain at rest or in uniform motion in a straight line unless acted upon by an external force. It may be seen as a statement about inertia, that objects will remain in their state of motion unless a force acts to change the motion.</p>
			<iframe src="https://www.youtube.com/embed/E6_6z1ZJ_0s" />
			<p>The First Law could be viewed as just a special case of the Second Law for which the net external force is zero, but that carries some presumptions about the frame of reference in which the motion is being viewed. The statements of both the Second Law and the First Law here are presuming that the measurements are being made in a reference frame which is not itself accelerating. Such a frame is often referred to as an "inertial frame". The statement of these laws must be generalized if you are dealing with a rotating reference frame or any frame which is accelerating.</p>
			<p>Newton's First Law contains implications about the fundamental symmetry of the universe in that a state of motion in a straight line must be just as "natural" as being at rest. If an object is at rest in one frame of reference, it will appear to be moving in a straight line to an observer in a reference frame which is moving by the object. There is no way to say which reference frame is "special", so all constant velocity reference frames must be equivalent.</p>
			<div v-if="!isHidden" :class="`card is-answer card-content has-background-white-bis ${isCorrect ? 'is-correct' : ''} ${isHidden ? 'is-invisible' : ''}`">
				<span class="tag is-danger">Quick question</span>
				<p style="margin-top: 0.5rem; margin-bottom: 0.5rem">What's the answer to this question which will give you points?</p>
				<b-radio native-value="Flint">First Law</b-radio>
				<b-radio native-value="Flint">Second Law</b-radio>
				<b-radio native-value="Flint">Third Law</b-radio>
				<div style="margin-top: 1rem">
					<button class="button is-link" @click.prevent="checkAnswer">Get your points!</button>
				</div>
			</div>
			<div v-if="isHidden && isCorrect" style="margin-top: 3rem">
				<nuxt-link to="/" class="button is-link is-large is-block">Next topic for 🏆 35 &rarr;</nuxt-link>
			</div>
		</div>
		<div class="progress">
			<div class="progress-value" :style="`width: ${progressPercent}%`"></div>
		</div>
	</main>
</template>

<script>
export default {
	data() {
		return {
			points: 42,
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
		window.onscroll = val => {
			let h = document.documentElement, 
			b = document.body,
			st = "scrollTop",
			sh = "scrollHeight";
			this.progressPercent = (h[st]||b[st]) / ((h[sh]||b[sh]) - h.clientHeight) * 100;
		}
	},
	methods: {
		checkAnswer() {
			this.isCorrect = !this.isCorrect;
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
p {
	line-height: 1.75;
	font-size: 115%;
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
		z-index: 1;
	}
	&.is-invisible {
		opacity: 0;
		max-height: 1px;
	}
}
.is-correct {
	overflow: hidden;
	.button {
		background-color: #2ecc71;
		transform: scale(20) translateY(10px);
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
		font-size: 32px;
		text-align: center;
		&.active {
			background-color: whitesmoke;
		}
	}
}
</style>
