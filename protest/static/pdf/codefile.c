#include<stdio.h>
#include <stdlib.h>
#define M 3
struct node
{
	int n; /* n < M No. of keys in node will always less than order of B
tree */
	int keys[M-1]; /*array of keys*/
	struct node *p[M]; /* (n+1 pointers will be in use) */
}*root=NULL;

enum KeyStatus { Duplicate,SearchFailure,Success,InsertIt,LessKeys };
void insert(int key);
void display(struct node *root,int);
void search(int x);
enum KeyStatus ins(struct node *r, int x, int* y, struct node** u);
int searchPos(int x,int *key_arr, int n);

int main()
{
	int key,n,i,choice;
	printf("Creation of B tree for node %d\n",M);
	while(1)
	{
		printf("\n 1.Insert\n 2.Search\n 3.Display\n 4.Quit\n");
		printf("Enter your choice : ");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:
				printf("\n Enter no.of keys");
				scanf("%d",&n);
				printf("\n Enter the key values : ");
				for(i=0;i<n;i++)
				{
					scanf("%d",&key);
					insert(key);
				}
			break;
			case 2:
				printf("Enter the key value to search: ");
				scanf("%d",&key);
				search(key);
			break;
			case 3:
				printf("Btree is :\n");
				display(root,0);
			break;
			case 4:
				exit(1);
				default:
					printf("Wrong choice\n");
			break;
		}//End of switch
	}//End of while
	return 0;
}//End of main()
void insert(int key)
{
	struct node *newnode;
	int upKey;
	enum KeyStatus value;
	value = ins(root, key, &upKey, &newnode);
	if (value == Duplicate)
		printf("Key already available\n");
	if (value == InsertIt)
	{
		struct node *uproot = root;
		root=malloc(sizeof(struct node));
		root->n = 1;
		root->keys[0] = upKey;
		root->p[0] = uproot;
		root->p[1] = newnode;
	}/*End of if */
}/*End of insert()*/
enum KeyStatus ins(struct node *ptr, int key, int *upKey,struct node**newnode)
{
	struct node *newPtr, *lastPtr;
	int pos, i, n,splitPos, newKey, lastKey;
	enum KeyStatus value;
	if (ptr == NULL)
	{
		*newnode = NULL;
		*upKey = key;
		return InsertIt;
	}
	n = ptr->n;
	pos = searchPos(key, ptr->keys, n);
	if (pos < n && key == ptr->keys[pos])
		return Duplicate;
	value = ins(ptr->p[pos], key, &newKey, &newPtr);
	if (value != InsertIt)
		return value;
/*If keys in node is less than M-1 where M is order of B tree*/
	if (n < M - 1)
	{
		pos = searchPos(newKey, ptr->keys, n);
		
		/*Shifting the key and pointer right for inserting the new key*/
		for (i=n; i>pos; i--)
		{
			ptr->keys[i] = ptr->keys[i-1];
			ptr->p[i+1] = ptr->p[i];
		}
		
		
		/*Key is inserted at exact location*/
		ptr->keys[pos] = newKey;
		ptr->p[pos+1] = newPtr;
		++ptr->n; /*incrementing the number of keys in node*/
		return Success;
	}/*End of if */
		
	/*If keys in nodes are maximum and position of node to be inserted is
last*/
	if (pos == M - 1)
	{
		lastKey = newKey;
		lastPtr = newPtr;
	}
	else /*If keys in node are maximum and position of node to be inserted
is not last*/
	{
		lastKey = ptr->keys[M-2];
		lastPtr = ptr->p[M-1];
		for (i=M-2; i>pos; i--)
		{
			ptr->keys[i] = ptr->keys[i-1];
			ptr->p[i+1] = ptr->p[i];
		}
		ptr->keys[pos] = newKey;
		ptr->p[pos+1] = newPtr;
	}
	splitPos = (M - 1)/2;
	(*upKey) = ptr->keys[splitPos];
	(*newnode)=malloc(sizeof(struct node));/*Right node after split*/
	ptr->n = splitPos; /*No. of keys for left splitted node*/
	(*newnode)->n = M-1-splitPos;/*No. of keys for right splitted node*/
	
	for (i=0; i < (*newnode)->n; i++)
	{
		(*newnode)->p[i] = ptr->p[i + splitPos + 1];
		if(i < (*newnode)->n - 1)
			(*newnode)->keys[i] = ptr->keys[i + splitPos + 1];
		else
			(*newnode)->keys[i] = lastKey;
	}
	(*newnode)->p[(*newnode)->n] = lastPtr;
	return InsertIt;
}/*End of ins()*/
void display(struct node *ptr, int blanks)
{
	if (ptr)
	{
		int i;
		for(i=1;i<=blanks;i++)
			printf(" ");
		for (i=0; i < ptr->n; i++)
			printf("%d ",ptr->keys[i]);
			printf("\n");
		for (i=0; i <= ptr->n; i++)
			display(ptr->p[i], blanks+10);
	}/*End of if*/
}/*End of display()*/
void search(int key)
{
	int pos, i, n;
	struct node *ptr = root;
	printf("Search path:\n");
	while (ptr)
	{
			n = ptr->n;
			for (i=0; i < ptr->n; i++)
				printf(" %d",ptr->keys[i]);
				printf("\n");
				pos = searchPos(key, ptr->keys, n);
			
			if (pos < n && key == ptr->keys[pos])
			{
				printf("Key %d found in position %d of last dispalyed node\n",key,i);
				return;
			}
			ptr = ptr->p[pos];
	}
	printf("Key %d is not available\n",key);
}
/*End of search()*/
int searchPos(int key, int *key_arr, int n)
{
	int pos=0;
	while (pos < n && key > key_arr[pos])
		pos++;
	return pos;
}/*End of searchPos()*/
