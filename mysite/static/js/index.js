function select(){
	var selectBtn = $('#select-btn');
	selectBtn.on('click', function(){
		$('#form-select').click();
	})
}	

function imgUpload(){
	var uploadBtn = $('#upload-btn');
	uploadBtn.on('click', function(){
		$('#form-upload').click();
	})
}

function init(){
	select();
	imgUpload();
}
$(document).ready(function(){
	init();
})