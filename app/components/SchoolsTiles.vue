<template>
    <div v-if="!schools"><h2>Loading</h2></div>
    <div v-else class="columns is-mobile is-multiline is-centered is-mobile">
        <div v-for="school in schools" :key="school.id" class="column is-3">
            <div class="card" @click="$router.push(`/duo/schools/${school.brin_nummer}`)">
                <div
                    class="card-image"
                    :style="`background-image: url('https://tse2.mm.bing.net/th?q=${school.instellings_naam}+${school.gemeentenaam}+Nederland+&w=250&h=250&p=0&dpr=2&adlt=moderate')`"
                >
                </div>
                <div class="card-content">
                    <div class="media">
                        <div class="media-content">
                            <p class="title">{{school.instellings_naam}}</p>
                            <p class="subtitle">{{school.plaatsnaam}}, {{school.provincie.toUpperCase()}}</p>
                        </div>
                    </div>

                    <div class="content">
                        <!-- Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                        Phasellus nec iaculis mauris. <a>@bulmaio</a>.
                        <a href="#">#css</a> <a href="#">#responsive</a>
                        <br>
                        <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time> -->
                        <p class="card-footer-item">
                            <a :href="`${school.internetadres}`" target="_blank">
                                <!-- {{school.internetadres}} -->
                                <span class="icon is-small">
                                    <i class="fas fa-external-link-alt"></i>
                                </span>
                            </a>
                        </p>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<style lang="scss" scoped>
.card {
    min-height: 500px;
}

.card-image {
    min-height: 200px;
    background-size: cover;
}

</style>

<script>
  export default {
    props: {
        schools: Array,
    },
    data () {
        return {}
    }
  }
</script>
