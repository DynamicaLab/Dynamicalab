/*
	
	By Edward Laurence

	Parse HTML file. Find HEX code of colors, e.g. "#F0F0F0", and add a small square after it of the same specified color.

*/

function small_square(color){
	color = color.slice(1, -1);
	// color = color.slice(1, );
	var str = " <div style=\"width:12px;height:12px;display: inline-block; border-radius:6px;background:"+color+";\"></div>"
	return str
}

window.onload = function () { 

	var html = $('html').html();
	var str = /<body.*?>([\s\S]*)<\/body>/.exec(html)[1];
	var regex = /(”|\')#([0-9A-F][0-9A-F])([0-9A-F][0-9A-F])([0-9A-F][0-9A-F])(”|\')/gi;

	var done = [];
	while ( (result = regex.exec(str)) ) {

	    var hexCode = result[0];
	    console.log(hexCode);
	    if (done.includes(hexCode)==false){
		    console.log(hexCode);

		    $("body").children().each(function () {
		    	var re = new RegExp(hexCode,"g");
			    $(this).html( $(this).html().replace(re, hexCode +small_square(hexCode)) );
			});
		    done.push(hexCode);
		}
	}

 }
