int countlinks(link h){
    link t=h;int count=0;
    while (t!=0){
        count++;
        t=t->next;
    }
    return count;
}