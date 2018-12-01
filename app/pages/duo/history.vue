<template>
    <main>
        <section class="hero is-info is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        Historical data
                    </h1>
                    <h2 class="subtitle">
                        Historical data reports and visualisation
                    </h2>
                </div>
            </div>
        </section>

        <section class="container filters-container">
            <div class="columns">
                <div class="column is-4">
                    <b-field>
                        <b-select placeholder="Region" icon="map" expanded v-model="filters.region">
                            <option value="">Region</option>
                            <option value="3">Central Limburg</option>
                            <option value="4">North Limburg</option>
                            <option value="0">North of South Limburg (Sittard area)</option>
                            <option value="1">South-East Limburg (Heerlen area)</option>
                            <option value="2">South-West Limburg (Maastricht area)</option>
                        </b-select>
                    </b-field>
                </div>
                <div class="column is-2">
                    <b-field>
                        <b-select placeholder="Origin" icon="earth" expanded v-model="filters.origin">
                            <option value="">Origin</option>
                            <option value="0">Limburg</option>
                            <option value="1">Non-Dutch</option>
                            <option value="2">(Other) Dutch</option>
                        </b-select>
                    </b-field>
                </div>
                <div class="column is-2">
                    <b-field>
                        <b-select placeholder="Track levels" icon="bullseye-arrow" expanded v-model="filters.track">
                            <option value="">Track levels</option>
                            <option value="0">vmbo bl/kl</option>
                            <option value="1">vmbo gl/tl</option>
                            <option value="2">havo</option>
                            <option value="3">vwo</option>
                        </b-select>
                    </b-field>
                </div>
                <div class="column is-2">
                    <b-field>
                        <b-select placeholder="Support level" icon="lifebuoy" expanded v-model="filters.support">
                            <option value="">Support level</option>
                            <option value="0">No</option>
                            <option value="1">Some</option>
                            <option value="2">A lot</option>
                            <option value="3">Quite a lot</option>
                        </b-select>
                    </b-field>
                </div>
                <div class="column is-2">
                    <b-field>
                        <b-select placeholder="Gender" icon="gender-male-female" expanded v-model="filters.gender">
                            <option value="">Gender</option>
                            <option value="0">Male</option>
                            <option value="1">Female</option>
                        </b-select>
                    </b-field>
                </div>
            </div>
        </section>

        <!-- <section class="container">
            <div>
                {{filters.region}}
                {{filters.origin}}
                {{filters.track}}
                {{filters.support}}
                {{filters.gender}}
            </div>
        </section> -->

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
                                    pupils
                                </h2>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="box hero is-warning is-bold">
                        <div class="hero-body">
                            <div class="container">
                                <h1 class="title">
                                    {{motivationNumber}}
                                </h1>
                                <h2 class="subtitle">
                                    with a school motivation score below 5
                                </h2>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="column is-4">
                    <div class="box hero is-danger is-bold">
                        <div class="hero-body">
                            <div class="container">
                                <h1 class="title">
                                    {{dropoutNumber}}
                                </h1>
                                <h2 class="subtitle">
                                    ever registered as school drop out
                                </h2>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="container d-chart-container">
            <div class="columns">
                <div class="column is-8">
                    <div class="box">
                        <cito-bar-chart :chartData="getBarChartData"  />
                    </div>
                </div>
                <div class="column is-4">
                    <div class="box">
                        <track-doughnut-chart :chartData="getDoughnutChartData" />
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>

<style lang="scss" scoped>
.stats-container {
    margin-top: 1rem;
    margin-bottom: 1rem;

    .title {
        font-size: 3em;
    }
}

.filters-container {
    margin-top: 1.5rem;
    margin-bottom: 1rem;
}
</style>


<script>
import firestore from '@/services/firestore';
import TrackDoughnutChart from '@/components/TrackDoughnutChart';
import CitoBarChart from '@/components/CitoBarChart';

