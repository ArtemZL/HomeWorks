#pragma once
#include <iostream>
#include <string>
using namespace std;

class City
{
private:
	string city_country;
	string city_name;
	int city_population;
public:
	City(string country = "", string name = "", int population = 0);
	City(const City& C);
	string getCountry() const;
	string getName() const;
	int getPopulation() const;
	void readFrom(std::istream& in);
	void writeTo(std::ostream& out) const;

	bool operator<(const City& C) const;
};

istream& operator>>(istream& in, City& C);
ostream& operator<<(ostream& out, const City& C);