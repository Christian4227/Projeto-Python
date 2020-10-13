#include <stdio.h>


int repetidos(int v[], int n){
	for (int i=0; i<n; i++){
		for (int j=1; j<n; j++){
			if (v[i] == v[j]){ 
				return 1;}
		}
		return 0; 
	}
}

int main (void){
	int a[3] = {0, 1, 2};
	int b[3] = {0, 0 , 1};
	printf("%d", repetidos(a, 3));
	printf("%d", repetidos(b, 3));
	return 0;
}

