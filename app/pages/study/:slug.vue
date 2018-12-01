<template>
	<main>
		<nav class="navbar" role="navigation" aria-label="main navigation">
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
					<a class="navbar-item">Home</a>
					<a class="navbar-item">Documentation</a>
					<div class="navbar-item has-dropdown is-hoverable">
						<a class="navbar-link">More</a>
						<div class="navbar-dropdown">
							<a class="navbar-item">About</a>
							<a class="navbar-item">Jobs</a>
							<a class="navbar-item">Contact</a>
							<hr class="navbar-divider">
							<a class="navbar-item">Report an issue</a>
						</div>
					</div>
				</div>
				<div class="navbar-end">
					<div class="navbar-item">
						<div class="buttons">
							<a class="button is-primary">
								<strong>Bookmark</strong>
							</a>
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
					<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.</p>
					<!-- <iframe id="ytplayer" type="text/html" width="640" height="360" src="https://www.youtube.com/embed/M7lc1UVf-VE" frameborder="0"></iframe> -->
				</div>
			</div>
		</div>
	</main>
</template>

<script>

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
		padding: 0.75rem 1.5rem;
		color: inherit;
		&:hover {
			background-color: rgba(255, 255, 255, 0.05);
		}
		&.nuxt-link-exact-active {
			background-color: rgba(0, 0, 0, 0.2);
		}
	}
}
nav.navbar {
	background-color: #34495e;
	a {
		color: #fff;
	}
}
</style>
