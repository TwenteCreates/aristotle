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
                        <!-- <track-doughnut-chart :chartData="getDoughnutChartData" /> -->
                    </div>
                </div>
                <div class="column is-4">
                    <div class="box">
                        <track-doughnut-chart :chartData="doughnutChartData" />
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

</style>


<script>
import firestore from '@/services/firestore';
import TrackDoughnutChart from '@/components/TrackDoughnutChart';

export default {
  layout: 'duo',
  components: {
    TrackDoughnutChart,
  },
  data () {
    return {
        dataItem: '',
        schools: null,
        pupilsNumber: 0,
        motivationNumber: 0,
        dropoutNumber: 0,
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
    };
  },
  mounted() {
      this.fetchSchools();
      this.fetchPupilsNumber();
      this.fetchMotivationNumber();
      this.fetchDropoutNumber();
      this.fetchDoughnutChartData();
  },
  methods: {
    fetchSchools() {
        firestore.collection("schools").onSnapshot(querySnapshot => {
            this.schools = [];
            querySnapshot.forEach(doc => {
                this.schools.push({...doc.data(), id: doc.id});
            });
        });
    },
    fetchPupilsNumber() {
        this.$axios.get('https://hackathon.anandchowdhary.com/pupils/').then(res => {
            this.pupilsNumber = res.data.count;
        })
    },
    fetchMotivationNumber() {
        this.$axios.get('https://hackathon.anandchowdhary.com/pupils/?school_motivation_score__gt=0.01&school_motivation_score__lt=0.5').then(res => {
            this.motivationNumber = res.data.count;
        })
    },
    fetchDropoutNumber() {
        this.$axios.get('https://hackathon.anandchowdhary.com/pupils?ever_registered_as_school_drop_out=1').then(res => {
            this.dropoutNumber = res.data.count;
        })
    },
    fetchDoughnutChartData() {
        const promises = []
        for(let i = 0; i < 4; i++) {
            promises.push(this.$axios.get(`https://hackathon.anandchowdhary.com/pupils?study_track_9th=${i}`));
        }

        Promise.all(promises).then(res => {
            for(let i = 0; i < 4; i++) {
                this.doughnutChartData.datasets[0].data[i] = res[i].data.count;
            }
        })
    }
  }
};
</script>
