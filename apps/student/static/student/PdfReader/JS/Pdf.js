function onPdf(i) {

    document.getElementsByClassName("overlayPdf")[i].style.display = "block";
}

function BackButtonOff(i) {
    document.getElementsByClassName("overlayPdf")[i].style.display = "none";
}

function CheckButtonOff(i) {
	document.getElementsByClassName("overlayPdf")[i].style.display = "none";
}

function OffNextSubject(i) {
    document.getElementsByClassName("ButtonLocked")[i].disabled = true;
}


function Locking() {

	var i;
	alert('hola');
	/*for(i in document.getElementsByClassName("ButtonLocked").length ) {
		OffNextSubject(i);	
	}*/

}
