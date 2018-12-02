<template>
    <main>
        <section class="hero is-primary is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        Teacher Dashboard
                    </h1>
                    <h2 class="subtitle">
                        Overview and insights about the status of the learning process.
                    </h2>
                </div>
            </div>
        </section>

        <!-- <section class="container">
            <a class="button is-primary" @click="$router.push('/teacher/classes')">Classes overview</a>
        </section> -->

        <section class="container stats-container">
            <div class="columns is-mobile">
                <div class="column is-3">
                    <div class="box hero is-info is-bold">
                        <div class="hero-body">
                            <div class="container">
                                <h1 class="title">
                                    {{pupilsNumber}}
                                </h1>
                                <h2 class="subtitle">
                                    pupils enrolled
                                </h2>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="column is-3">
                    <div class="box hero is-warning is-bold">
                        <div class="hero-body">
                            <div class="container">
                                <h1 class="title" style="color: white">
                                    {{classesNumber * 2}}
                                </h1>
                                <h2 class="subtitle" style="color: white">
                                    working groups
                                </h2>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="column is-3">
                    <div class="box hero is-primary is-bold">
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
                <div class="column is-3">
                    <div class="box hero is-danger is-bold">
                        <div class="hero-body">
                            <div class="container">
                                <h1 class="title">
                                    {{unasweredQuestionNumber}}
                                </h1>
                                <h2 class="subtitle">
                                    unanswered questions
                                    <br/>
                                </h2>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="container">
            <div class="columns">
                <div class="column">
                    <div class="box">
                        <teacher-line-chart :chartData="getTeacherChartData"/>
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>

<style lang="scss" scoped>
.container {
    margin-top: 1rem;
    margin-bottom: 1rem;
}

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
import ClassesTiles from '@/components/ClassesTiles';
import TeacherLineChart from '@/components/TeacherLineChart';

export default {
  layout: 'teacher',
  components: {
    ClassesTiles,
    TeacherLineChart
  },
  data () {
    return {
        dataItem: '',
        classes: null,
        classesNumber: 4,
        pupilsNumber: 58,
        unasweredQuestionNumber: 3,
    };
  },
  mounted() {
  },
  computed: {
    getTeacherChartData() {
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
                    label: 'Cummulative points',
                    backgroundColor: '#209cee',
                    data: [23, 22, 32, 11, 33],
                },
                {
                    label: 'Quests attempted',
                    backgroundColor: '#00d1b2',
                    data: [38, 33, 59, 24, 43],
                }
            ]
        }
    }
  },
  methods: {
    fetchClasses() {
        firestore.collection("classes").onSnapshot(querySnapshot => {
            this.classes = [];
            querySnapshot.forEach(doc => {
                const event = doc.data();
                this.classes.push({...event, id: doc.id});
            });
        });
    }
  }
};
</script>
