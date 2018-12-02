<template>
    <line-chart style="max-height: 500px" :chart-data="chartData" :options="options"></line-chart>
</template>


<script>
  import LineChart from '@/components/charts/LineChart.js'

  export default {
    components: {
        LineChart
    },
    data () {
        return {
            options: {
                scales:{
                xAxes: [{
                        display: true
                    }]
                },
                legend: {
                    display: true,
                    position: 'bottom',
                },
                title: {
                    display: true,
                    fontSize: '18',
					text: 'Agregated points and questions - last 5 days'
				},
                responsive: true,
                maintainAspectRatio: false,
            }
        }
    },
    props: {
        chartData: Object
    }
  }
</script>
