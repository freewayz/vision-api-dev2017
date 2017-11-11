var vm = new Vue({
    el: '#app',
    template: '#appTemplate',
    data() {
        return {
            appName: 'Devfest 2017 Image Mind'
        }
    },

    mounted() {
        console.log('Vue mounted ', this.appName);
    }
})