<template>
    <main>
        Student: {{studentId}} from the class {{classId}}
    </main>
</template>

<style scoped></style>


<script>
export default {
  data () {
    return {
        classId: null,
        studentId: null,
    };
  },
  mounted() {
    this.classId = this.$route.params.classId;
    this.studentId = this.$route.params.studentId;
  }
};
</script>
