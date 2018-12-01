<template>
    <main>
        <section class="hero is-primary is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        Teacher dashboard
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
                <div class="column is-4">
                    <div class="box hero is-info is-bold">
                        <div class="hero-body">
                            <div class="container">
                                <h1 class="title">
                                    Medium title
                                </h1>
                                <h2 class="subtitle">
                                    Medium subtitle
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
                                    Medium title
                                </h1>
                                <h2 class="subtitle">
                                    Medium subtitle
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
                                    Medium title
                                </h1>
                                <h2 class="subtitle">
                                    Medium subtitle
                                </h2>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
</template>

<style scoped>
.container {
    margin-top: 1rem;
    margin-bottom: 1rem;
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
  },
  data () {
    return {
        dataItem: '',
        classes: null,
    };
  },
  mounted() {
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
