<template>
    <main>
        <bar-chart style="max-height: 600px" :chart-data="chartData" :options="options"/>
    </main>
</template>


<script>
  import BarChart from '@/components/charts/BarChart.js'

  export default {
    components: {
        BarChart
    },
    data () {
        return {
			options: {
                responsive: true,
                maintainAspectRatio: false,
				legend: {
					position: 'bottom',
				},
				title: {
                    display: true,
                    fontSize: '20',
					text: 'Average Cito Scores By Starting Year'
				},
				animation: {
					animateScale: true,
					animateRotate: true
                },
                scales: {
                    xAxes: [{
                        stacked: true,
                    }],
                    yAxes: [{
                        stacked: true
                    }]
                }
            }
        }
    },
    props: {
        chartData: Object
    }
  }
</script>
