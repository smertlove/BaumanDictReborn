"use strict";


 $(window).scroll(function() {
      if ($(this).scrollTop()>300) {
        $('.back-to-top-btn').fadeIn(1000);
      }else {
        $('.back-to-top-btn').fadeOut(1000);
      }
});