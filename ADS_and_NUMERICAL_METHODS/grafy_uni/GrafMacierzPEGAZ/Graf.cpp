#include "Graf.h"
#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

Graf::Graf() : numberOfVertices(0) {
    clear();
}

void Graf::clear() {
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            matrix[i][j] = 0;
        }
    }
}

void Graf::createVertices(int ile) {
    if (ile > 100) {
        std::cerr << "Maksymalna liczba wierzchołków to 100." << std::endl;
        return;
    }
    numberOfVertices = ile;
}

void Graf::addEdge(int i_Vertex_Index_1, int i_Vertex_Index_2) {
    if (i_Vertex_Index_1 < numberOfVertices && i_Vertex_Index_2 < numberOfVertices) {
        matrix[i_Vertex_Index_1][i_Vertex_Index_2] = 1;
        matrix[i_Vertex_Index_2][i_Vertex_Index_1] = 1;
    }
}

void Graf::removeEdge(int i_Vertex_Index_1, int i_Vertex_Index_2) {
    if (i_Vertex_Index_1 < numberOfVertices && i_Vertex_Index_2 < numberOfVertices) {
        matrix[i_Vertex_Index_1][i_Vertex_Index_2] = 0;
        matrix[i_Vertex_Index_2][i_Vertex_Index_1] = 0;
    }
}

bool Graf::checkEdge(int i_Vertex_Index_1, int i_Vertex_Index_2) {
    return (i_Vertex_Index_1 < numberOfVertices && i_Vertex_Index_2 < numberOfVertices && matrix[i_Vertex_Index_1][i_Vertex_Index_2] == 1);
}

int Graf::vertexDegree(int idx) {
    if (idx >= numberOfVertices) return -1;
    int degree = 0;
    for (int i = 0; i < numberOfVertices; i++) {
        degree += matrix[idx][i];
    }
    return degree;
}

std::vector<int> Graf::getNeighbourIndices(int idx) {
    std::vector<int> neighbours;
    if (idx >= numberOfVertices) return neighbours;
    
    for (int i = 0; i < numberOfVertices; i++) {
        if (matrix[idx][i] == 1) {
            neighbours.push_back(i);
        }
    }
    return neighbours;
}

void Graf::printNeighbourIndices(int idx) {
    std::vector<int> neighbours = getNeighbourIndices(idx);
    for (int n : neighbours) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
}

int Graf::getNumberOfEdges() {
    int count = 0;
    for (int i = 0; i < numberOfVertices; i++) {
        for (int j = i + 1; j < numberOfVertices; j++) {
            if (matrix[i][j] == 1) {
                count++;
            }
        }
    }
    return count;
}

void Graf::readFromFile(std::string path) {
    std::ifstream file(path);
    if (!file) {
        std::cerr << "Nie można otworzyć pliku!" << std::endl;
        return;
    }
    int n, a, b;
    file >> n;
    createVertices(n);
    while (file >> a >> b) {
        addEdge(a, b);
    }
}
