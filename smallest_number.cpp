//第一行输入数组大小n
//第二行输入数组内的数
//将这些数排列成一串最小的数,0可以在最前
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

static bool cmp(int a, int b) {
    string A = "";
    string B = "";
    A += to_string(a);
    A += to_string(b);
    B += to_string(b);
    B += to_string(a);

    return A < B;
}
string PrintMinNumber(vector<int> numbers) {
    string  answer = "";
    sort(numbers.begin(), numbers.end(), cmp);
    for (int i = 0;i < numbers.size();i++) {
        answer += to_string(numbers[i]);
    }
    return answer;
}

int main() {
    int n;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    string res = PrintMinNumber(arr);
    cout << res << endl;
    return 0;
}
