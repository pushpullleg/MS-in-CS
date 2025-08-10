#include <iostream>
using namespace std;

// Define a Node
struct Node {
    int data;
    Node* next;
};

// Function to print the linked list
void printList(Node* n) {
    while (n != nullptr) {
        cout << n->data << " ";
        n = n->next;
    }
    cout << endl;
}

int main() {
    // Create nodes
    Node* head = nullptr;
    Node* second = nullptr;
    Node* third = nullptr;

    // Allocate nodes in the heap
    head = new Node();
    second = new Node();
    third = new Node();

    // Assign data and link nodes
    head->data = 1; // Assign data to first node
    head->next = second; // Link first node with second

    second->data = 2; // Assign data to second node
    second->next = third; // Link second node with third

    third->data = 3; // Assign data to third node
    third->next = nullptr; // End of list

    // Print the linked list
    printList(head);

    // Free allocated memory
    delete head;
    delete second;
    delete third;

    return 0;
}