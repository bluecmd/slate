$(document).ready(function() {
	
	// Hide sub models
	$("h4").each(function() {
		var h4 = $( this );
		var table = h4.next();

		if (table.is('table')) {
			h4.addClass('collapsed');
			h4.css('text-decoration', 'underline');
			h4.css('cursor', 'pointer');
			table.addClass('hidden');

			h4.click(function() {
				if (h4.hasClass('collapsed')) {
					h4.removeClass('collapsed');
					table.removeClass('hidden');
				} else {
					h4.addClass('collapsed');
					table.addClass('hidden');
				}
			});
		}
	});
});