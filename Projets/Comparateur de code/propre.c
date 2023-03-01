#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int factorielle_iterative(int n){
    int i,res=1;
    for(i=2;i<=n;i++){
        res=res*i;
    }
    return res;
}
int main(){
clock_t deb = clock();
for(int i=0;i<=1000000;i++){
factorielle_iterative(40);
}
clock_t fin=clock()-deb;
FILE * tmp = NULL;
 tmp = fopen("tmp.txt","w");

fprintf(tmp,"%ld",fin);
fclose(tmp);
return fin;
}

