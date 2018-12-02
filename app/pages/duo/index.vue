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
            <div class="columns">
                <div class="column is-1">
                    <span class="icon is-large is-pulled-right has-text-info map-icon">
                        <i class="fas fa-map-marked-alt"></i>
                    </span>
                </div>
                <div class="column is-3">
                    <b-field>
                        <b-select
                            extended
                            placeholder="Region"
                            size="is-medium"
                            v-model="selectedRegion"
                            >
                            <option value="">Region</option>
                            <option v-for="region in regions" :key="region" >{{region}}</option>
                        </b-select>
                    </b-field>

                </div>
            </div>
        </section>

        <section class="container map-container">
            <netherlands-map @regionChange="onRegionChange"/>
        </section>

        <section class="container schools-container">
            <h1 class="title">Educational institutions <span v-if="selectedRegion">in {{selectedRegion}}</span></h1>
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
.map-icon {
    font-size: 26px;
    line-height: 26px;
}
</style>


<script>
import firestore from '@/services/firestore';
import SchoolsTiles from '@/components/SchoolsTiles';
import NetherlandsMap from '@/components/NetherlandsMap';

export default {
  layout: 'duo',
  components: {
      SchoolsTiles,
      NetherlandsMap,
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
        regionsMap: {
            OV:	'Overijssel',
            FR:	'Friesland',
            UT:	'Utrecht',
            GE:	'Gelderland',
            FL:	'Flevoland',
            NH:	'Noord-Holland',
            ZE:	'Zeeland',
            ZH:	'Zuid-Holland',
            GR:	'Groningen',
            DR:	'Drenthe',
            NB:	'Noord-Brabant',
            LI:	'Limburg',
        },
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
    onRegionChange(region) {
        if (region) {
            const regionCode = region.split('-')[1];
            if (regionCode) {
                this.selectedRegion = this.regionsMap[regionCode];
            }
        }
    },
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
