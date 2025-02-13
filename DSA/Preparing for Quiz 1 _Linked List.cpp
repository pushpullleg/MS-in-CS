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

