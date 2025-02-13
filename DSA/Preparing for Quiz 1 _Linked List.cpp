/*
There is a exam tomorrow and i am working on it 

Learning about type default
*/

/*
Write a function allLessThan(link h, int value) that checks if all the 
values in the linked list are less than a given value. The function should 
return 1 if all values are less than the given value, and 0 otherwise.
*/

int allLessThan(link h, int value) {
    link t=h;
    while(t!=0){
        if(t->item>value) return 0; // change to >=
        t=t->next;
    }
    return 1;
}

// However, to ensure that all items are strictly less than the given value, 
// you should also consider the case where an item is equal to the given value

/*Write a function findMiddle(link h) that finds and 
returns the middle element of a singly linked list. 
If the list has an even number of elements, return the second of the two middle elements.
You should not use any extra space (i.e., no arrays or additional data structures)
*/

int findMiddle(link h){
    link t,t1,t2=h;
    int count,middle;
    while(t!=0){
        count++;
        t=t->next;
    }
    
    if (count%2==1){
        middle=(count++)/2;// Not necessary,as this automaticlly takes 1 
        for(int i=1;i<middle;i++){
            t1=t1->next;
        }
        return t1->item;
    }else{
        middle=count/2;
        for(int i=1;i<=middle;i++){
            t2=t2->next;
        }
        return t2->item

    }

}

/*
Learning: intialise count to zero
handling empty linked list
Smart way is two different traversal speed 
*/

/*
Search an element 
*/

int searchone(link h,int a){

    link t=h;
    while (t!=0){
        if(t->item==a) return 1;
        t=t->next;
    }
    return 0;
}

/*
find the node value same as s and delete the node
asume h is not empty 
all values in linkedlist are distinct
link deleteone(link h,int s)
if linkedlist becomes empty , then function returns null,else
returns same

this is a fall2024 midterm question
*/

link deleteone(link h, int n){
    if(h->item==n && h->next==NULL)return NULL;
    if(h->item!=n && h->next==NULL)return h;
    link t=h;
    while (t!=0){
        if(t->next->item==n){
            if(h->next->next==0) {
                h->next=NULL;
                t=t->next;
                delete t;
                return h;
            }                       //this is something u need to cautious
            else{
            h->next=h->next->next;
            t=t->next;
            delete t; // can i delete t->next instead of taking t ??
            return h;
            }
        }
        t=t->next;
        h=h->next;
    }
    return h;
}

/*
This one i completely missed
  // If the head node itself holds the key to be deleted and there are more nodes
    if (h->item == n) {
        link temp = h;
        h = h->next; // Change head
        delete temp; // Free old head
        return h;
    }
*/

/*
Write a function link reverseList(link h) that reverses a singly linked list. 
The function should return the new head of the reversed list. 
Assume that the linked list is not empty.

Example:

Input: 1 -> 2 -> 3 -> 4 -> 5
Output: 5 -> 4 -> 3 -> 2 -> 1
*/

link reverseList(link h){
    link t=h;
    link t1=h;
    link ans=NULL;
    ans->item=0;
    link ans1=NULL;
    ans1->item=0;
    int count=0;
    while (t!=0){
        count++;
        t=t->next;
    }

    for(int i=count;i>=1;i--){
        int a=1;
        while(a!=i){ 
            t1=t1->next;
            a++;
        }
        ans1->item=t1;
        t1=h;
        ans->next=ans1;
        ans=ans->next;
    }
    return ans;
}

/*
ans and ans1 are initialized as NULL, 
but you are trying to access ans1->item 
and ans->next, which causes segmentation faults.
*/

