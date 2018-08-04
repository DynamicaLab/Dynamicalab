/*
	
	By Edward Laurence

	Parse HTML file. Find HEX code of colors, e.g. "#F0F0F0", and add a small square after it of the same specified color.

*/


var str = $('html').html();

var regex = /#([0-9A-F][0-9A-F])([0-9A-F][0-9A-F])([0-9A-F][0-9A-F])/gi  = [];

while ( (result = regex.exec(str)) ) {
    console.log(result);
}