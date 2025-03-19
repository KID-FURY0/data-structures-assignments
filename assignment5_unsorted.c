#include<stdio.h>

void merge (int a[],int m, int b[], int n, int r[]);

int main()
{
    int a[] = {2,9,5,7};
    int b[] = {1,6,3,8};
    int r[8];

    printf("Array 1\n");
    for (int j=0;j<4;j++)
    {
        printf("%d\t",a[j]);
    }

    printf("\nArray 2\n");
    for(int k=0;k<4;k++)
    {
        printf("%d\t",b[k]);
    }

    printf("\nUnsorted Merged array\n");
    merge(a,4,b,4,r);
    for(int i=0;i<8;i++)
    {
        printf("%d\t",r[i]);
    }

    return 0;
}

void merge (int a[], int m, int b[], int n, int r[])
{
    int i=0,j=0,k=0;
    while(i<m)
    {
        r[k]=a[i];
        k++;
        i++;
    }

    while(j<n)
    {
        r[k]=b[j];
        k++;
        j++;
    }
}