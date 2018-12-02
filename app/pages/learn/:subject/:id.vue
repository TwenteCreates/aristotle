<template>
	<main>
		<aside>
			<div class="vertical-nav">
				<button :class="`${activeNav === 'graphs' ? 'active' : ''}`" @click="activeNav = 'graphs'">
					<i class="fas fa-chart-line"></i>
				</button>
				<button :class="`${activeNav === 'nav' ? 'active' : ''}`" @click="activeNav = 'nav'">
					<i class="fas fa-book-reader"></i>
				</button>
				<button :class="`${activeNav === 'chat' ? 'active' : ''}`" @click="activeNav = 'chat'">
					<i class="fas fa-comments"></i>
				</button>
				<button :class="`${activeNav === 'profile' ? 'active' : ''}`" @click="activeNav = 'profile'">
					<i class="fas fa-user"></i>
				</button>
				<button :class="`${activeNav === 'settings' ? 'active' : ''}`" @click="activeNav = 'settings'">
					<i class="fas fa-cogs"></i>
				</button>
			</div>
			<div name="fade">
				<div key="settings" class="insides" v-if="activeNav === 'settings'">
					<button class="button is-secondary is-fullwidth is-large" @click="eDo(`window.agastya.api('cssClass', 'dyslexia')`)">
						Dyslexia mode
					</button>
					<button class="button is-secondary is-fullwidth is-large" @click="eDo(`window.agastya.api('cssClass', 'blueFilter')`)">
						Blue light filter
					</button>
					<button class="button is-secondary is-fullwidth is-large" @click="eDo(`window.agastya.api('cssClass', 'night')`)">
						Night mode
					</button>
					<button class="button is-secondary is-fullwidth is-large" @click="eDo(`window.agastya.api('cssClass', 'desaturate')`)">
						Desaturate
					</button>
				</div>
				<div key="profile" style="text-align: center" class="insides" v-if="activeNav === 'profile'">
					<img style="width: 30%; margin: 1rem 0; border-radius: 100%" :src="user.photoURL"/>
					<div class="subtitle" style="margin-bottom: 0.6rem">{{user.displayName}}</div>
					<div class="subtitle" style="font-size: 100%; opacity: 0.6">{{user.email}}</div>
					<button class="button is-primary" @click="logout">Log out</button>
				</div>
				<div key="chat" class="insides" v-if="activeNav === 'chat'">
					<div class="messages">
						<div :class="`message-single from-${item.from}`" v-for="(item, index) in chatMessages" :key="'m_' + index">
							<div class="message-content">{{item.text}}</div>
						</div>
					</div>
					<form @submit.prevent="sendMessage">
						<input type="text" v-model="message" placeholder="Enter your message">
					</form>
				</div>
				<ul key="nav" v-if="activeNav === 'nav'">
					<li>
						<nuxt-link to="/learn/0">
							<i class="fas fa-fw fa-font"></i>
							Nederlands
						</nuxt-link>
						<ul>
							<li v-for="(item, index) in mathOptions.c_0" :key="'nederlands_' + index"><nuxt-link :to="`/learn/0/${item.id}`">{{item.name}}</nuxt-link></li>
						</ul>
					</li>
					<li>
						<nuxt-link to="/learn/1">
							<i class="fas fa-fw fa-font"></i>
							Engels
						</nuxt-link>
						<ul>
							<li v-for="(item, index) in mathOptions.c_1" :key="'engels_' + index"><nuxt-link :to="`/learn/1/${item.id}`">{{item.name}}</nuxt-link></li>
						</ul>
					</li>
					<li>
						<nuxt-link to="/learn/2">
							<i class="fas fa-fw fa-calculator"></i>
							Wiskunde
						</nuxt-link>
						<ul>
							<li v-for="(item, index) in mathOptions.c_2" :key="'wiskunde_' + index"><nuxt-link :to="`/learn/2/${item.id}`">{{item.name}}</nuxt-link></li>
						</ul>
					</li>
					<li>
						<nuxt-link to="/learn/3">
							<i class="fas fa-fw fa-globe-africa"></i>
							Aardrijkskunde
						</nuxt-link>
						<ul>
							<li v-for="(item, index) in mathOptions.c_3" :key="'aardrijkskunde_' + index"><nuxt-link :to="`/learn/3/${item.id}`">{{item.name}}</nuxt-link></li>
						</ul>
					</li>
					<li>
						<nuxt-link to="/learn/4">
							<i class="fas fa-fw fa-landmark"></i>
							Geschiedenis
						</nuxt-link>
						<ul class="timeline">
							<div class="before">
								<li class="item-completed" v-for="(item, index) in details.relatedItems['i_m1']" :key="'kg_' + index">
									<nuxt-link :to="`/learn/4/${item.from_concept.id}`">
										<i class="fas fa-fw fa-circle"></i>
										{{item.from_concept.name}}
									</nuxt-link>
								</li>
							</div>
							<div class="present">
								<span v-for="(item, index) in details.relatedItems['i_0']" :key="'kg_' + index">
									<li class="item-current" v-if="true">
										<nuxt-link :to="`/learn/4/${details.id}`">
											<i class="fas fa-fw fa-circle"></i>
											{{details.name}}
										</nuxt-link>
									</li>
									<li class="item-future">
										<nuxt-link :to="`/learn/4/${item.from_concept.id}`">
											<i class="far fa-fw fa-circle"></i>
											{{item.from_concept.name}}
										</nuxt-link>
									</li>
								</span>
							</div>
							<div class="after">
								<li class="item-future" v-for="(item, index) in details.relatedItems['i_1']" :key="'kg_' + index">
									<nuxt-link :to="`/learn/4/${item.from_concept.id}`">
										<i class="far fa-fw fa-circle"></i>
										{{item.from_concept.name}}
									</nuxt-link>
								</li>
							</div>
						</ul>
						<ul>
							<li v-for="(item, index) in mathOptions.c_4" :key="'geschiedenis_' + index"><nuxt-link :to="`/learn/4/${item.id}`">{{item.name}}</nuxt-link></li>
						</ul>
					</li>
				</ul>
			</div>
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
			<img class="h-image" alt="" :src="details.image">
			<div class="summary-text" v-html="marked(details.summary)" data-read-aloud />
			<iframe :src="`https://www.youtube.com/embed/${details.video}`" />
			<div v-if="!isHidden" :class="`card is-answer card-content has-background-white-bis ${isCorrect ? 'is-correct' : ''} ${isHidden ? 'is-invisible' : ''}`">
				<span class="tag is-danger">Snelle vraag</span>
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
			<audio :src="`https://agastya-services.oswaldlabs.com/read-aloud/?text=${encode(details.summary)}`" controls />
		</div>
		<div class="progress">
			<div class="progress-value" :style="`width: ${progressPercent}%`"></div>
		</div>
		<iframe v-if="chatting" class="chatbot" src="https://console.dialogflow.com/api-client/demo/embedded/1b37d0e9-c3ab-429c-b87f-7cb50a473f21"></iframe>
	</main>
