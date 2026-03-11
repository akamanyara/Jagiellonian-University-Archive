#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include "Graf.h"
#include <algorithm>

Graf::Graf() {}

void Graf::createVertices(int ile) {
    vertexList.resize(ile);
}

void Graf::addEdge(int i_Vertex_Index_1, int i_Vertex_Index_2) {
    if (i_Vertex_Index_1 >= vertexList.size() || i_Vertex_Index_2 >= vertexList.size()) return;
    vertexList[i_Vertex_Index_1].emplace_back(i_Vertex_Index_1, i_Vertex_Index_2);
    vertexList[i_Vertex_Index_2].emplace_back(i_Vertex_Index_2, i_Vertex_Index_1);
}

bool Graf::removeEdge(int i_Vertex_Index_1, int i_Vertex_Index_2) {
    if (i_Vertex_Index_1 >= vertexList.size() || i_Vertex_Index_2 >= vertexList.size()) return false;
    
    std::vector<edge> &edges1 = vertexList[i_Vertex_Index_1];
    std::vector<edge> &edges2 = vertexList[i_Vertex_Index_2];
    
    edges1.erase(std::remove_if(edges1.begin(), edges1.end(), [&](const edge &e) {
        return e.vertex_Index2 == i_Vertex_Index_2;
    }), edges1.end());
    
    edges2.erase(std::remove_if(edges2.begin(), edges2.end(), [&](const edge &e) {
        return e.vertex_Index2 == i_Vertex_Index_1;
    }), edges2.end());
    
    return true;
}

bool Graf::checkEdge(int i_Vertex_Index_1, int i_Vertex_Index_2) {
    if (i_Vertex_Index_1 >= vertexList.size() || i_Vertex_Index_2 >= vertexList.size()) return false;
    
    for (const edge &e : vertexList[i_Vertex_Index_1]) {
        if (e.vertex_Index2 == i_Vertex_Index_2) return true;
    }
    return false;
}

int Graf::vertexDegree(int idx) {
    if (idx >= vertexList.size()) return -1;
    return vertexList[idx].size();
}

std::vector<int> Graf::getNeighbourIndices(int idx) {
    std::vector<int> neighbours;
    if (idx >= vertexList.size()) return neighbours;
    for (const edge &e : vertexList[idx]) {
        neighbours.push_back(e.vertex_Index2);
    }
    return neighbours;
}

void Graf::printNeighbourIndices(int idx) {
    if (idx >= vertexList.size()) return;
    for (const edge &e : vertexList[idx]) {
        std::cout << e.vertex_Index2 << " ";
    }
    std::cout << std::endl;
}

int Graf::getNumberOfEdges() {
    int count = 0;
    for (const std::vector<edge> &edges : vertexList) {
        count += edges.size();
    }
    return count / 2;
}

void Graf::readFromFile(std::string path) {
    std::ifstream file(path);
    if (!file.is_open()) return;
    
    int v1, v2;
    while (file >> v1 >> v2) {
        addEdge(v1, v2);
    }
    file.close();
}
