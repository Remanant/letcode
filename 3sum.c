int find(int* arr, int size, int elem)
{
    for(int i = 0; i < size; i++)
    {
        if(arr[i]==elem)
        {
            return i;
        }
    }return -1;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* result = malloc(2* sizeof (int));
    *returnSize = 2* sizeof (int);
    for(int i = 0; i < numsSize; i++)
    {
        int elem = nums[i];
        int secelem = target - elem;
        int a=find(nums, numsSize, secelem);
    if(a == i)
    {
        continue;
    }
    if(a == -1)
    {
        continue;
    }
    result [0] = i;
    result [1] = a;
    }
    return result;
}
