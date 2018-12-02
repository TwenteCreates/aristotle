<template>
    <main>
        <section class="hero is-primary is-bold">
            <div class="hero-body">
                <div class="container">
                    <div class="columns">
                        <div class="column is-2">
                            <figure class="image is-128x128">
                                <img class="is-rounded" :src="studentData.photoUrl"/>
                            </figure>
                        </div>
                        <div class="column">
                            <h1 class="title">
                                {{studentData.name}}
                            </h1>
                            <h2 class="subtitle">
                                {{studentData.email}}
                            </h2>
                            <h1>
                                Last activity: <br/>
                                {{studentData.lastSignInTime}}
                            </h1>
                            <h1>
                                {{studentData.points}} total points
                            </h1>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <section class="container">
            <section class="container stats-container">
                <div class="columns is-mobile">
                    <div class="column is-4">
                        <div class="box hero is-bold">
                            <div class="hero-body">
                                <div class="container">
                                    <h1 class="title">
                                        {{wiskunde}} %
                                    </h1>
                                    <h2 class="subtitle">
                                        'Wiskunde' progress
                                    </h2>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="box hero is-bold">
                            <div class="hero-body">
                                <div class="container">
                                    <h1 class="title">
                                        {{aardrijkskunde}} %
                                    </h1>
                                    <h2 class="subtitle">
                                        'Aardrijkskunde' progress
                                    </h2>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="column is-4">
                        <div class="box hero is-bold">
                            <div class="hero-body">
                                <div class="container">
                                    <h1 class="title">
                                        {{geschiedenis}} %
                                    </h1>
                                    <h2 class="subtitle">
                                        'Geschiedenis' active teachers
                                    </h2>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
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

export default {
  layout: 'teacher',
  data () {
    return {
        classId: null,
        studentId: null,
        classData: null,
        studentData: {},
        wiskunde: 28,
        aardrijkskunde: 49,
        geschiedenis: 76,
    };
  },
  mounted() {
    this.classId = this.$route.params.classId;
    this.studentId = this.$route.params.studentId;
    this.fetchClass();
    this.fetchStudent();
  },
  methods: {
    fetchClass() {
        firestore.collection("classes").doc(this.classId).get().then(doc => {
            this.classData = {id: doc.id, ...doc.data()};
        });
    },
    fetchStudent() {
        firestore.collection("users").doc(this.studentId).get().then(doc => {
            this.studentData = {id: doc.id, ...doc.data()};
        });
    }
  }
};
</script>
