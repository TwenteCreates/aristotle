<template>
    <div class="map-container">
        <div id="nl-map" class="jvmap-smart"></div>
    </div>
</template>

<style lang="scss">
.jvmap-smart{
    width: 100%;
    height: 100%;
}

.jvectormap-container {
    width: 90%;
    height: 90%;
}

@media only screen and (min-width: 576px) {
    .map-container{
        height: 250px;
    }
}
@media only screen and (min-width: 768px) {
    .map-container{
        height: 350px;
    }
}
@media only screen and (min-width: 992px) {
    .map-container{
        height: 400px;
    }
}
@media only screen and (min-width: 1200px) {
    .map-container{
        height: 500px;
    }
}
</style>


<script>
    window.jQuery = require('jquery');
    require('jvectormap');
    require('./nl-mill.js');
    import $ from 'jquery'

    export default {
        mounted() {
            this.initMap();
        },
        methods: {
            initMap() {
                const that = this;
                const nlMap = $('#nl-map');
                nlMap.empty();
                nlMap.vectorMap({
                    map: 'nl_mill',
                    backgroundColor: "transparent",
                    regionsSelectable: true,
                    regionsSelectableOne: true,
                    zoomOnScroll: false,
                    zoomButtons: false,
                    regionStyle: {
                        initial: {
                            fill: '#209cee',
                        },
                        selected: {
                            fill: '#005ea5'
                        },
                    },
                    onRegionClick: function(e, code) {
                        that.emitChange(code);
                    }
                });
            },
            emitChange(code) {
                this.$emit('regionChange', code);
            }
        },
    }
</script>
