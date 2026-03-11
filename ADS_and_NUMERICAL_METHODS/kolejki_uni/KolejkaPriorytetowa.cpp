#include <iostream>
#include <vector>
#include "KolejkaPriorytetowa.h"

using namespace std;

void KolejkaPriorytetowa::heapifyUp(int index) {
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (heap[index] > heap[parent]) {
            swap(heap[index], heap[parent]);
            index = parent;
        } else {
            break;
        }
    }
}

void KolejkaPriorytetowa::heapifyDown(int index) {
    int leftChild, rightChild, largest;
    while (true) {
        leftChild = 2 * index + 1;
        rightChild = 2 * index + 2;
        largest = index;

        if (leftChild < heap.size() && heap[leftChild] > heap[largest]) {
            largest = leftChild;
        }
        if (rightChild < heap.size() && heap[rightChild] > heap[largest]) {
            largest = rightChild;
        }
        if (largest == index) {
            break;
        }
        swap(heap[index], heap[largest]);
        index = largest;
    }
}

void KolejkaPriorytetowa::insert(int x) {
    heap.push_back(x);
    heapifyUp(heap.size() - 1);
}

int KolejkaPriorytetowa::RemoveRootElem() {
    if (heap.empty()) {
        throw runtime_error("Heap is empty");
    }
    int root = heap[0];
    heap[0] = heap.back();
    heap.pop_back();
    if (!heap.empty()) {
        heapifyDown(0);
    }
    return root;
}

int KolejkaPriorytetowa::getRootElem() {
    if (heap.empty()) {
        throw runtime_error("Heap is empty");
    }
    return heap[0];
}

void KolejkaPriorytetowa::print() {
    for (int val : heap) {
        cout << val << " ";
    }
    cout << endl;
}

int main() {
    KolejkaPriorytetowa pq;
    pq.insert(10);
    pq.insert(20);
    pq.insert(15);
    pq.insert(30);
    pq.insert(40);

    cout << "Kolejka po wstawieniu elementów: ";
    pq.print();

    cout << "Usunięty element: " << pq.RemoveRootElem() << endl;
    cout << "Kolejka po usunięciu korzenia: ";
    pq.print();

    cout << "Aktualny korzeń: " << pq.getRootElem() << endl;
    
    return 0;
}

