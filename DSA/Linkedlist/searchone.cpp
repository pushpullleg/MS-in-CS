void searchone(link h,int k){

    while (t!=0){
        if(t->item==k) cout<<"Presnet";
        t=t->next;
    }
    cout<<"Not Present";
}