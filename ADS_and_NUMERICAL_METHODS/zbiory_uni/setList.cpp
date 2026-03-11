#include <iostream>
#include <vector>
#include <algorithm>
#include "setList.h"

// zwraca liczbę elementów w zbiorze
int setList::getSize() {
    return vec.size();
}

// wypisuje elementy zbioru
void setList::printSet() {
    std::cout << "{";
    for (size_t i = 0; i < vec.size(); i++) {
        if (i > 0) std::cout << ", ";
        std::cout << vec[i];
    }
    std::cout << "}\n";
}

// dodaje element do zbioru
void setList::insert(int x) {
    if (!isInSet(x)) {
        vec.push_back(x);
    }
}

// usuwa element ze zbioru
void setList::withdraw(int x) {
    vec.erase(std::remove(vec.begin(), vec.end(), x), vec.end());
}

// sprawdza, czy element jest w zbiorze
bool setList::isInSet(int x) {
    return std::find(vec.begin(), vec.end(), x) != vec.end();
}

// suma zbiorów
setList setList::operator+(setList& obj) {
    setList result = *this;
    for (int x : obj.vec) {
        result.insert(x);
    }
    return result;
}

// część wspólna zbiorów
setList setList::operator*(setList& obj) {
    setList result;
    for (int x : vec) {
        if (obj.isInSet(x)) {
            result.insert(x);
        }
    }
    return result;
}

// różnica zbiorów
setList setList::operator-(setList& obj) {
    setList result;
    for (int x : vec) {
        if (!obj.isInSet(x)) {
            result.insert(x);
        }
    }
    return result;
}

// rownowaznosc zbiorow
bool setList::operator==(setList& obj) {
    if (vec.size() != obj.vec.size()) return false;
    for (int x : vec) {
        if (!obj.isInSet(x)) return false;
    }
    return true;
}

// inkluzja zbiorow
bool setList::operator<=(setList& obj) {
    for (int x : vec) {
        if (!obj.isInSet(x)) return false;
    }
    return true;
}

// ==== TESTY ====
int main() {
    std::cout << "\nTestowanie klasy setList:\n";

    setList listA, listB;
    listA.insert(10);
    listA.insert(20);
    listB.insert(20);
    listB.insert(30);

    std::cout << "Zbiór A: ";
    listA.printSet();
    
    std::cout << "Zbiór B: ";
    listB.printSet();

    setList unionList = listA + listB;
    std::cout << "Suma zbiorów (A + B): ";
    unionList.printSet();

    setList intersectionList = listA * listB;
    std::cout << "Część wspólna (A * B): ";
    intersectionList.printSet();

    setList differenceList = listA - listB;
    std::cout << "Różnica (A - B): ";
    differenceList.printSet();

    std::cout << "Czy A == B? " << (listA == listB ? "TAK" : "NIE") << "\n";
    std::cout << "Czy A <= B? " << (listA <= listB ? "TAK" : "NIE") << "\n";
    std::cout << "Czy A <= unionList? " << (listA <= unionList ? "TAK" : "NIE") << "\n";

    return 0;
}