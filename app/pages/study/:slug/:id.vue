<template>
	<main>
		<nav class="navbar is-dark" role="navigation" aria-label="main navigation">
			<div class="navbar-brand">
				<a class="navbar-item">Aristotle</a>
				<a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
					<span aria-hidden="true"></span>
					<span aria-hidden="true"></span>
					<span aria-hidden="true"></span>
				</a>
			</div>
			<div id="navbarBasicExample" class="navbar-menu">
				<div class="navbar-start">
					<a class="navbar-item">Study</a>
					<a class="navbar-item">Progress</a>
					<div class="buttons" style="margin-left: 1rem">
						<a class="button is-primary">
							<strong>Save for later</strong>
						</a>
					</div>
				</div>
				<div class="navbar-end">
					<a class="navbar-item">Have a question?</a>
					<div class="navbar-item has-dropdown is-hoverable">
						<a class="navbar-link">{{user.profile.displayName}}</a>
						<div class="navbar-dropdown">
							<a class="navbar-item">About</a>
							<a class="navbar-item">Jobs</a>
							<a class="navbar-item">Contact</a>
							<hr class="navbar-divider">
							<a class="navbar-item">Report an issue</a>
						</div>
					</div>
				</div>
			</div>
		</nav>
		<div class="container-fluid">
			<div class="columns">
				<div class="column is-one-fifth">
					<h2 class="has-text-weight-semibold">Syllabus</h2>
					<ul>
						<li>
							<router-link to="/study/newtons-laws-of-motion">
								Newton's laws of motion
							</router-link>
							<ul>
								<router-link to="/study/newtons-laws-of-motion/introduction">
									Introduction
								</router-link>
								<router-link to="/study/newtons-laws-of-motion/applications">
									Applications
								</router-link>
								<router-link to="/study/newtons-laws-of-motion/quiz">
									Quiz
								</router-link>
							</ul>
						</li>
						<li>
							<router-link to="/study/normal-force-and-contact-force">
								Normal force and contact force
							</router-link>
						</li>
						<li>
							<router-link to="/study/balanced-and-unbalanced-forces">
								Balanced and unbalanced forces
							</router-link>
						</li>
						<li>
							<router-link to="/study/inclined-planes-and-friction">
								Inclined planes and friction
							</router-link>
						</li>
						<li>
							<router-link to="/study/tension">
								Tension
							</router-link>
						</li>
					</ul>
				</div>
				<div class="column container text" style="max-width: 640px">
					<h1 class="title">Newton&rsquo;s laws of motion</h1>
					<p>The motion of an aircraft through the air can be explained and described by physical principals discovered over 300 years ago by Sir Isaac Newton. Newton worked in many areas of mathematics and physics. He developed the theories of gravitation in 1666, when he was only 23 years old. Some twenty years later, in 1686, he presented his three laws of motion in the "Principia Mathematica Philosophiae Naturalis." The laws are shown above, and the application of these laws to aerodynamics are given on separate slides.</p>
					<p class="is-size-6 has-text-grey-light">Source: NASA &middot; Public domain</p>
					<iframe id="ytplayer" type="text/html" src="https://www.youtube.com/embed/kKKM8Y-u7ds" frameborder="0"></iframe>
					<p>This text</p>
				</div>
			</div>
		</div>
	</main>
</template>

<script>
export default {
	data() {
		return {
			user: {
				profile: {}
			}
		}
	},
	mounted() {
		this.user = this.$store.state.user;
	}
}
</script>


<style lang="scss">
.text {
	padding: 5rem 0;
	font-size: 110%;
	line-height: 1.75;
}
.is-one-fifth {
	color: #fff;
	background-color: #2c3e50;
	overflow-y: auto;
	padding-left: 0;
	padding-right: 0;
	h2 {
		text-align: center;
		margin: 1rem;
	}
	li a {
		border-top: 1px solid rgba(255, 255, 255, 0.1);
		display: block;
		padding: 0.75rem 1.75rem;
		color: inherit;
		&:hover {
			background-color: rgba(255, 255, 255, 0.05);
		}
		&.nuxt-link-active {
			background-color: rgba(0, 0, 0, 0.2);
			&:hover {
				background-color: rgba(0, 0, 0, 0.3);
			}
		}
		&.nuxt-link-exact-active {
			background-color: rgba(0, 0, 0, 0.3);
		}
	}
	li ul a {
		padding: 0.5rem 1.75rem;
		padding-left: 3rem;
		background-color: rgba(0, 0, 0, 0.2);
		border-top: 1px solid rgba(255, 255, 255, 0.05);
	}
}
nav.navbar.is-dark, .navbar-dropdown {
	background-color: #34495e;
	a {
		color: #fff;
	}
}

iframe {
	width: 100%;
	border: 0;
	margin: 2rem 0;
	height: 65%;
}
</style>
