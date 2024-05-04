#include <iostream>
#include <vector>
#include "func.h"
#include "City.h"
#include <algorithm>
using namespace std;

int main()
{
	int choice;
	cout << "Enter your choice: " << endl;
	cout << " 1. Scalar product of vectors" << endl;
	cout << " 2. Multiply vector by matrix" << endl;
	cin >> choice;

	switch (choice)
	{
	case 1:
	{
		std::vector<int> a = { 1, 2, 3 };
		std::vector<int> b = { 2, 2, 2 };
		int result = scalarProduct(a, b);
		cout << "Scalar product of vectors: " << result << endl;
		break;
	}
	case 2:
	{
		std::vector<int> v = { 2, 2, 2 };
		std::vector<std::vector<int>> matrix = { {1, 4}, {2, 5}, {3, 6} };
		std::vector<int> result1 = multiplyVectorMatrix(v, matrix);
		cout << "Result of vectors-matrix multiplacation: [";
		for (size_t i = 0; i < result1.size(); ++i)
		{
			cout << result1[i];
			if (i < result1.size() - 1)
			{
				cout << " ";
			}
		}
		cout << "]" << endl;
		break;
	}
	default:
		break;
	}

	
	vector<City> cities;
	read(cities, "Text1.txt");
	cout << "Eastern cities:\n";
	print(cities, "");
	cout << endl;

	vector<City> cities2;
	read(cities2, "Text2.txt");
	cout << "Buetiful cities:\n";
	print(cities2, "");
	cout << endl;

	vector<City> cities3;
	read(cities3, "Text3.txt");
	cout << "Central cities:\n";
	print(cities3, "");
	cout << endl;

	cities.insert(cities.begin(), cities2.begin(), cities2.end());
	copy(cities3.cbegin(), cities3.cend(), back_inserter(cities));
	cout << "All cities:\n";
	print(cities);

	sort(cities.rbegin(), cities.rend());
	cout << "Sorted cities:\n";
	print(cities);

	vector<pair<string, vector<City>>> city_countrys;
	for (size_t i = 0; i < cities.size(); ++i)
	{
		string brand = cities[i].getCountry();
		int population = cities[i].getPopulation();

		bool added = false;
		for (size_t j = 0; j < city_countrys.size(); ++j)
		{
			if (city_countrys[j].first == brand)
			{
				city_countrys[j].second.push_back(cities[i]);
				added = true;
				break;
			}
		}

		if (!added)
		{
			city_countrys.push_back(make_pair(brand, vector<City>({ cities[i] })));
		}
	}

	cout << " Sorted be countrys:\n";
	for (size_t i = 0; i < city_countrys.size(); ++i)
	{
		cout << city_countrys[i].first << " citys:\n";
		print(city_countrys[i].second, "");
		cout << endl;
	}

	cout << "Total population bu country:\n";
	for (size_t i = 0; i < city_countrys.size(); ++i)
	{
		string country = city_countrys[i].first;
		int totalPopulation = 0;
		for (int j = 0; j < city_countrys[i].second.size(); ++j)
		{
			totalPopulation += city_countrys[i].second[j].getPopulation();
		}
		cout << "\nTotal population of " << country << ": " << totalPopulation << "\n\n";
	}

	
	


	return 0;
}

