<template>
    <main>
        <section class="hero is-secondary is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        Students of the class {{classData.name}}
                    </h1>
                    <h2 class="subtitle">

                    </h2>
                </div>
            </div>
        </section>
        <section class="container">
            Students table
        </section>
    </main>
</template>

<style scoped></style>


<script>
import firestore from '@/services/firestore';

export default {
  data () {
    return {
        classId: '',
        classData: {}
    };
  },
  mounted() {
    this.classId = this.$route.params.classId
    this.fetchClass();
  },
  methods: {
      fetchClass() {
        firestore.collection("classes").doc(this.classId).get().then(doc => {
            console.log(doc);
            this.classData = {id:doc.id, ...doc.data()};
        });
      }
  }
};
</script>
