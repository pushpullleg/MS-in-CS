/*this is the example no.11 tejaswini class notes
output all the items in the linkedlist 1 but not in l2
assuming that both the linkedlist are sorted in order 

I have a sub question came to my mind , arrange and return 
linkedlist in sorting 
*/

void diff(link l1,link l2){
    link t1=l1;
    link t2=l2;
    if(t2==0){              //this is a edge case that i missed 
        while (t1!=0){            
            cout<<t1->item;<<" ";
            t1=t1->next;
        }
        return;
    }
    while(t1!=0 && t2!=0){
        if(t1->item==t2->item){
            t1=t1->next;
            t2=t2->next;
        }
        else if(t1->item < t2->item){
            t1=t1->next;
        }else{
            cout<<t1->item;
            t1=t1->next;
            t2=t2->next;
        }
    }
    while (t1!=0){ //this case i missed 
        cout<< t1->item << " ";
        t1=t1->next;

    } 
}

/*learning these two functions were missed */ 
// Output remaining items in t1
// If l2 is empty, output all items in l1
