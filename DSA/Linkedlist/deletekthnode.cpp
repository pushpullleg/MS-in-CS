link deletekthnode(link h, int k){
    link t=h;
    link temp=NULL;
    int count =k-1;
    if (k <= 0) return h;
   
    if (k==1){
        h=h->next;
        delete t;
        return h;
    }
    while (count > 0 ){
        if (temp==NULL && t== NULL)return h;  // this one is missing 
        temp=t;
        t=t->next;
        count--;
       
    }
  
    if (t->next==0){
        temp->next=0;
        delete t;
        return h;
    }
    else{
    temp->next=t->next;
    delete t;
    return h ;
    }
}