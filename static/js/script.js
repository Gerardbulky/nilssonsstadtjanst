$(document).ready(function(){
    $('#myCollapsible').collapse('show')
    $('#element').toast('show')
    
    $('.slider').slick({
        centerMode: true,
        centerPadding: '60px',
        slidesToShow: 3,
        dots: true,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '40px',
                    slidesToShow: 3,
                }
            },
            {
                breakpoint: 480,
                settings: {
                    arrows: false,
                    centerMode: true,
                    centerPadding: '40px',
                    slidesToShow: 1,
                }
            }
        ]
    });

})
