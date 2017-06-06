var swiper = new Swiper('.swiper-container', {
    pagination: '.swiper-pagination',
    slidesPerView: 1,
    paginationClickable: true,
    spaceBetween: 30,
    autoplay: 3000,
    loop: true,
});

$(function(){
    $("a[name=navlist]").hide();
    $("#navfa").click(function() {
        if($(this).parent().find('a[name=navlist]').is(':hidden')){
            $(this).parent().find("a[name=navlist]").show();
            $(this).children().removeClass('fa-angle-up').addClass('fa-angle-down');
        }
        else{
            $(this).parent().find('a[name=navlist]').hide();
            $(this).children().removeClass('fa-angle-down').addClass('fa-angle-up');
        }
  });
})
