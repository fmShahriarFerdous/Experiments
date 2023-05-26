var n=12
var num=21
var sum=0

while(num != 0)
{
    var rem = num%10;
    num = parseInt(num/10);
    sum = sum*10 + rem;
}
console.log(sum);