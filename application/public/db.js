var firebase;

$(function () {
	var $submit_btn = $('#submit_btn');
	var $close_btn = $('#close_btn');
	var $alert_close = $('#alert_close');

	const firebaseConfig = {
		apiKey: "AIzaSyB8u-emsXhNkff5DBMUrDLGLvi7nNUo2CU",
		authDomain: "autoapply-ee19b.firebaseapp.com",
		databaseURL: "https://autoapply-ee19b.firebaseio.com",
		projectId: "autoapply-ee19b",
		storageBucket: "autoapply-ee19b.appspot.com",
		messagingSenderId: "1080872531410",
		appId: "1:1080872531410:web:a5fe0087f44e71fb18440b"
	};
	firebase.initializeApp(firebaseConfig);
	var database = firebase.database().ref();
	var users = [];

	database.on('value', function (snapshot) {
		for (var i in snapshot.val()) {
			var tsmc_id = snapshot.val()[i].tsmc_id;
			users.push(tsmc_id);
		}
		// console.log(users);
	});

	function insert() {
		var date = new Date();
		var formattedDate = moment(date).format('MMMM Do YYYY, h:mm:ss a');
		var postData = {
			tsmc_id: $('#id_text').val(),
			create_date: formattedDate
		};
		database.push(postData);
		$('#successModal').modal('show');
	}

	$submit_btn.on('click', function () {
		var isExist = false;
		var error = false;
		var id_num = parseInt($('#id_text').val());
		if (!isNaN(id_num)){
			if (id_num < 50000 || id_num > 999999){
				error = true;
			}
		}
		else{
			error = true;
		}
		
		users.forEach(function(user){
			if (user == $('#id_text').val()){
				isExist = true;
			}
		});
		
		console.log(error);
		if(error){
			alert("輸入格式有誤");
		}
		else if(isExist){
			alert("此工號已申請過本服務");
		}
		else{
			insert();
		}
	});

	$close_btn.on('click', function(){
		$('#successModal').modal('toggle');
	});
	// $alert_close.on('click', function(){
	// 	$('#alert').alert('toggle');
	// });
});