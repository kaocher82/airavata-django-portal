import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import GroupCreate from './groups_components/GroupCreate.vue'
// This is imported globally on the website so no need to include it again in this view
// import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Autocomplete from 'v-autocomplete'

Vue.use(BootstrapVue);
Vue.use(Autocomplete);

new Vue({
  el: "#create-group",
  template: '<group-create></group-create>',
  components: {
      GroupCreate
  }
})
