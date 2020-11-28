var num = [1, 0, 3, 8, 10];
var sum = 0;
num.forEach(function(elem, index, arr)
{
	arr[index] = elem * elem;
	sum += arr[index]
});

alert(sum)