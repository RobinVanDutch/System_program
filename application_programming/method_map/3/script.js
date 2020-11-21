let icantstop = ['банжур','Hello', 'привет', 'земля', '!??!', 'naziwin'];

result = icantstop.map(function(elem) {
	return elem.split('').reverse().join('')
});

console.log(result);