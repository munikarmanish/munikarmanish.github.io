$(document).ready(function(){
  $('#categories .panel').hover(function(){
    $(this).find('.panel-body').hide();
    $(this).find('.panel-back').show();
  }, function(){
    $(this).find('.panel-body').show();
    $(this).find('.panel-back').hide();
  });
});

$(window).scroll(function(){
  if ($(document).scrollTop() > 50) {
    $('#main-nav').addClass('shrink');
  } else {
    $('#main-nav').removeClass('shrink');
  }
});
