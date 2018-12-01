
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
	background-color: #005ea5;
	position: absolute;
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
            color: #005ea5;
		}
	}
}

</style>

<script>
import teacherLayout from '@/layouts/teacher';
export default {
    extends: teacherLayout,
    data() {
        return {
            menuItems: [
                {name: 'Overall dashboard', icon: 'fas fa-map', routeName: 'duo'},
                {name: 'Historical data', icon: 'fas fa-history', routeName: 'duo-history'},
                {name: 'Profile admin', icon: 'fas fa-cogs', routeName: 'profile-duo'},
            ]
        }
    },
}
</script>
