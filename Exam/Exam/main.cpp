#include <iostream>
#include "ScoolarShip.h"
#include <vector>
#include <algorithm>
#include <fstream>
#include <set>

using namespace std;
int main()
{
	PremiumShip<int> a(2000, 12, ScolarType::Regular, 10);
	ScolarShip<double> b(1999.99, 12, ScolarType::Personal);
	cout << a << b << endl;
	ScolarShip<int> x;
	PremiumShip<int> y;

	vector<ScolarShip<int>*> money;
	money.push_back(new PremiumShip<int>(a));

	ifstream fin("Text.txt");
	while (!fin.eof())
	{
		char type; fin >> type;
		if (type == 'S')
		{
			money.push_back(new ScolarShip<int>());
			fin >> *money.back();
		}
		else if (type == 'P')
		{
			money.push_back(new PremiumShip<int>());
			fin >> *money.back();
		}
		else
		{
			string temp; getline(fin, temp);
		}
	}
	fin.close();

	//char flag = 'Y';
	//while (flag != 'N')
	//{
	//	cout << "Enter ScolarShip(S) / PremiumShip(P) / Exit(N): ";
	//	cin >> flag;
	//	if (flag == 'S')
	//	{
	//		cout << "Enter SColarShip details (type(1/2/3), value, month)\n";
	//		money.push_back(new ScolarShip<int>());
	//		cin >> *money.back();
	//	}
	//	else if (flag == 'P')
	//	{
	//		cout << "Enter PremiumShip details (type(1/2/3), value, months, increase)\n";
	//		money.push_back(new PremiumShip<int>());
	//		cin >> *money.back();
	//	}
	//	else
	//	{
	//		flag = 'N';
	//	}
	//}
	//

	cout << "\nAll scolarships:\n";
	for_each(money.cbegin(), money.cend(), [](const auto item)
		{
			cout << *item;
		});
	cout << endl;

	set<ScolarType> types;
	transform(money.cbegin(), money.cend(), inserter(types, types.begin()), [](const auto& item)
		{
			return item->getType();
		});
	cout << "All Scolarships types:\n";
	copy(types.begin(), types.end(), ostream_iterator<ScolarType>(cout, " "));
	cout << "\n\n";

	

	return 0;
}