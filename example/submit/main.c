#include <stdio.h>

int main(int argc,char *argv[]) {
	int n;
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		printf("%d\n", i + 1);
	}
	
	return 0;
}