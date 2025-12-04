
#include <fstream>
#include <iostream>



int main() {
    std::ifstream file("day10.txt");

    std::string line;
    
    while (std::getline(file, line)) {
        std::cout << line << std::endl;
    }

    file.close();
}