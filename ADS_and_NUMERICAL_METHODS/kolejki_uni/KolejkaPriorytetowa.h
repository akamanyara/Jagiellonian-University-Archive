#pragma once
#include <array>

using namespace std;

class KolejkaPriorytetowa
{
    private: // dodane zeby kazda instancja miala swoja kolejke, nie jedna globalna
    vector<int> heap;

    void heapifyUp(int index);
    void heapifyDown(int index);

    public:
    void insert(int x);
    int RemoveRootElem();
    void print();   //opcjonalnie dla wy�wietlenia kolejnych element�w macierzy, w kt�rej trzymany jest kopiec.
    int getRootElem();
};