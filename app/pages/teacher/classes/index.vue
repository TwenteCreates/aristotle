<template>
    <main>
        <section class="hero is-primary is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        Classes Overview
                    </h1>
                    <h2 class="subtitle">
                        An overview of all the classes assigned to you.
                    </h2>
                </div>
            </div>
        </section>
        <!-- <section class="container">
            <div class="column is-12 chart-wrapper box">
                <class-line-chart :chartData="getClassChartData" />
            </div>
        </section> -->

        <section class="container classes-container">
            <!-- <h1 class="title">Classes</h1> -->
            <classes-tiles :classes="classes" />
        </section>
    </main>
</template>

<style scoped>
.chart-wrapper, .classes-container {
    margin-top: 1rem;
    margin-bottom: 1.5rem;
}
</style>


<script>
import firestore from '@/services/firestore';
import ClassesTiles from '@/components/ClassesTiles';
import ClassLineChart from '@/components/ClassLineChart';


export default {
  layout: 'teacher',
  components: {
    ClassesTiles,
    ClassLineChart
  },
  data () {
    return {
        dataItem: '',
        classes: [],
    };
  },
  computed: {
    getClassChartData() {
        return {
            // labels: this.analyses.map(analysis => analysis.createdAt.toDate().toLocaleDateString()),
            labels: [],
            datasets: [
                {
                    label: 'Average class grades',
                    backgroundColor: '#2581c3',
                    data: [],
                }
            ]
        }
    }
  },
  mounted() {
    this.fetchClasses();
  },
  methods: {
    fetchClasses() {
        firestore.collection("classes").orderBy('name').onSnapshot(querySnapshot => {
            this.classes = [];
            querySnapshot.forEach(doc => {
                const classData = doc.data();
                this.classes.push({...classData, id: doc.id});
            });
        });
    }
  }
};
</script>
