   var myVar;

    function createloader() {
    document.getElementById("loader").style.display = "inherit";
      myVar = setTimeout(hideloader, 30000);
    }

    function hideloader() {
      document.getElementById("loader").style.display = "none";
    }