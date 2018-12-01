<template>
    <main>
        Class: {{classId}}
    </main>
</template>

<style scoped></style>


<script>
export default {
  data () {
    return {
        classId: null,
    };
  },
  mounted() {
    this.classId = this.$route.params._classId
  }
};
</script>
