#include<stdio.h>

#define Max 10 //number of strings
#define Len 20 //length of @string

void deleteString(char arr[Max][Len], int *size, int index){
    for(int i=index;i<*size-1;i++) {
        for(int j=0;j<Len;j++){
            arr[i][j] = arr[i+1][j];
        }
    }
    (*size)--;
}

int main()
{
    int i;
    int b;
    int size = Max;

    printf("How many friends do you have?  ");
    scanf("%d",&i);

    char arr[Max][Len];
    printf("\nEnter their names:\n");
    for(int j=0;j<i;j++){
        printf("Friend %d: ",j+1);
        scanf("%s",&arr[j]);
    }
    printf("\nThese are all your friends\n");
    for(int j=0;j<i;j++){
        printf("Friend %d: %s\t\t", j+1, arr[j]);
    }
    printf("\n\nEnter the Friend number you dislike: ");
    scanf("%d", &b);

    deleteString(arr, &size, (b-1));
    printf("\nThese are your current friends:\n");
    for(int j=0;j<i;j++){
        printf("%s\t", arr[j]);

    }
    

    return 0;
}
