#include "forecost.h"
#include <istream>
#include <iostream>
using namespace std;

istream& operator>>(istream& in, Precipitation& P)
{
	string text;
	in >> text;
	if (text == "None")
		P = Precipitation::None;
	else if (text == "Rain")
		P = Precipitation::Rain;
	else if (text == "Snow")
		P = Precipitation::Snow;
	else
		P = Precipitation::Undefined;
	return in;
}

ostream& operator<<(ostream& out, const Precipitation& P)
{
	switch (P)
	{
	case Precipitation::None:
		cout << "None";
		break;
	case Precipitation::Rain:
		cout << "Rain";
		break;
	case Precipitation::Snow:
		cout << "Snow";
		break;
	case Precipitation::Undefined:
	default:
		break;
	}
	return out;
}

istream& operator>>(istream& in, Forecost& F)
{
	F.readFrom(in);
	return in;
}

ostream& operator<<(ostream& out, const Forecost& F)
{
	F.writeTo(out);
	return out;
}

Forecost::Forecost(string name, int number, string month, double temperature, Precipitation precipitation, double amount)
	: day_name(name), day_number(number), month(month),
	day_temperature(temperature), precipitation(precipitation), precipitation_amount(amount)
{}

Forecost::Forecost(const Forecost & F)
	: day_name(F.day_name), day_number(F.day_number), month(F.month), day_temperature(F.day_temperature), precipitation(F.precipitation),
	precipitation_amount(F.precipitation_amount)
{}

string Forecost::getMonth() const
{
	return month;
}

double Forecost::getprecipitationAmount() const
{
	return precipitation_amount;
}

double Forecost::getDayTemperature() const
{
	return day_temperature;
}

string Forecost::getDayName() const
{
	return day_name;
}

void Forecost::changeTemperature(double newTemperature)
{
	day_temperature = newTemperature;
}

void Forecost::changePrecipitation(double newPrecipitation)
{
	precipitation_amount = newPrecipitation;
}

bool Forecost::operator<(const Forecost& F) const
{
	if (month == F.month)
	{
		return day_number < F.day_number;
	}
	else
	{
		return month < F.month;
	}
}

void Forecost::readFrom(istream& in)
{
	in >> day_name >> day_temperature >> month >> day_number >> precipitation >> precipitation_amount;
}

void Forecost::writeTo(ostream& out) const
{
	out << day_name << " " << day_temperature << " " << month << " " << day_number << " " << precipitation << " " << precipitation_amount;
}




	
