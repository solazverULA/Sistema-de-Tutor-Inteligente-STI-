function onPdf(i) {
    document.getElementsByClassName("overlayPdf")[i - 1 ].style.display = "block";
}

function BackButtonOff(i) {
    document.getElementsByClassName("overlayPdf")[i - 1].style.display = "none";
}

function CheckButtonOff(i) {
	document.getElementsByClassName("overlayPdf")[i - 1].style.display = "none";
}

function OffNextSubject(i) {
    document.getElementsByClassName("ButtonLocked")[i - 1].disabled = true;
}


function Locking() {

	var i;
	alert('hola');
	/*for(i in document.getElementsByClassName("ButtonLocked").length ) {
		OffNextSubject(i);	
	}*/

}
