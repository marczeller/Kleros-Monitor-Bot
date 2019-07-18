
(function ($) {
	$(".datetime-string").each(function() {
		let datetime = $(this).html();
		let dot_marker_index = datetime.indexOf('.');
		if (dot_marker_index >= 0) $(this).html(datetime.substring(0, dot_marker_index));
	});
})(jQuery);