<template>
  <div class="home-page">
    <MainSection username=""  />
    <!-- <Projects />
    <Experience /> -->
  </div>
</template>

<script>
import MainSection from '@/components/MainSection.vue'
// import Projects from '@/components/section/Projects.vue'
// import Experience from '@/components/section/Experience.vue'

export default {
  name: 'HomePage',
  components: {
    MainSection,
  },
  data () {
    return {
      banner_text: "Welcome to the place where I dump all the cool stuff I have been working on!"
    }
  }
}
</script>
