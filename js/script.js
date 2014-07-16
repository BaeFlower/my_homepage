$(document).ready(function(){
	/* */
	activeIconOn();
	
	/*
	var t = document.querySelecctor("#templateTest");
	t.content.querySelecctor("img").src = "./img/giraffe.jpg";
	var clone = document.importNode(t.content, true);
	document.body.appendChild(clone);
	*/

	var contentsDiv = document.querySelector("#contents");
	var t = document.querySelector("#template0");

	//t.content.querySelector("img").src="./img/giraffe.jpg";

	var clone = document.importNode(t.content, true);
	contentsDiv.appendChild(clone);

	$(".iconImg.iconAnc").click(function(){
	
		var $iconImgs = $(".iconImg:not(.iconAnc)");

		for (var i=0; i<$iconImgs.length ; i++){
			var $tmp = $iconImgs[i];
			
			if ($($tmp).hasClass("activeIcon")) {
				$($tmp).toggleClass("activeIcon");
			}
		}

		var $iconId = $(this).attr("id");
		var iconNum = $iconId.split("_")[1];

		var templateId = "#template" + iconNum;

		t = document.querySelector(templateId);
		clone = document.importNode(t.content, true);

		$("#contents").empty();
		contentsDiv.appendChild(clone);

		//activeIcon 변경 - 현재 작동 안함
		var iconLi = "#iconLi_" + iconNum;
		$(iconLi).addClass("activeIcon");

		activeIconOn();
	});
});

function activeIconOn(){
	/*
	$(".iconImg:not(.activeIcon)").hover(function(){
		$(this).children(':nth-child(1)').children(':nth-child(1), :nth-child(2)').css("color","#778488");
  		}, function(){
  		$(this).children(':nth-child(1)').children(':nth-child(1), :nth-child(2)').css("color","#c2c7c9");
  		}
	);	
	

	$(document).on("hover", ".iconImg:not(.activeIcon)", function(){
		$(this).children(':nth-child(1)').children(':nth-child(1), :nth-child(2)').css("color","#778488");
  		}, function(){
  		$(this).children(':nth-child(1)').children(':nth-child(1), :nth-child(2)').css("color","#c2c7c9");
  		}
  	);
*/
	

	//$(".activeIcon").children(":nth-child(2), :nth-child(3)").css("color", "#2990ea");
}

function addToDoList(){
	console.log("addToDoList");
	var raw_tags = "<ul class='toDoListUl'><li><input type='text' class='form-control fc-input' id='firstLi' placeholder='Type your to do list' readonly /></li>";

	for (var i=0; i<5; i++){
		raw_tags += "<li><input type='text' class='form-control fc-input' /></li>"
	}	

	//$("#btnAddToDoList").click(function(){
		var $ul_toDo =$(raw_tags);
		$(".listPart").append($ul_toDo);
	//});
}

function checkboxCheck(){
	/*
	:checkbox').click(function() {
    	var $this = $(this);
    	// $this will contain a reference to the checkbox   
    	if ($this.is(':checked')) {

    		console.log("checkboxCheck");
	*/

    	$(".chkList").click(function(){
    		var $this = $(this);
    	});
}