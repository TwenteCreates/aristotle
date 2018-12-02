<template>
    <main>
        <section class="hero is-info is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 v-if="!schoolData">Loading...</h1>
                    <div v-else class="columns">
                        <!-- <div class="column is-2">
                            <div class="image"
                            :style="`background-image: url('https://tse2.mm.bing.net/th?q=${schoolData.instellings_naam}+${schoolData.gemeentenaam}+Nederland&w=250&h=250&p=0&dpr=2&adlt=moderate')`"
                            ></div>
                        </div> -->
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
            <section class="container stats-container">
                <div class="columns is-mobile">
                    <div class="column is-4">
                        <div class="box hero is-info is-bold">
                            <div class="hero-body">
                                <div class="container">
                                    <h1 class="title">
                                        {{pupilsNumber}}
                                    </h1>
                                    <h2 class="subtitle">
                                        active pupils
                                    </h2>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="box hero is-info is-bold">
                            <div class="hero-body">
                                <div class="container">
                                    <h1 class="title">
                                        {{classesNumber}}
                                    </h1>
                                    <h2 class="subtitle">
                                        active classes
                                    </h2>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="box hero is-info is-bold">
                            <div class="hero-body">
                                <div class="container">
                                    <h1 class="title">
                                        {{teachersNumber}}
                                    </h1>
                                    <h2 class="subtitle">
                                        active teachers
                                    </h2>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section class="container">
                <div class="columns">
                    <div class="column is-8">
                        <div class="box">
                            <school-line-chart :chartData="getClassChartData" />
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="box change-box">
                            <div>
                                <p class="title">Daily</p>
                                <p>Based on {{getDayDataSize}} submissions</p>
                                <p class="subtitle">Average score: {{getDailyAverage}}</p>
                            </div>

                            <div>
                                <p class="title">Monthly</p>
                                <p>Based on {{getMonthDataSize}} submissions</p>
                                <p class="subtitle">Average score: {{getMonthlyAverage}}</p>
                            </div>

                            <div>
                                <p class="title">Yearly</p>
                                <p>Based on {{getYearDataSize}} submissions</p>
                                <p class="subtitle">Average score: {{getYearlyAverage}}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </section>
    </main>
</template>

<style lang="scss">
.icon {
    margin-left: 0.25rem;
}

.image {
    min-height: 250px;
}

.stats-container {
    margin-top: 1rem;
    margin-bottom: 1rem;

    .title {
        font-size: 3em;
    }
}

.change-box {
    min-height: 440px;

    .title {
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }

    .subtitle {
        margin: 0;
    }
}
</style>



<script>
import firestore from '@/services/firestore';
import SchoolLineChart from '@/components/SchoolLineChart'

export default {
  layout: 'duo',
  components: {
    SchoolLineChart
  },
  data () {
    return {
        schoolId: null,
        schoolData: null,
        classesNumber: 0,
        pupilsNumber: 0,
        teachersNumber: 0,
    };
  },
  computed: {
    getClassChartData() {
        return {
            labels: [
                'Wednesday, 28 Nov 2018',
                'Thursday, 29 Nov 2018',
                'Friday, 30 Nov 2018',
                'Saturday, 1 Dec 2018',
                'Sunday, 2 Dec 2018'
            ],
            datasets: [
                {
                    label: 'Average points per student (5d)',
                    backgroundColor: '#209cee',
                    data: [286, 198, 234, 186, 213],
                }
            ]
        }
    },
    getDayDataSize() {
        return 87;
    },
    getDailyAverage() {
        return 213;
    },
    getMonthDataSize() {
        return '12k';
    },
    getMonthlyAverage() {
        return 110;
    },
    getYearDataSize() {
        return '87k';
    },
    getYearlyAverage() {
        return 138;
    },
  },
  mounted() {
    this.schoolId = this.$route.params.schoolId;
    const seed = parseInt(this.schoolId);
    this.pupilsNumber = 178 + seed * 3;
    this.classesNumber = seed * 2;
    this.teachersNumber = 11 + seed * 2;
    this.fetchSchool();
  },
  methods: {
    fetchSchool() {
        this.$axios.get(`https://hackathon.anandchowdhary.com/primary_schools/?limit=10&brin_nummer=${this.schoolId}`).then(res => {
            this.schoolData = res.data.results[0];
        });
    },

  }
};
</script>
