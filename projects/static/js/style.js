window.onload = $(function(){
    $('.hamburger').click(function(){
      $('.hamburger').toggleClass('active');
      $('.inner').toggleClass('open');
      $(this).addClass("current");
    }); 
  });