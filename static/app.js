var username = null;
var password = null;

// function login(){

// }

function adminLogin(){
    if(username === null){
		username = $("[name='ad-username']")[0].value;
		password = $("[name='ad-password']")[0].value;
	}
    // alert(username)
}