$('#select').selectize({
    create: true,
    optgroupOrder: ["Weddings", "Other Events"]
});

$('#product').typed({
    strings: ['\n', '\nCake Topper ', '\nTable Centerpieces ', '\nCufflinks '],
    contentType: 'text',
    typeSpeed: 120,
    backSpeed: 120,
    backDelay: 7000,
    showCursor: false,
    loop: true,
    preStringTyped: function(arrayPos) {
	var images = [
	    'url(../images/Hero_highres_full_width.jpg)',
	    'url(../images/Hero_Cake_Topper.png)',
	    'url(../images/Hero_Centerpiece.jpg)',
	    'url(../images/Hero_Cufflinks.jpg)',
	];
	$('.hero').css('background-image', images[arrayPos]);
	if (arrayPos > 0) {
	    $('.hero p').css('color', '#fff');
	    $('.hero h2').css('color', '#fff');
	} else {
	    $('.hero p').css('color', '#000');
	    $('.hero h2').css('color', '#000');
	}
    }
});

$('#occasion').typed({
    strings: ['\n', '\nYour Wedding', '\na Baby Shower', '\nYour Groomsmen'],
    contentType: 'text',
    typeSpeed: 120,
    backSpeed: 120,
    backDelay: 7000,
    showCursor: false,
    loop: true,
});

// Width of inspiration pictures should be relative to height for responsiveness
var currentWidth = $('.inspiration').width();
$('.inspiration').css({'height': currentWidth+'px'});

// Datepicker
rome(duedate, {time: false});

