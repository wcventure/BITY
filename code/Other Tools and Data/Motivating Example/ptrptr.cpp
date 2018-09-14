#include<stdio.h>

void print(char **pp)
{
	printf("%s",**pp);
}

void main(){
	char k,*p,**pp;
	
	k='a';
	p=&k;
	pp=&p;

	print(pp);
}