<template>
    <div v-if="!classes"><h2>Loading</h2></div>
    <div v-else class="columns is-mobile">
        <div v-for="classItem in classes" :key="classItem.id" class="column is-4">
            <div class="box" @click="$router.push(`/teacher/classes/${classItem.id}`)">
                <span>{{classItem.name}}</span>
            </div>
        </div>
    </div>
</template>


<script>
  import LineChart from '@/components/charts/LineChart.js'

  export default {
    components: {
        LineChart
    },
    props: {
        classes: Array,
    },
    data () {
        return {}
    }
  }
</script>
