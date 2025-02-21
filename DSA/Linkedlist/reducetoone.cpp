link reducetoone(link h){
    link t=h;
    link temp=h;
    if(h->next==0){
        return h;
    }
    while(t->next!=0){
        temp=t;
        t=t->next;
        delete temp; //did i by mistake delete t in mid term ?
    }
    return t;
}

