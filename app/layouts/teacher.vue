
<template>
    <div class="columns">
        <aside class="column is-narrow">
			<div class="vertical-nav">
				<a href="#" v-for="item in menuItems"
                    :key="item.icon"
                    :class="{active: isMenuItemActive(item)}"
                    @click.prevent="$router.push({name: item.routeName})">
                    <i :class="item.icon"></i>
                </a>
			</div>
		</aside>

        <div class="column">
            <nuxt />
        </div>
    </div>
</template>

<style lang="scss" scoped>
.vertical-nav {
	background-color: #455A64;
	position: fixed;
	left: 0;
    top: 0;
	bottom: 0;
	a {
		display: block;
		width: 70px;
		height: 70px;
		line-height: 70px;
		color: whitesmoke;
		font-size: 24px;
		text-align: center;
		&.active {
			background-color: whitesmoke;
            color: #455A64;
		}
	}
}

</style>

<script>
import defaultLayout from '@/layouts/default';
export default {
    extends: defaultLayout,
    data() {
        return {
            menuItems: [
                {name: 'Teacher dashboard', icon: 'fas fa-chalkboard-teacher', routeName: 'teacher'},
                {name: 'Teacher dashboard', icon: 'fas fa-users', routeName: 'teacher-classes'},
                {name: 'Teacher dashboard', icon: 'fas fa-cogs', routeName: 'profile-teacher'},
            ]
        }
    },
    methods: {
        isMenuItemActive(item) {
            return item.routeName === this.$route.name;
        }
    }
}
</script>
