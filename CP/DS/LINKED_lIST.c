#include <stdio.h>
#include <stdlib.h>


struct Node{
    int val;
    struct Node* next;
};

struct Node* newNode(int val){
    struct Node* node = NULL;
    node = (struct Node*)malloc(sizeof(struct Node));
    node->val = val;
    node->next = NULL;
    return node;
}
void printList(struct Node* head){
    // struct Node* root = head;
    while(head!=NULL){
        printf("%d->",head->val);
        head = head->next;
    }
    printf("NULL\n");
}

struct Node* insertAtFirst(struct Node* head, int value){
    struct Node* node = newNode(value);
    if (head==NULL){
        head = node;
    }
    node->next = head;
    head = node;
    return head;
}

struct Node* insertAtEnd(struct Node* head, int value){
    struct Node* node = newNode(value);
    if (head==NULL){
        head = node;
    }
    struct Node* root = head;
    while(root->next!=NULL){
        root = root->next;
    }
    root->next = node;
    return head;
}

struct Node* insertAtPosition(struct Node* head, int value, int k){
    struct Node* node = newNode(value);
    if (head==NULL){
        head = node;
    }
    struct Node* root = head;
    int count =0;
    while(root!=NULL){
        count++;
        root = root->next;
    }
    k%=count;
    root = head;
    struct Node* prev = NULL;
    while(k>0){
        prev = root;
        root = root->next;
        k--;
    }
    prev->next = node;
    node->next = root;
    return head;
}

int main(){
    // 1 2 5 7 4 NULL
    struct Node* head = newNode(1);
    head->next = newNode(2);
    head->next->next = newNode(5);
    head->next->next->next = newNode(7);
    head->next->next->next->next = newNode(4);

    //
    int option;
    scanf("Enter select option:\n1 (Insert at front)\n2 (insert at end)\n3 (insert at position k)\n %d", &option);

    int value, k;
    // int value = 8;
    // int k = 4;
    printf("before adding: \n");
    printList(head);
    switch(option){
        case 1:
            scanf("Enter value %d",&value);
            head = insertAtFirst(head,value);
            printf("after adding at front\n");
            printList(head);
            break;
        case 2:
            scanf("Enter value %d",&value);
            head = insertAtEnd(head,value);
            printf("after adding at end\n");
            printList(head);
            break;
        case 3:
            scanf("Enter value %d %d",&value,&k);
            head = insertAtPosition(head,value,k);
            printf("before adding at position k\n");
            printList(head);
            break;

    }
    // printf("before adding at front\n");
    // head = insertAtFirst(head,value);
    // printList(head);

    // printf("before adding at end\n");
    // head = insertAtEnd(head,value);
    // printList(head);

    // printf("before adding at position k\n");
    // head = insertAtPosition(head,value,k);
    // printList(head);


    return 0;
}
