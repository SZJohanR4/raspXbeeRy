const app = new Vue({
    el: "#nodes_list_tbl",
    data: {
      response_data: [],
    },
    methods: {},
    mounted() {
      fetch("get_sensor_inf/")
        .then(response => response.json())
        .then((data) => {
          this.response_data = data;
        })
    },
});
