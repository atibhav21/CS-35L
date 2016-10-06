#include <stdio.h>
#include <stdlib.h>
//#include <iostream>
//using namespace std;

int frobcmp(const char * a, const char* b)
{
  if(a == NULL || b == NULL)
    {
      fprintf(stderr, "Null Pointer Passed to Function\n");
      exit(1);
    }
  while(*a != ' ' && *b != ' ')
    {
      if(*a == *b)
	{
	  a++;
	  b++;
	}
      else if (((*a) ^ 42) < ((*b) ^ 42))
	{
	  return -1;
	}
      else
	return 1;
    }
  if( *a != ' ' && *b == ' ' )
    {
      return 1;
    }
  else if( *a == ' ' && *b != ' ')
    {
      return -1;
    }
  return 0;

}

int wrapperFunction(const void* a, const void* b)
{
  return frobcmp( *((const char**) a), *((char**)b));
}

void generateSortedOutput(char** begin, int numElements)
{
  int (*fp)(const void *, const void * );
  fp = wrapperFunction;
  qsort(begin, numElements, sizeof(char*) , fp);
}

int main(void)
{
  /*int x = frobcmp("*{_CIA\030\031 ", "*`_GZY\v ");
  printf("%d", x);
  x = frobcmp("*{_CIA\030\031 ", "*{_CIA\030\03130 ");
  printf("%d", x);*/
  unsigned int elementCount = 0;
  int currentChar;
  char* tempArray = (char*) malloc (16);
  int currentSize = 16;
  char* iterator = tempArray;
  int currentPosition = 0;
  while(1)
  {
    currentChar = fgetc(stdin);
    if(currentChar == EOF)
      {
	break;
      }
    *iterator = currentChar;
    currentPosition++;
    iterator++;
    if(currentChar == ' ')
      {
        elementCount++;
      }
    // find the maximum width of an element
    
    if(currentPosition >= currentSize)
      {
	//tempArray[currentPosition] = ' ';
	//currentPosition++;
    
	currentSize = currentSize * 2;
	char* ptr = (char*) realloc(tempArray, currentSize);
	if(ptr!= NULL)
	{
	  tempArray = ptr;
	  iterator = tempArray + currentPosition;
	}
	else
	  {
	  fprintf(stderr, "Error in assigning memeory");
	  exit(1);
	 }
	//tempArray = realloc(tempArray, currentSize);
    	//iterator = tempArray + temp;
      }
  }

  if(currentPosition == 0)
    {
      free(tempArray);
      exit(0);
    }
  
  if(currentChar != ' ' )
    {
      tempArray[currentPosition] = ' ';
      currentPosition++;
      elementCount++;
    }
  //printf(tempArray);

  size_t totalSpace = (elementCount * sizeof(char*));
  char** basePointer = (char**) malloc(totalSpace);
  int i;
  int spaces = 1;
  basePointer[0] = tempArray;
  for(i = 0; spaces < elementCount; i++)
    {
      if(tempArray[i] == ' ')
	{
	  basePointer[spaces] = &tempArray[i+1];
	  spaces++;
	}
    }

  
  //printf(basePointer);
  //free(tempArray);
  generateSortedOutput(basePointer, elementCount);

  int k;

  for(k = 0; k < elementCount; k++)
    {
      int j;
      for(j = 0; basePointer[k][j] != ' '; j++)
	{
	  putchar(basePointer[k][j]);
	}
      putchar(' ');
    }
  free(tempArray);
  free(basePointer);
}
