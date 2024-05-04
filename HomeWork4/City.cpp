#include "City.h"
#include <iostream>
#include <string>
using namespace std;

City::City(string country , string name, int population)
	: city_country(country), city_name(name), city_population(population)
{}

City::City(const City & C)
	: city_country(C.city_country), city_name(C.city_name), city_population(C.city_population)
{}

string City::getCountry() const
{
	return city_country;
}

string City::getName() const
{
	return city_name;
}

int City::getPopulation() const
{
	return city_population;
}

void City::readFrom(std::istream& in)
{
	in >> city_country >> city_name >> city_population;
}

void City::writeTo(std::ostream& out) const
{
	out << "Country: " << city_country
		<< ". Name: " << city_name
		<< ". Population: " << city_population << endl;
}

bool City::operator<(const City& C) const
{
	return city_population < C.city_population;
}

istream& operator>>(istream& in, City& C)
{
	C.readFrom(in);
	return in;
}

ostream& operator<<(ostream& out, const City& C)
{
	C.writeTo(out);
	return out;
}
