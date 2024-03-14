#include <stdio.h>
#include <string.h>

int main()
{
    printf("Hello World 3\n");
	printf("Job ID (used to build): %d\n",JOB_ID_BUILD);
	
	FILE * pFile;
	char fileName[100];
	sprintf(fileName, "hello_world_3_%d.txt",JOB_ID_BUILD);
    pFile = fopen(fileName, "w");
	if (NULL != pFile)
	{
		fwrite(fileName, strlen(fileName), 1, pFile);
		fclose(pFile);
	}
	
    return 0;
}