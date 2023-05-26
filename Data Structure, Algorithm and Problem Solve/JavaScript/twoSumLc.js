var twoSum = function(nums, target) {
    len = nums.length;
    let outpt = []
    for (let i =0;i<len;i++)
    {
        for(let j=i+1;j<len;j++)
        {
            if(nums[i]+nums[j]==target)
            {
                outpt.push(i);
                outpt.push(j);
            }
        }
    }
    console.log(outpt);
    
};

let intpt = [3,2,4];
twoSum(intpt,6);
