#include <stdbool.h>
bool isPalindrome(int x) 
{
    int rev = 0;
    if(x<0){
        return false;
    }
    //rev = x%10;
   for(int i = x; i > 0; i = i/10)
   {
    int r = i%10;
   rev = rev*10 + r;
   
}
if(rev - x == 0){
    return true;
}else{
    return false;
}
}

int main(){
    bool d = isPalindrome(1);
    printf("%d\n", d);
}