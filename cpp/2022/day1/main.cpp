#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool myfunction (int i,int j) { 
    return (i>j); 

}
    
int main() {
    ifstream myfile;
    myfile.open("input.txt");

    vector<int> numbers;

    string line;
    int cum_sum = 0;
    if ( myfile.is_open() ) {
        while (getline(myfile, line)) {
            if (line == "") {
                numbers.push_back(cum_sum);
                cum_sum = 0;
            } else {
                cum_sum += stoi(line);
            }
        }
    }
    
    numbers.push_back(cum_sum);
    int res = 0;
    sort(numbers.begin(), numbers.end(), myfunction);
    for (int i = 0; i < 3; i++) {
        res += numbers[i];
    }
    cout << res << endl;
    return 0;
}
