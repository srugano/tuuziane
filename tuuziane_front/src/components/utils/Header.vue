<template>
  <tuuziane-nav>

    <nav :class="isScrolled ? 'scrolled' : 'not-scrolled'" class="shadow py-3">
    <div class="container">
      <div class="row align-items-center">
        <!-- Logo Column -->
        <div class="col-6 col-md-2 text-center">
          <b v-if="isScrolled" 
            >
           TUUZIANE</b>
          <b v-if="!isScrolled"
            >TUUZIANE</b>
        </div>
      


        <!-- Navigation Links (Hidden on Mobile) -->
        <div class="col-auto d-none d-md-block">
            <RouterLink to="/">HOME</RouterLink>
        </div>
        <div class="col-auto d-none d-md-block">
            <RouterLink to="#services">SERVICE</RouterLink>
        </div>
        <div class="col-auto d-none d-md-block">
            <RouterLink to="#contact">CONTACT</RouterLink>
        </div>
        <div class="col-auto d-none d-md-block">
            <RouterLink to="#about">ABOUT</RouterLink>
        </div>
      </div>
    </div>
    </nav>

    </tuuziane-nav>



</template>

<script>


export default {
  data() {
    return {
      slidesPerView: 4,

      isScrolled: false,

      
      activeImageIndex: 0, // Start with the first image

      currentYear: new Date().getFullYear(),
      selected: false,
      option: null,
      currentIndex: 0,
      service: null,
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
    this.startImageRotation()
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
 
    nextSlide() {
      this.currentIndex = (this.currentIndex + 1) % this.items.length
    },
    prevSlide() {
      this.currentIndex =
        (this.currentIndex - 1 + this.items.length) % this.items.length
    },
    
    handleScroll() {
      this.isScrolled = window.scrollY > 0
    },
  },
}
</script>