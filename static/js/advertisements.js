$(document).ready(function(){
    function create_card(Advertisement) {
        if(Advertisement.fields.ad_type == "FARMLAND"){
            return `
        <div class="col">
            <div class="card" style="width: 18rem;">
                <img class="card-img-top" src="https://imageio.forbes.com/specials-images/imageserve/62be10f32ce37625d88bca9b/Tractor-spraying-pesticides-on-soybean-field--with-sprayer-at-spring/960x0.jpg?format=jpg&width=960" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">${Advertisement.fields.title}</h5>
                    <p class="card-text">${Advertisement.fields.description}</p>
                </div>
                <div class="card-footer">
                    <p class="card-text">By : ${Advertisement.fields.username}</p>
                </div>
            </div>
        </div>
        `
        }
        else{
            return `
            <div class="col">
                <div class="card" style="width: 18rem;">
                    <img class="card-img-top" src="https://oxfarm.co.ke/wp-content/uploads/2018/10/Fresh-produce.jpg" alt="Card image cap">
                    <div class="card-body">
                        <h5 class="card-title">${Advertisement.fields.title}</h5>
                        <p class="card-text">${Advertisement.fields.description}</p>
                    </div>
                    <div class="card-footer">
                        <p class="card-text">By : ${Advertisement.fields.username} </p>
                    </div>
                </div>
            </div>
        `
        }
    };

    function Add_Advertisement() {
        $.get("/advertisement/json", function(data) {
            $.each(data, function(i, value) {
                $("#cardrow").append(create_card(value));
            });
        })
    };
    
    Add_Advertisement();
});
