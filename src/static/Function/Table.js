function searchTable() {
    var input, filter, table, tr, td, i;
  
    var input = document.getElementById("search");
    var filter = input.value.toUpperCase();
    var table = document.getElementById("table");
    var tr = table.getElementsByTagName("tr");
  
    for (var i = 1; i < tr.length; i++) {
      var tds = tr[i].getElementsByTagName("td");
      var firstCol = tds[0].textContent.toUpperCase();
      var secondCol = tds[1].textContent.toUpperCase();
      if (firstCol.indexOf(filter) > -1 || secondCol.indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
  
  function searchTableDevice(device) {
    var filter, table, tr, td, i;
  
    $("#deviceSelector").html(device);
  
    var filter = device.toUpperCase();
    var table = document.getElementById("table");
    var tr = table.getElementsByTagName("tr");
    if (device == "all") {
      $("#table tr").css("display", "");
      $("#deviceSelector").html("Devices");
    } else {
      searchTable();
      for (var i = 1; i < tr.length; i++) {
        var tds = tr[i].getElementsByTagName("td");
        var secondCol = tds[1].textContent.toUpperCase();
        if (secondCol.indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }