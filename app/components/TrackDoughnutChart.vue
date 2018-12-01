<template>
    <main>
        <doughnut-chart style="height: 500px" :chart-data="chartData" :options="options"/>
    </main>
</template>


<script>
  import DoughnutChart from '@/components/charts/DoughnutChart.js'

  export default {
    components: {
        DoughnutChart
    },
    data () {
        return {
			options: {
				responsive: true,
				legend: {
					position: 'bottom',
				},
				title: {
                    display: true,
                    fontSize: '20',
					text: 'Study track 9th grade'
				},
				animation: {
					animateScale: true,
					animateRotate: true
                },
                circumference: Math.PI,
				rotation: -Math.PI
            }
        }
    },
    props: {
        chartData: Object
    }
  }
</script>
