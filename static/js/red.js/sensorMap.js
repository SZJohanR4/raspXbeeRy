const app = new Vue({
    el: "#cauces_list_tbl",
    data: {
      response_data: [],
    },
    methods: {},
    mounted() {
      fetch("sensor_inf_map/")
        .then(response => response.json())
        .then((data) => {
          this.response_data = data;
          console.log(this.response_data.causes);
        })
    },
});
