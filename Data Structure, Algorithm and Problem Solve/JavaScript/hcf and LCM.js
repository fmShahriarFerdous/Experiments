function hcf(a,b)
{
    if (b==0)
        return a;
    else
        return hcf(b,a%b);

}

var hcf;
var a = 255;
var b = 135;
var lcm;
hcf=hcf(a,b);
lcm=(a*b)/hcf;
console.log("HCF:", hcf, "\n" + "LCM:",lcm);
