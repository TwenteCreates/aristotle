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
                        display: false //this will remove all the x-axis grid lines
                    }]
                },
                legend: {
                    display: true,
                    position: 'bottom',
                },
                title: {
                    display: true,
                    fontSize: '18',
					text: 'Class points and questions solved - last 5 days'
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
