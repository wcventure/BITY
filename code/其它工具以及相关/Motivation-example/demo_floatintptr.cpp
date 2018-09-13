void func1(float* a){
	*a = 10.0 ;
}

void func2(int* a){
	*a = 10.0 ;
}

void func3(double* a){
	*a = 10.0 ;
}

int main(){

	float *x = new float;
	int *y = new int;
	double *z = new double;
	
	func1(x);
	func2(y);
	func3(z);

	return 0;
}

