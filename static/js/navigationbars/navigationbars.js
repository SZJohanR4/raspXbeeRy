$( document ).ready(function() {
    currentPageActive();
});

function currentPageActive() {
  // this function find the current path to add active class
  var path_sidebar = location.pathname;
  var path_navbar = "/"+location.pathname.split("/")[1]+"/"
  navbar_element = document.getElementsByName(path_navbar)[0];
  if(navbar_element != undefined){
    navbar_element.classList.add("active");
  }
   $('nav ul a').each(function() {
    if (this.pathname == path_sidebar) {
     $(this).addClass('active');
    }
   });
}
