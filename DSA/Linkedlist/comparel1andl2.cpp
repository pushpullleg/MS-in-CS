/*this is the example no.11 tejaswini class notes
output all the items in the linkedlist 1 but not in l2
assuming that both the linkedlist are sorted in order 

I have a sub question came to my mind , arrange and return 
linkedlist in sorting 
*/

void diff(link l1,link l2){
    link t1=l1;
    link t2=l2;
    if(t2==0){
        while (t1!=0){
            cout<<t1->item;
            t=t->next;
        }
    }
    while(t1!=0 && t2!=0){
        if(t1->item==t2->item){
            t1=t1->next;
            t2=t2->next;
        }
        if(t1->item<t2->item){
            t1=t1->next;
        }else{
            cout<<t1->item;
            t1=t1->next;
            t2=t2->next;
        }
    }

}