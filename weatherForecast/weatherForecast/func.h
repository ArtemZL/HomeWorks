#pragma once
#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

template <typename T>
void print(const vector<T>& v, const char* delim = " ")
{
	copy(v.cbegin(), v.cend(), ostream_iterator<T>(cout, delim));
	cout << endl;
}

template <typename T>
void readElement(vector<T>& v, string fileName)
{
	ifstream fin(fileName);
	T elem;
	while (!fin.eof())
	{
		fin >> elem;
		v.push_back(elem);
	}
	fin.close();
}

template <typename T>
void read(vector<T>& v, string fileName)
{
	ifstream fin(fileName);
	copy(istream_iterator<T>(fin), istream_iterator<T>(), back_inserter(v));
	fin.close();
}

double calculateTotalPrecipitation(const vector<Forecost>& forecasts, const string& targetMonth)
{
	double totalPrecipitation = 0.0;
	for_each(forecasts.begin(), forecasts.end(), [&totalPrecipitation, &targetMonth](const Forecost& forecast) 
		{
		if (forecast.getMonth() == targetMonth) 
		{
			totalPrecipitation += forecast.getprecipitationAmount();
		}
		});
	return totalPrecipitation;
}

int countDryDays(const vector<Forecost>& forecasts, const string& targetMonth)
{
	return count_if(forecasts.begin(), forecasts.end(), [&targetMonth](const Forecost& forecast) 
		{
		return forecast.getMonth() == targetMonth && forecast.getprecipitationAmount() == 0.0;
		});
}

vector<double> getUniqueTemperaturesForDay(const vector<Forecost>& forecasts, const string& targetDay)
{
	vector<double> temperatures;
	for_each(forecasts.begin(), forecasts.end(), [&temperatures, &targetDay](const Forecost& forecast)
		{
		if (forecast.getDayName() == targetDay) 
		{
			temperatures.push_back(forecast.getDayTemperature());
		}
		});

	sort(temperatures.begin(), temperatures.end());

	auto last = unique(temperatures.begin(), temperatures.end());
	temperatures.erase(last, temperatures.end());

	return temperatures;
}