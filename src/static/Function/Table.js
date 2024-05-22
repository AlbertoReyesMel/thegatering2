/*function searchTable() {
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
  }*/




  document.addEventListener("DOMContentLoaded", function(){

    fetch('/BE-A01/areas')
                .then(response => response.json())
                .then(data => {
                    const areaSelect = document.getElementById('area');
                    data.forEach(area => {
                        const option = document.createElement('option');
                        option.value = area.id_Area;
                        option.textContent = area.area_Name;
                        areaSelect.appendChild(option);
                    });
                })
                .catch(error => console.error('Error:', error));
    fetch('/BE-A01/notifications').then(response=> response.json()).then(data =>{
      const tableBody = document.getElementById('notifications-table').getElementsByTagName('tbody')[0];
      data.forEach(notification => {
        const row = document.createElement('tr');
        row.innerHTML = `
        <td'>${notification.id_Notification}</td>
        <td>${notification.area_Name}</td>
        <td>${notification.message}</td>
        <td>${notification.notification_Date}</td>
        <td><button class="btn btn-warning">Editar</button></td>
        <td><button class="btn btn-danger">Eliminar</button></td>
         `;
        tableBody.appendChild(row);
      });
      
    })
    .catch(error=> console.error('Error:', error))
    const notificationForm = document.getElementById('notificationForm');
    notificationForm.addEventListener('submit', function(event){
      event.preventDefault();

      const area = document.getElementById('area').value;
      const message = document.getElementById('message').value;

      fetch('/BE-A01/notifications', {
        method: 'POST',
        headers:{
          'Content-Type':'application/json'
        },
        body: JSON.stringify({
          area: area,
          message: message

        })
      })
      .then(response => response.json())
      .then(data => {
        $('#addNotificationModal').modal('hide');
        addNotificationToTable(data);
        
      })
      .catch(error=>console.error('Error:', error));
    });

    function addNotificationToTable(notification) {
      const tableBody = document.getElementById('notifications-table').getElementsByTagName('tbody')[0];
      const row = document.createElement('tr');
      row.innerHTML = `
          <td>${notification.id_Notification}</td>
          <td>${notification.area_Name}</td>
          <td>${notification.message}</td>
          <td>${notification.notification_Date}</td>
          <td><button class="btn btn-warning">Editar</button></td>
          <td><button class="btn btn-danger">Eliminar</button></td>
      `;
      tableBody.appendChild(row);
  }
  });