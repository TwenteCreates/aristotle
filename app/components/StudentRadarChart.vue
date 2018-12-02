<template>
    <main>
        <radar-chart style="height: 400px" :chart-data="chartData" :options="options"/>
    </main>
</template>


<script>
  import RadarChart from '@/components/charts/RadarChart.js'

  export default {
    components: {
        RadarChart
    },
    data () {
        return {
            options: {
                responsive: true,
                maintainAspectRatio: false,
				scale: {
					ticks: {
						beginAtZero: true
					}
                },
                legend: {
					position: 'bottom',
				},
				title: {
                    display: true,
                    fontSize: '20',
					text: 'Student skills distribution'
				},
				animation: {
					animateScale: true,
					animateRotate: true
                },
			}
        }
    },
    props: {
        chartData: Object
    }
  }
</script>
