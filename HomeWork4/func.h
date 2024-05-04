#pragma once
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int scalarProduct(std::vector<int> a, std::vector<int> b)
{
	int result = 0;
	for (size_t i = 0; i < a.size(); ++i)
	{
		result += a[i] * b[i];
	}
	return result;
}

std::vector<int> multiplyVectorMatrix(std::vector<int> v, std::vector<std::vector<int>> matrix)
{
	std::vector<int> result(matrix[0].size(), 0);
	for (size_t i = 0; i < matrix.size(); ++i)
	{
		for (size_t j = 0; j < matrix[i].size(); ++j)
		{
			result[j] += v[i] * matrix[i][j];
		}
	}
	return result;
}

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