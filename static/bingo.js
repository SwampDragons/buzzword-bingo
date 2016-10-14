$(document).ready(function() {
  console.log('Loaded and ready for action.');
  $('.cell').on('click', function(e) {
    $(this).toggleClass('clicked');
    var clicked_list = new Array(25);
    var index = 0;
    $('.cell').each(function() {
      clicked_list[index] = $(this).hasClass('clicked');
      index++;
    });
    console.log(clicked_list);
    $.ajax({
      url: "/checkbingo",
      data: {list: JSON.stringify(clicked_list)},
      type: 'post',
      success: function(data) {
        alert(data);
      }
    });
  });
});
