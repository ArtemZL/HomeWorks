#pragma once
#include <iostream>
#include <string>
#include <istream>

using namespace std;

enum class Precipitation
{
	None,
	Rain,
	Snow,
	Undefined
};

istream& operator>>(istream& in, Precipitation& P);
ostream& operator<<(ostream& out, const Precipitation& P);

class Forecost
{
private:
	string day_name;
	int day_number;
	string month;
	double day_temperature;
	Precipitation precipitation;
	double precipitation_amount;

public:
	Forecost(string name = "", int number = 0, string month = "",
		double temperature = 0.0, Precipitation precipitation = Precipitation::Undefined, double amount = 0.0);
	Forecost(const Forecost& F);

	string getMonth() const;
	double getprecipitationAmount() const;
	double getDayTemperature() const;
	string getDayName() const;
	void changeTemperature(double newTemperature);
	void changePrecipitation(double newPrecipitation);
	bool operator<(const Forecost& F) const;
	void readFrom(istream& in);
	void writeTo(ostream& out) const;
};

istream& operator>>(istream& in, Forecost& F);
ostream& operator<<(ostream& out, const Forecost& F);
