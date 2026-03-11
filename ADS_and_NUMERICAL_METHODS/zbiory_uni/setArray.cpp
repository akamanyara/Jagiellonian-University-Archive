#include <iostream>
#include "setArr.h"
#include <algorithm>

// inicjalizacja tabeli konstruktorem
setArr::setArr() : size(0) {
    table = new bool[universeSize];
    std::fill(table, table + universeSize, false);
}

// destruktor dla zwalniania pamieci
setArr::~setArr() {
    delete[] table;
}

bool setArr::checkRangeCorrectness(int x) {
    return x >= 0 && x < universeSize;
}

void setArr::insert(int x) {
    if (checkRangeCorrectness(x) && !table[x]) {
        table[x] = true;
        size++;
    }
}

void setArr::withdraw(int x) {
    if (checkRangeCorrectness(x) && table[x]) {
        table[x] = false;
        size--;
    }
}

bool setArr::isInSet(int i) {
    return checkRangeCorrectness(i) && table[i];
}

int setArr::getSize() {
    return size;
}

void setArr::clearSet() {
    std::fill(table, table + universeSize, false);
    size = 0;
}

void setArr::printSet() {
    std::cout << "{";
    bool first = true;
    for (int i = 0; i < universeSize; i++) {
        if (table[i]) {
            if (!first) std::cout << ", ";
            std::cout << i;
            first = false;
        }
    }
    std::cout << "}\n";
}

// suma
setArr setArr::operator+(setArr& object) {
    setArr result;
    for (int i = 0; i < universeSize; i++) {
        if (table[i] || object.table[i])
            result.insert(i);
    }
    return result;
}

// czesc wspolna
setArr setArr::operator*(setArr& object) {
    setArr result;
    for (int i = 0; i < universeSize; i++) {
        if (table[i] && object.table[i])
            result.insert(i);
    }
    return result;
}

// roznica
setArr setArr::operator-(setArr& object) {
    setArr result;
    for (int i = 0; i < universeSize; i++) {
        if (table[i] && !object.table[i])
            result.insert(i);
    }
    return result;
}

// rownowaznosc
bool setArr::operator==(setArr& object) {
    for (int i = 0; i < universeSize; i++) {
        if (table[i] != object.table[i])
            return false;
    }
    return true;
}

// inkluzja
bool setArr::operator<=(setArr& object) {
    for (int i = 0; i < universeSize; i++) {
        if (table[i] && !object.table[i]) // Jeśli A ma element, którego nie ma B
            return false;
    }
    return true;
}

// ===== TESTY =====
int main() {
    std::cout << "Testowanie klasy setArr:\n";

    setArr setA, setB;
    setA.insert(10);
    setA.insert(20);
    setB.insert(20);
    setB.insert(30);

    std::cout << "Zbiór A: ";
    setA.printSet();

    std::cout << "Zbiór B: ";
    setB.printSet();

    setArr unionSet = setA + setB;
    std::cout << "Suma zbiorów (A + B): ";
    unionSet.printSet();

    setArr intersectionSet = setA * setB;
    std::cout << "Część wspólna (A * B): ";
    intersectionSet.printSet();

    setArr differenceSet = setA - setB;
    std::cout << "Różnica (A - B): ";
    differenceSet.printSet();

    // Test operatora ==
    setArr setC;
    setC.insert(10);
    setC.insert(20);
    std::cout << "Zbior C: ";
    setC.printSet();
    std::cout << "Czy A == C? " << (setA == setC ? "TAK" : "NIE") << "\n";

    // Test operatora <=
    std::cout << "Czy A <= B? " << (setA <= setB ? "TAK" : "NIE") << "\n";
    std::cout << "Czy A <= unionSet? " << (setA <= unionSet ? "TAK" : "NIE") << "\n";

    return 0;
}