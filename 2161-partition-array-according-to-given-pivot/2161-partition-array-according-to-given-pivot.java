class Solution {
    public int[] pivotArray(int[] nums, int pivot) {
        int[] arr = new int[nums.length];
        int k =0;
        for(int a : nums){
            if(a < pivot)
            arr[k++] = a;
        }

        for(int a : nums){
            if(a == pivot)
            arr[k++] = a;
        }

        for(int a : nums){
            if(a > pivot)
            arr[k++] = a;
        }

        return arr;
    }
}