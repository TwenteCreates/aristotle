<template>
	<main>
		<aside>
			<div class="vertical-nav">
				<nuxt-link to="/"><i class="fas fa-chart-line"></i></nuxt-link>
				<nuxt-link to="/learn/wiskunde/1"><i class="fas fa-book-reader"></i></nuxt-link>
				<nuxt-link to="/chat" class="active"><i class="fas fa-comments"></i></nuxt-link>
				<nuxt-link to="/settings"><i class="fas fa-cogs"></i></nuxt-link>
			</div>
		</aside>
		<div class="content">
			<iframe src="https://console.dialogflow.com/api-client/demo/embedded/1b37d0e9-c3ab-429c-b87f-7cb50a473f21"></iframe>
		</div>
	</main>
</template>

<style lang="scss">
iframe {
	height: 70vh;
	width: 100%;
	border: 0;
}
.content {
	width: 700px;
	position: absolute;
	left: 50%;
	padding: 5rem 0;
	margin-left: -315px;
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
