/* Funzione del paragrafo a comparsa */
function openTab(tabName) {
    var i, x;
    x = document.getElementsByClassName("containerTab");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    document.getElementById(tabName).style.display = "block";
  }

/* Script Javascript per il Navbar Responsive */
function myFunction() {
  var x = document.getElementById("myNavigationBar");
      if (x.className === "navigationbar") {
         x.className += " responsive";
   } else {
         x.className = "navigationbar";
         }
  }

/* Funzione del paragrafo a comparsa Responsive */
function openTabRe(tabNameRe) {
  var i, x;
    x = document.getElementsByClassName("containerTab");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    document.getElementById(tabNameRe).style.display = "block";
  }
