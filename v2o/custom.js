$(document).ready(function(){
    $('#categories .panel').hover(function(){
        $(this).find('.panel-front').hide();
        $(this).find('.panel-back').fadeIn();
    }, function(){
        $(this).find('.panel-back').hide();
        $(this).find('.panel-front').fadeIn();
    });
});

$(window).scroll(function(){
    if ($(document).scrollTop() > 50) {
        $('#main-nav').addClass('shrink');
    } else {
        $('#main-nav').removeClass('shrink');
    }
});
