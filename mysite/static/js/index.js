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


function plugin(){
	function homeUp(){
		$('#icon-down').on('click', function(){
			var height = $('.home').height();
			$('html,body').scrollTop(height)
		})
	}
	function tab(){
		$('.nav-li').on('click', function(){
			var index = $('.nav-li').index(this);
			$('.nav-li').eq(index).addClass('active').siblings().removeClass('active');
			$('.function-list').eq(index).css('display', 'block').siblings().css('display', 'none');
		})
	}

	function showImgName(){
		$('#form-select').on('change', function(){
			var html = '';
			for(var i = 0; i < this.files.length; i++){
				html = html + this.files[i].name + '  '
			}
			console.log(html);
			$('.select-area').html(html)
		})
	}
	
	function mask(){
		$('.mask-btn').on('click', function(){
			
			$('#mask-plugin').css('display', 'block');
		})
	}
	tab();
	showImgName();
	mask();
	homeUp();
}

function init(){
	select();
	imgUpload();
	plugin();
}
$(document).ready(function(){
	init();
})