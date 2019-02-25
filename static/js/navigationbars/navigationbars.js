$( document ).ready(function() {
    currentPageActive();
});

function currentPageActive() {
  // this function find the current path to add active class
  var path_sidebar = location.pathname;
  var path_navbar = "/"+location.pathname.split("/")[1]+"/"
   $('nav ul a').each(function() {
    if (this.pathname == path_sidebar) {
     $(this).addClass('active');
    }
    if (this.pathname == path_navbar) {
     $(this).addClass('active');
    }
   });
}