export default {
  layout: 'duo',
  components: {
    TrackDoughnutChart,
    CitoBarChart,
  },
  data () {
    return {
        dataItem: '',
        schools: null,
        pupilsNumber: 0,
        motivationNumber: 0,
        dropoutNumber: 0,
        filters: {
            region: null,
            origin: null,
            track: null,
            support: null,
            gender: null,
        },
        doughnutChartData: {
            datasets: [{
                data: [
                    0.25,
                    0.25,
                    0.25,
                    0.25,
                ],
                backgroundColor: [
                    '#00d1b2',
                    '#ff3860',
                    '#ffdd57',
                    '#005ea5',
                ],
                label: 'Dataset 1'
            }],
            labels: [
                'VMBO BL/KL',
                'VMBO GL/TL',
                'HAVO',
                'VWO'
            ]
        },
        barChartData: {
            labels: [],
            datasets: [{
                label: 'Study Skills Cito',
                backgroundColor: '#005ea5',
                data: []
            }, {
                label: 'Math Cito',
                backgroundColor: '#ffdd57',
                data: []
            }, {
                label: 'Language Cito',
                backgroundColor: '#ff3860',
                data: []
            }]
        },
    };
  },
  computed: {
      getDoughnutChartData() {
          return { ...this.doughnutChartData };
      },
      getBarChartData() {
          return { ...this.barChartData };
      }
  },
  mounted() {
      this.fetchData();
  },
  watch: {
    filters: {
        handler: function (newValue) {
            this.fetchData();
        },
        deep: true
    }
  },
  methods: {
    fetchData() {
      this.fetchPupilsNumber();
      this.fetchMotivationNumber();
      this.fetchDropoutNumber();
      this.fetchBarChartData();
      this.fetchDoughnutChartData();
    },
    fetchSchools() {
        firestore.collection("schools").onSnapshot(querySnapshot => {
            this.schools = [];
            querySnapshot.forEach(doc => {
                this.schools.push({...doc.data(), id: doc.id});
            });
        });
    },
    fetchPupilsNumber() {
        this.$axios.get(this.addFiltersToUrl('https://hackathon.anandchowdhary.com/pupils?random=&')).then(res => {
            this.pupilsNumber = res.data.count;
        })
    },
    fetchMotivationNumber() {
        this.$axios.get(this.addFiltersToUrl('https://hackathon.anandchowdhary.com/pupils/?school_motivation_score__gt=0.01&school_motivation_score__lt=0.5')).then(res => {
            this.motivationNumber = res.data.count;
        })
    },
    fetchDropoutNumber() {
        this.$axios.get(this.addFiltersToUrl('https://hackathon.anandchowdhary.com/pupils?ever_registered_as_school_drop_out=1'))
        .then(res => {
            this.dropoutNumber = res.data.count;
        })
    },
    fetchDoughnutChartData() {
        const promises = []
        for(let i = 0; i < 4; i++) {
            promises.push(this.$axios.get(this.addFiltersToUrl(`https://hackathon.anandchowdhary.com/pupils?study_track_9th=${i}`)));
        }

        Promise.all(promises).then(res => {
            for(let i = 0; i < 4; i++) {
                this.doughnutChartData.datasets[0].data[i] = res[i].data.count;
            }
        }).then(() => {
            // Trigger reactivity
            this.$set(this.doughnutChartData, 'labels', JSON.parse(JSON.stringify(this.doughnutChartData.labels)));
        })
    },
    fetchBarChartData() {
        const promises = []
        const START = 1995;
        const YEARS = 8;
        for(let i = START; i < START + YEARS; i++) {
            promises.push(this.$axios.get(this.addFiltersToUrl(`https://hackathon.anandchowdhary.com/pupils?student_birth_year=${i}`)));

            // Add the year as the label
            this.barChartData.labels.push(i);
        }

        this.barChartData.datasets[0].data = [];
        this.barChartData.datasets[1].data = [];
        this.barChartData.datasets[2].data = [];

        Promise.all(promises).then(res => {
            for(let i = 0; i < YEARS; i++) {
                // Filter cito students
                const citoStudents = res[i].data.results.filter(pupil => pupil.student_end_6th_year !== 0);

                // Take study skills scores;
                const citoStudyScores = citoStudents.map(pupil => pupil.correct_study_skills_cito);
                const citoMathScores = citoStudents.map(pupil => pupil.correct_math_cito);
                const citoLangScores = citoStudents.map(pupil => pupil.correct_language_cito);

                // Take averages and push them to the dataset
                this.barChartData.datasets[0].data.push(this.average(citoStudyScores).toFixed(2));
                this.barChartData.datasets[1].data.push(this.average(citoMathScores).toFixed(2));
                this.barChartData.datasets[2].data.push(this.average(citoLangScores).toFixed(2));
            }
        }).then(() => {
            // Trigger reactivity
            let labels = [];
            // Add the labels, also trigger the chart update.
            for(let i = START; i < START + YEARS; i++) {
                // Add the year as the label
                labels.push(i);
            }
            this.$set(this.barChartData, 'labels', labels);
        })


    },
    addFiltersToUrl(url) {
        url += this.filters.region ? '&region=' + this.filters.region : '';
        url += this.filters.origin ? '&origin=' + this.filters.origin : '';
        url += this.filters.track ? '&study_track_9th=' + this.filters.track : '' ;
        url += this.filters.support ? '&parent_support_home_lessons=' + this.filters.support : '';
        url += this.filters.gender ? '&gender=' + this.filters.gender : '';
        return url;
    },
    average(arr) {
        return arr.reduce((a, v) => a + v, 0 ) / arr.length;
    },
  }
};
</script>
