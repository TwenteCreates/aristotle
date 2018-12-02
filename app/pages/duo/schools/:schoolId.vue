<template>
    <main>
        <section class="hero is-info is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 v-if="!schoolData">Loading...</h1>
                    <div v-else class="columns">
                        <div class="column is-2">
                            <div class="card-image"
                            :style="`background-image: url('https://tse2.mm.bing.net/th?q=${schoolData.instellings_naam}+${schoolData.gemeentenaam}+Nederland&w=250&h=250&p=0&dpr=2&adlt=moderate')`"
                            ></div>
                        </div>
                        <div class="column">
                            <h1 class="title">
                                {{schoolData.instellings_naam}}
                            </h1>
                            <h2 class="subtitle">
                                {{schoolData.plaatsnaam}}, {{schoolData.provincie.toUpperCase()}}
                            </h2>
                            <p class="subtitle">
                                <a :href="`${schoolData.internetadres}`" target="_blank">
                                    {{schoolData.internetadres}}
                                    <span class="icon is-small">
                                        <i class="fas fa-external-link-alt"></i>
                                    </span>
                                </a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="container">
            {{schoolData}}
        </section>
    </main>
</template>

<style lang="scss">
.icon {
    margin-left: 0.25rem;
}
</style>



<script>
import firestore from '@/services/firestore';

export default {
  layout: 'duo',
  data () {
    return {
        schoolId: null,
        schoolData: null,
    };
  },
  mounted() {
    this.schoolId = this.$route.params.schoolId;
    this.fetchSchool();
  },
  methods: {
    fetchSchool() {
        this.$axios.get(`https://hackathon.anandchowdhary.com/primary_schools/?limit=10&brin_nummer=${this.schoolId}`).then(res => {
            this.schoolData = res.data.results[0];
        });
    }
  }
};
</script>
