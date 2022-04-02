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
    while(head!=NULL){
        printf("%d->",head->val);
        head = head->next;
    }
    printf("NULL\n");
}

struct Node* deleteAtFirst(struct Node* head){
    struct Node* node = head;
    if (head==NULL){
        return head;;
    }
    head = head->next;
    node->next = NULL;
    node = NULL;
    return head;
}

struct Node* deleteAtEnd(struct Node* head){
    if (head==NULL){
        return head;
    }
    struct Node* root = head, *prev = NULL;
    while(root->next!=NULL){
        prev = root;
        root = root->next;
    }
    prev->next = NULL;
    root = NULL;
    return head;
}

struct Node* deleteAtPosition(struct Node* head,int k){
    if (head==NULL){
        return head;
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
    while(k>1){
        prev = root;
        root = root->next;
        k--;
    }
    prev->next = root->next;
    root->next = NULL;
    root = NULL;
    return head;
}

int main(){
    // 1 2 5 7 4 NULL
    struct Node* head = newNode(1);
    head->next = newNode(2);
    head->next->next = newNode(5);
    head->next->next->next = newNode(7);
    head->next->next->next->next = newNode(4);

    int option, k;
    printf("Enter select option:\n1 (delete at front)\n2 (delete at end)\n3 (delete at position k)\n");
    scanf("%d", &option);
    printf("before deleting: \n");
    printList(head);
    switch(option){
        case 1:
            printf("after deleting at front\n");
            head = deleteAtFirst(head);
            printList(head);
            break;
        case 2:
            printf("after deleting at end\n");
            head = deleteAtEnd(head);
            printList(head);
            break;
        case 3:
            printf("Enter position: ");
            scanf("%d",&k);
            printf("after deleting at position k\n");
            head = deleteAtPosition(head,k);
            printList(head);
            break;
        default:
            printf("Invalid ip\n");
            break;
    }
    return 0;
}
