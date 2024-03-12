/*
	please ensure cs50 library is installed.
	libcs50: https://github.com/cs50/libcs50/tree/main
*/
#include <stdio.h>
#include <cs50.h> 

int main(void)
{
	int pyramid_Height;
	int hash_Number = 2;
	int row_Index = 1; 
	
	//Getting height
	do
	{
		printf("Height: ");
		pyramid_Height = GetInt();
	}
	while(pyramid_Height < 0 || pyramid_Height > 23);
	
	int counter = 0;
	//Repeat until required height is reached
	while(counter < pyramid_Height)
	{
		//Printing spaces. 
		int spaces = pyramid_Height - row_Index;
		
		while(spaces > 0)
		{
			printf(" ");
			spaces--;
		}
		
		row_Index++;
		
		//Printing #s
		int i = 0;
		while( i < hash_Number)
		{
			printf("#");
			i++;
		}
		//Incrementing hashes needed to next row
		hash_Number++;
		printf("\n");
		
		//Incrementing counter. Moving closer to required height
		counter++;	
	}	
	
	
	
	return 0;
}
