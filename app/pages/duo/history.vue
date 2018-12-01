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
