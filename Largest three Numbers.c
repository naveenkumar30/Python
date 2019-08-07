#include <stdio.h>

int main() {
	int n;
	scanf("%d",&n);
	int a,b,c;
	
	for(int i=0;i<n;i++)
	{
	    scanf("%d %d %d",&a,&b,&c);
	    if(a>b && a>c)
	    printf("Largest of %d, %d, %d is %d\n",a,b,c,a);
	    else if(b>c)
	    printf("Largest of %d, %d, %d is %d\n",a,b,c,b);
	    else
	    printf("Largest of %d, %d, %d is %d\n",a,b,c,c);
	}
	return 0;
}
