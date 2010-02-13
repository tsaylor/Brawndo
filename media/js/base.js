$(document).ready(function(){
	$('.small_link').each(function(idx,a) {
		$(a).click(function(event){
			event.preventDefault();
			$.get(a.getAttribute('href'), '', function(data, textStatus, xhr) {
				alert(data); alert(textStatus); alert(xhr);
			});
		});
	});
});
