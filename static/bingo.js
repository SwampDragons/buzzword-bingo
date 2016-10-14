$(document).ready(function() {
  console.log('Loaded and ready for action.');
  $('.cell').on('click', function(e) {
    $(this).toggleClass('clicked');
    var click_list = new Array(25);
    var index = 0;
    $('.cell').each(function() {
      click_list[index] = $(this).hasClass('clicked');
      index++;
    });
    console.log(click_list);
  });
});
