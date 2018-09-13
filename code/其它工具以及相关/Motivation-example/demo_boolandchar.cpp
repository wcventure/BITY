#include<stdio.h>

void func1(int t){
	
	bool a;

	switch (t){
		case 1:
			a = 10;
		case 2:
			a = false;
		case 3:
			a = 'A';
		default:
			break;
	}
	if (!a)
		printf ("%s",a);
}

void func2(int t){

	char a;

	switch (t){
		case 1:
			a = 10;
		case 2:
			a = false;
		case 3:
			a = 'A';
		default:
			break;
	}
	if (!a)
		printf ("%s",a);
}

void main(){

	func1(1);
	func2(1);
}

