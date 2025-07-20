$(document).ready(function(){
    var form = $('#form_buying');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var pro_name = submit_btn.data("name");
        console.log(pro_name);

        $('.basket-items ul').append('<li>'+pro_name+','+nmb+'wt.    ' + '<a class = "delete-item" href ="">  x</a>'+'</li>');
    });

    function  shovingBasket(){
        $('.basket-items').removeClass('hidden');
    };

    $('.basket-container').on('click',function(e){
        e.preventDefault();
        shovingBasket();
    });

    $('.basket-container').mouseover(function(){
        shovingBasket();
    });


    // $('.basket-container').mouseout(function(){
    //     shovingBasket();
    // });

    $(document).on('click','.delete-item', function(){
        $(this).closest('li').remove();
    });
});