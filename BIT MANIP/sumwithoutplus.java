class Solution {
    public int getSum(int a, int b) {
        while(b!=0){
            int temp = (a&b) << 1; //shift left as carries go to left, 1,1 spotted then it adds the carry latter
            a = a ^ b;   //XOR is like half addition without carry which will be taken care in the following line: 
            b = temp;  //also b will run out so return a 
        }
        return a;
    }
}
