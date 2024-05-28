#include <iostream>
#include <vector>
#include "forecost.h"
#include "func.h"
#include <fstream>
#include <algorithm>
using namespace std;



int main()
{
	vector<Forecost> forecost;
	read(forecost, "forecost.txt");
	cout << "Weather forecoast:\n";
	print(forecost, "\n");
	cout << endl;
	
	sort(forecost.begin(), forecost.end());
	print(forecost, "\n");

	string targetMonth;
	cout << "Enter the month to calculate precipitation: ";
	cin >> targetMonth;

	double totalPrecipitation = calculateTotalPrecipitation(forecost, targetMonth);
	int dryDays = countDryDays(forecost, targetMonth);
	cout << "Total precipitation in: " << targetMonth << " is: " << totalPrecipitation << "\n";
	cout << "Dry days in: " << targetMonth << " is: " << dryDays << "\n";

	vector<Forecost> dryDay;
	copy_if(forecost.begin(), forecost.end(), back_inserter(dryDay), [](const Forecost& forecast)
		{
			return forecast.getprecipitationAmount() == 0.0;
		});
	sort(forecost.begin(), forecost.end(), [](const Forecost& a, const Forecost& b)
		{
			return a.getDayTemperature() < b.getDayTemperature();
		});
	print(dryDay, "\n");

	string targetDay;
	cout << " Enter the day: ";
	cin >> targetDay;

	vector<double> uniqueTemperatures = getUniqueTemperaturesForDay(forecost, targetDay);
	cout << "Unique temperatures for: " << targetDay << ": ";
	print(uniqueTemperatures, "\n");

	return 0;
}
// В мене сортування, мабуть, що не так працює
// Воно не сортує за місяцями
// Я вже не знав як це виправити і лишив так як є. Тобто воно сортує за днем місяця але місяці не йдуть по порядку
