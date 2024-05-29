#pragma once
#include <iostream>
#include <string>
using namespace std;

enum class ScolarType
{
	Regular = 1,
	Social = 2,
	Personal = 3

};
istream& operator>>(istream& in, ScolarType& S)
{
	int type; in >> type;
	S = (ScolarType)type;
	return in;
}
ostream& operator<<(ostream& out, const ScolarType& S)
{
	switch (S)
	{
	case ScolarType::Regular:
		out << "Regular";
		break;
	case ScolarType::Social:
		out << "Social";
		break;
	case ScolarType::Personal:
		out << "Personal";
		break;
	default:
		break;
	}
	return out;
}

template<typename T>
class ScolarShip
{
protected:
	T scolar_value;
	int scolar_month;
	ScolarType scolar_type;
public:
	ScolarShip(T value = T(), int month = 0, ScolarType type = ScolarType::Regular)
		: scolar_value(value), scolar_month(month), scolar_type(type)
	{}
	ScolarShip(const ScolarShip& S)
		: scolar_value(S.scolar_value), scolar_month(S.scolar_month), scolar_type(S.scolar_type)
	{}
	virtual ~ScolarShip() = default;

	virtual void readFrom(istream& in)
	{
		in >> scolar_type >> scolar_value >> scolar_month;
	}
	virtual void writeTo(ostream& out) const
	{
		out << scolar_type << " scolarship. Value: " << scolar_value << " uah. Duration: "
			<< scolar_month << " month. Total: " << getScolarShip() << " uah.\n";
	}
	ScolarType getType() const
	{
		return scolar_type;
	}
	virtual T getScolarShip() const
	{
		return scolar_value * (T)scolar_month;
	}
	bool& operator<(const ScolarShip& S) const
	{
		return getScolarShip() < S.getScolarShip();
	}
	ScolarShip& operator+(T value)
	{
		return ScolarShip(scolar_value + value, scolar_month, scolar_type);
	}
};
template <typename T>
istream& operator>>(istream& in, ScolarShip<T>& S)
{
	S.readFrom(in);
	return in;
}
template <typename T>
ostream& operator<<(ostream& out, const ScolarShip<T>& S)
{
	S.writeTo(out);
	return out;
}

template<typename T>
class PremiumShip : public ScolarShip<T>
{
private:
	int scolar_increase;
public:
	PremiumShip(T value = T(), int month = 0,
		ScolarType type = ScolarType::Regular, int increase = 0)
		: ScolarShip<T>(value, month, type), scolar_increase(increase)

	{}
	PremiumShip(const PremiumShip& P)
		: ScolarShip<T>(P), scolar_increase(P.scolar_increase)
	{}

	virtual void readFrom(istream& in) override
	{
		ScolarShip<T>::readFrom(in);
		in >> scolar_increase;
	}
	virtual void writeTo(ostream& out) const override
	{
		out << "PREMIUM " << scolar_increase << " % ";
		ScolarShip<T>::writeTo(out);
	}
		
	virtual T getScolarShip() const override
	{
		T base = ScolarShip<T>::getScolarShip();
		T increase = base * (T)scolar_increase * 0.01;
		return base + increase;
	}

	void addIncrease(int increase)
	{
		scolar_increase += increase;
	}
};
