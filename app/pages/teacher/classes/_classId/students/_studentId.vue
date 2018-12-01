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
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <section class="container">
            {{studentData}}
        </section>
    </main>
</template>

<style scoped></style>


<script>
import firestore from '@/services/firestore';

export default {
  data () {
    return {
        classId: null,
        studentId: null,
        classData: null,
        studentData: {},
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
