<template>
    <main>
        <section class="hero is-info is-bold">
            <div class="hero-body">
                <div class="container">
                    <h1 class="title">
                        DUO Dashboard
                    </h1>
                    <h2 class="subtitle">
                        Overview and insights about the status of the learning process in the Netherlands
                    </h2>
                </div>
            </div>
        </section>

        <section class="container region-container">
            <b-field>
                <b-select
                    placeholder="Region"
                    size="is-medium"
                    v-model="selectedRegion"
                    >
                    <option value="">Region</option>
                    <option v-for="region in regions" :key="region" >{{region}}</option>
                </b-select>
            </b-field>
        </section>

        <section class="container schools-container">
            <schools-tiles :schools="schools" />
        </section>
    </main>
</template>

<style scoped>
.container {
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.schools-container {
    display: flex;
    flex-wrap: wrap;
}
</style>


<script>
import firestore from '@/services/firestore';
import SchoolsTiles from '@/components/SchoolsTiles';

export default {
  layout: 'duo',
  components: {
      SchoolsTiles
  },
  data () {
    return {
        dataItem: '',
        schools: null,
        regions: [
            'Groningen',
            'Friesland',
            'Drenthe',
            'Overijssel',
            'Flevoland',
            'Gelderland',
            'Utrecht',
            'Noord-Holland',
            'Zuid-Holland',
            'Zeeland',
            'Noord-Brabant',
            'Limburg'
        ],
        selectedRegion: '',
    };
  },
  watch: {
      selectedRegion: {
        handler: function (old, newVal) {
            this.fetchSchools();
        }
      }

  },
  mounted() {
      this.fetchSchools();
  },
  methods: {
    fetchSchools() {
        let url = 'https://hackathon.anandchowdhary.com/primary_schools/?limit=20&offset=29';
        url += this.selectedRegion ? `&provincie=${this.selectedRegion}` : '';

        this.$axios.get(url).then(res => {
            this.schools = res.data.results.slice(0, 8);
        });
    }
  }
};
</script>
