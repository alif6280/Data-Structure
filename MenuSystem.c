#include<stdio.h>
#include<string.h>
#include<windows.h>

void inputString(char str[]);
void findLength(char str[]);
void subString(char str[]);
void compareString(char str[]);
void indexing(char str[]);
void concatenation(char str[]);
void exitProgram();

int main()
{
    int choice;
    char str[100];

    while(1)
    {
        printf("\n====MENU====\n");
        printf("1. Input a String\n");
        printf("2. Length\n");
        printf("3. Substring\n");
        printf("4. Compare Two String\n");
        printf("5. Indexing\n");
        printf("6. Concatenation\n");
        printf("7. Exit\n");
        printf("\nEnter your choice : ");
        scanf("%d",&choice);
        getchar();

        switch(choice)
        {
        case 1:
        {
            inputString(str);
            break;
        }
        case 2:
        {
            findLength(str);
            break;
        }
        case 3:
        {
            subString(str);
            break;
        }
        case 4:
        {
           compareString(str);
           break;
        }
        case 5:
        {
            indexing(str);
            break;
        }
        case 6:
        {
            concatenation(str);
            break;
        }
        case 7:
        {
            exitProgram();
            return 0;
        }
        default:
            {
                printf("\nInvalid Choice ! please try again.\n");
            }
        }
    }
}
void inputString(char str[])
{
    printf("\nEnter any string : ");
    gets(str);
}
void findLength(char str[])
{
    printf("The length of string is : %d\n",strlen(str));
}
void subString(char str[])
{
    int start,length,i;
    char sub[100];
    printf("\nEnter starting of substring : ");
    scanf("%d",&start);
    printf("Enter length of substring : ");
    scanf("%d",&length);

    for(i=0;i<length;i++)
    {
        sub[i]=str[start+i];
    }
    sub[i]='\0';
    printf("Substrings : %s\n",sub);
}
void compareString(char str[])
{
    char str2[100];
    printf("Enter other string : ");
    gets(str2);

    if(strcmp(str,str2)==0)
    {
        printf("---Strings are Equal---\n");
    }
    else
    {
        printf("---Strings are not Equal---\n");
    }
}
void indexing(char str[])
{
    int i;
    printf("The index : %d\n",strlen(str));
    for(i=0;i<strlen(str);i++)
    {
        printf("\nIndex %d -> %c\n",i,str[i]);
    }
}
void concatenation(char str[])
{
    char str2[100];
    printf("Enter other string : ");
    gets(str2);

    strcat(str," ");
    strcat(str,str2);
    printf("The Concatenation of string : %s\n",str);
}
void exitProgram()
{
    int i;
    printf("\nExiting Program");
    for(i=0;i<5;i++)
    {
        printf(".");
        fflush(stdout);
        Sleep(250);
    }
    printf("bye!!\n");
}
