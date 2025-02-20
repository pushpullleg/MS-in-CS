link reducetoone(link h){
    link t=h;
    link temp=h;
    if(h->next==0){
        return h;
    }
    while(t->next!=0){
        temp=t;
        t=t->next;
        delete t;
    }
    return t;
}

