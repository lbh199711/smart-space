<template>
    <div class="header">
        <div class="header__content">
            <router-link to="/" class="header__link">[ Smart Space]</router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'footer-section'
    }
</script>

<style lang="scss">
    @import '@/assets/scss/_variables.scss';
    .header {
        color: $color-text;
        border-bottom: 1px solid $color-black;
        width: 100%;
    }

    .header__content {
        display: flex;
        justify-content: space-between;
        width: $global-width;
        max-width: $global-max-width;
        margin: auto;
        padding: 2rem $global-side-padding 1.75rem;

        @media screen and (max-width: $mobile-width) {
            padding: 2rem $global-side-padding-mobile 1.75rem;
            width: $global-width-mobile;
        }
    }

    .header__link {
        color: $color-text;
        text-decoration: none;

        &:hover {
            color: $color-link-highlight;
        }
    }
</style>
    
