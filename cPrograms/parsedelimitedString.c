#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int ac, char* av[])
{
	int size = strlen(av[1]);
	char* strbuf = (char*) malloc(size+1);
	if(!strcpy(strbuf, av[1]))
	{
		printf("Failed to copy \n");
	}
//	printf("original string is %s\n", strbuf);

	char* tmpbuf = (char*) malloc(sizeof(strbuf));
	int len = strlen(strbuf);
	strncpy(tmpbuf, strbuf, len);
	tmpbuf[len] = '\0';
//	printf("tmp string is %s\n", tmpbuf);

	char* tmp = tmpbuf;
	char* tmp1 = NULL;
	char word[124] = {'\0'};
//	tmp1 = strchr(tmp, ' ');
//	*tmp = '\0';
//	char *tmp1 = NULL;	
//	printf("tmpbuf = %s\n", tmpbuf);
	while((tmp1 = strchr(tmp, ' ')) != NULL)
	{
		*tmp1 = '\0';
		strcpy(word, tmp);
		printf("word = %s\n", word);
		//printf("tmp = %s\n", tmp + 1);
		//printf("%s\n", tmp1+1);
		tmp = tmp1 + 1;
		//tmp1 = strchr(tmp+1,' ');		
	}
	printf("tmp1 = %s\n", tmp);

	return 0;
}
