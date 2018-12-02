<template>
    <div v-if="!classes"><h2>Loading</h2></div>
    <div v-else class="columns is-mobile">
        <div v-for="classItem in classes" :key="classItem.id" class="column is-3">
            <div class="box" @click="$router.push(`/teacher/classes/${classItem.id}`)">
                <h1>{{classItem.name}}</h1>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    props: {
        classes: Array,
    },
    data () {
        return {}
    }
  }
</script>
