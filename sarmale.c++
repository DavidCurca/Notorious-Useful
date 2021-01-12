#include <iostream>
#include <Windows.h>
#include <bits/stdc++.h>
using namespace std;

int main(int argc, char *argv[]){
    string command = "python sarmale.py ";
    for (int i = 1; i < argc; ++i) {
        command += argv[i];
        command += " ";
    }
    system(command.c_str());
    return 0;
}