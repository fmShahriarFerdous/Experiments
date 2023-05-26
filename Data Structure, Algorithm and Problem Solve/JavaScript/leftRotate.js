/* var arr=[1,2,3,4,5,6,7];
len=arr.length;
var i=0;
var j=2;

var newarr=[]

while (i<len)
{
    if (j<len)
      {
        newarr[i]=arr[j]
        
      } 
    else
   {
        newarr[i]=arr[j-len]
        
   }
    i+=1
    j+=1
}
arr=newarr;
console.log(arr);
*/

function rotateleft(arr,leng)
{
  var p = 0;
  var j = 2;
  var temp = [];
  for(let i=j; i<leng; i++)
    {
      temp[p]=arr[i];
      p += 1;
    }

  for(let i=0; i<j; i++)
    {
      temp[p]=arr[i];
      p += 1;
    }
    return temp;
}

ar = [1,2,3,4,5,6,7];
console.log(ar);
var leng = ar.length; 
ar = rotateleft(ar, leng);
console.log(ar);


/*function rotateleft(arr,len,d)
{
    var p=1;
    while(p<=d)
    {
        var temp = arr[0];
        for(let i=0;i<len-1;i++)
        {
            arr[i]=arr[i+1];
        }
        arr[len-1]=temp;
        p += 1;
    }
    document.getElementById("goo").innerHTML=arr;
    
}
var arr = [1,2,3,4,5,6,7];
var d=2;
console.log(arr);
var len = arr.length;
document.getElementById("goo").innerHTML=arr;*/
