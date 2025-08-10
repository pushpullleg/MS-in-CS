/* return link after deleting the tail node, assume
the link h is not empty */

link deletetail(link h){
    link t=h;link temp=NULL;
    if(h==0) return NULL;
    // If the list has only one node, delete it and return NULL
    if(h->next==0) {
        delete h;           //I forgot to delete 
        return NULL;
    }
    
    while(t->next!=0){
        temp=t;
        t=t->next;
    }
    temp->next=0;
    delete t;
    return h;
}