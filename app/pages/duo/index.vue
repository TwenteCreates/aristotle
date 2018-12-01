<template>
    <main>
        <section class="hero is-info is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        DUO dashboard
                    </h1>
                    <h2 class="subtitle">
                        Overview and insights about the status of the learning process in the Netherlands
                    </h2>
                </div>
            </div>
        </section>

        <section class="container stats-container">
            <div class="columns is-mobile">
                Map here
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

export default {
  layout: 'duo',
  components: {
  },
  data () {
    return {
        dataItem: '',
        schools: null,
    };
  },
  mounted() {
  },
  methods: {
    fetchSchools() {
        firestore.collection("schools").onSnapshot(querySnapshot => {
            this.schools = [];
            querySnapshot.forEach(doc => {
                const event = doc.data();
                this.schools.push({...event, id: doc.id});
            });
        });
    }
  }
};
</script>
