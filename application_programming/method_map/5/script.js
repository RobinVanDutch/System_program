let arr = [234, 2532, 123, 456, 127809841];

let ok = arr.map(function(elem, index) {
	return elem * index;
});

console.log(ok);