</template>

<script>
import Hovercard from "hovercard";
import marked from "marked";
import { LOGOUT } from '@/store/user';
import "@/node_modules/hovercard/build/index.css";
import firestore from "@/services/firestore";
export default {
	data() {
		return {
			activeNav: "nav",
			loading: true,
			points: 0,
			chatMessages: [
				{
					text: "Hallo! 👋",
					from: "bot"
				},
				{
					text: "Hoe kan ik helpen?",
					from: "bot"
				}
			],
			tries: 0,
			details: {
				related: {},
				relatedItems: {
					i_m1: [],
					i_0: [],
					i_1: []
				}
			},
			chatting: false,
			progressPercent: 0,
			message: "",
			isCorrect: false,
			increasing: false,
			isHidden: false,
			mathOptions: {}
		}
	},
	computed: {
		user() {
			return this.$store.state.user.profile;
		}
	},
	mounted() {
		if (this.user && this.user.uid) {
			firestore.collection("users").doc(this.user.uid).get().then(doc => {
				this.points = doc.data().points;
			});
		}
		this.setup();
		this.$axios.get("https://hackathon.anandchowdhary.com/concepts")
			.then(data => {
				for (let i = 0; i < data.data.results.length; i++) {
					this.mathOptions['c_' + data.data.results[i].category] = this.mathOptions['c_' + data.data.results[i].category] || [];
					this.mathOptions['c_' + data.data.results[i].category].push(data.data.results[i]);
				}
				this.$forceUpdate();
            });
    },
	methods: {
        fetchPoints() {
            firestore.collection("users").doc(this.user.uid).get().then(doc => {
                this.points = doc.data().points;
            });
        },
		sendMessage() {
			this.chatMessages.push({
				from: "user",
				text: this.message
			});
			this.$axios.get("https://api.dialogflow.com/v1/query?v=20150910&lang=nl&sessionId=24978328e&query=" + encodeURIComponent(this.message), {
					headers: {
						Authorization: "Bearer 5008c94ea2954924818204e3791ba416"
					}
				}).then(response => {
					this.typing = false;
					this.chatMessages.push({
						text: response.data.result.fulfillment.messages[0].speech,
						from: "bot"
					});
					setTimeout(() => {
						document.querySelector(".messages").scrollTo(0, document.querySelector(".messages").scrollHeight);
					}, 5);
				});
			this.message = "";
			setTimeout(() => {
				document.querySelector(".messages").scrollTo(0, document.querySelector(".messages").scrollHeight);
			}, 5);
		},
		encode(text) {
			return encodeURIComponent(text);
		},
		logout() {
			this.$store.dispatch(LOGOUT);
		},
		setup() {
			this.loading = true;
			this.$axios.get("https://hackathon.anandchowdhary.com/concepts/?id=" + this.$route.params.id)
				.then(data => {
					this.details = data.data.results[0];
					this.details.relatedItems = {
						i_m1: [],
						i_0: [],
						i_1: []
					};
					for (let i = 0; i < this.details.related.length; i++) {
						if (this.details.related[i].level === -1) this.details.relatedItems.i_m1.push(this.details.related[i]);
						if (this.details.related[i].level === 1) this.details.relatedItems.i_1.push(this.details.related[i]);
						if (this.details.related[i].level === 0) this.details.relatedItems.i_0.push(this.details.related[i]);
					}
					this.loading = false;
					setTimeout(() => {
						["gehele getallen", "optellen", "factor", "concreet", "voorwaarde", "vermenigvuldiging", "automatiseringsprobleem", "beheersen", "toegepast", "de som", "irrationele getallen", "complexe getallen", "breuken", "inverse", "Grensvlak", "Aardkorst", "Atmosfeer", "provincies", "bestuurslaag", "inwoners", "oppervlakte", "Vulcanus", "lava", "krater", "gas", "natuurramp", "lava", "aardkorst", "natuurramp", "hypocentrum", "breuklijnen", "aardplaten", "magma", "archeologen", "Lage Landen", "Julius Ceasar", "De Bello Gallico", "prehistorie", "protohistorie", "Egypte", "Soemerië", "bronstijd ", "ijzertijd", "mammoeten", "gereedschap", "Vlaanderen ", "graf", "Nederland", "moerassen", "reus", "dinosauriërs", "Grieken", "Romeinen", "Cultuur", "schrift", "prehistorie", "middeleeuwen", "oudheid", "Na christus", "Romeinese Rijk", "Amerika", "Boekdrukkunst", "volksverhuizingen"].forEach(importantTerms => {
							document.querySelector(".summary-text").innerHTML = document.querySelector(".summary-text").innerHTML.replace(importantTerms, `<span class="hovercard">${importantTerms}</span>`);
						});
						setTimeout(() => {
							const card = new Hovercard({
								lang: "nl"
							});
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
		eDo(script) {
			eval(script);
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
			this.tries++;
		},
		checkAnswer() {
			this.isCorrect = true;
			let givePoints = 30;
			if (this.tries === 1) givePoints = 20;
			if (this.tries === 2) givePoints = 10;
			if (this.tries >= 3) givePoints = 0;
			const newPoints = this.points + givePoints;
			if (this.user && this.user.uid) {
				firestore.collection("users").doc(this.user.uid).update({
					points: newPoints
				});
			}
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
.chatbot {
	position: fixed;
	bottom: 0;
	height: 60vh;
	right: 5.75rem;
	background-color: #fff;
	margin: 0;
	box-shadow: 0px 0px 30px rgba(0, 0, 0, 0.3);
	width: 350px;
}
.progress {
	position: fixed;
	left: 400px; right: 0;
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
	width: 400px;
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
	margin-left: -175px;
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
	z-index: 19;
	height: 390px;
}
p + .card {
	margin-top: 3rem;
}
.button {
	transition: 1s;
	margin-bottom: 0.25rem;
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
	a, button {
		background: none;
		border: 0;
		display: block;
		width: 70px;
		height: 70px;
		line-height: 70px;
		color: rgba(0, 0, 0, 0.5);
		font-size: 24px;
		text-align: center;
		&:focus {
			outline: 0; // Don't ever do
			// This is only to record a screen video
		}
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
				padding-bottom: 1px;
				li a {
					padding: 0 1rem;
					margin-bottom: 1rem;
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
audio {
	position: fixed;
	height: 100px !important;
	bottom: 1rem;
	left: 50%;
	z-index: 5;
}
.h-image {
	max-width: 300px;
	float: left;
	margin-right: 2rem;
	margin-bottom: 1rem;
}
.insides {
	margin-left: 70px;
	padding: 1rem;
	.messages {
		max-height: 90vh;
		overflow-y: auto;
		.message-single {
			display: flex;
			margin-bottom: 1rem;
			.message-content {
				background-color: #fff;
				padding: 0.65rem 1rem;
				border-radius: 2rem;
			}
			&.from-user {
				justify-content: flex-end;
				.message-content {
					background-color: #3498db;
					color: #fff;
				}
			}
		}
	}
	form {
		position: absolute;
		bottom: 1rem;
		right: 1rem;
		left: calc(70px + 1rem);
		input {
			font: inherit;
			padding: 0.5rem 1rem;
			border-radius: 0.25rem;
			border: 1px solid #ddd;
			width: 100%;
		}
	}
}
.button.is-secondary.is-fullwidth +
.button.is-secondary.is-fullwidth {
	margin-top: 1rem;
}
.item-completed {
	color: #aaa;
}
.timeline {
	overflow-x: hidden;
}
.after, .before, .present {
	width: 600px;
	margin-left: -150px;
	.item-future, .item-completed, .item-current {
		display: inline-block;
		a {
			padding-right: 0;
		}
	}
	&::before {
		content: "";
		position: absolute;
		left: 0;
		top: 0;
		bottom: 0;
		background-image: linear-gradient(to right, #fff, transparent);
		z-index: 3;
		pointer-events: none;
		width: 5rem;
	}
	&::after {
		content: "";
		position: absolute;
		right: 0;
		pointer-events: none;
		top: 0;
		bottom: 0;
		background-image: linear-gradient(to right, transparent, #fff);
		z-index: 3;
		width: 5rem;
	}
}
.timeline {
	text-align: center;
	position: relative;
	i {
		position: relative;
		z-index: 1;
	}
}
</style>
