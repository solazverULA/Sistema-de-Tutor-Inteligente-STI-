function onPdf(i,a) {
    document.getElementsByClassName("overlayPdf")[i - 1 ].style.display = "block";
	console.log(a);
}

function BackButtonOff(i) {
    document.getElementsByClassName("overlayPdf")[i - 1].style.display = "none";
}

function CheckButtonOff(i) {
	document.getElementsByClassName("overlayPdf")[i - 1].style.display = "none";
	document.getElementsByClassName("unlock")[i].disabled=false;
}



