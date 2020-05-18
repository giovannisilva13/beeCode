
function updateStock(event){
    
    const data = {};

    const id = event.id.split('-')[1];
    const key = event.id.split('-')[0];
    const value = event.value;

    data[key] = value;
    data["pk"] = id;

    $.ajax({
        url: "/alterar-estoque/",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(data),
        success: function(data){
            if (data.status == 200){
                window.location.reload();
            } else {
                alert(data.message);
            }
        },
        error: function(data){
            console.log(data);
        }
    });

}
