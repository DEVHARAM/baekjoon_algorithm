#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	int count;

	cin >> count;
	for (int i = 0; i < count; i++){
		string t1;
		string t2;
		cin >> t1, cin >> t2;
		bool flag = true;
		vector<char> v1;
		vector<char> v2;
		
		for (int j = 0; j < t1.size(); j++){
			v1.push_back(t1[j]);
			v2.push_back(t2[j]);
		}
		if (v1.size() != v2.size()){
			cout << "Impossible\n";
			continue;
		}

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		for (int j= 0; j < v1.size(); j++){
			if (v1[j] == v2[j])
				continue;
			else{
				flag = false;
				break;
			}
		}
		if (flag == true)
			cout << "Possible\n";

		else
			cout << "Impossible\n";
			
	}
	return 0;
}
