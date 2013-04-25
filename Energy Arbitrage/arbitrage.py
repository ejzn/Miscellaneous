#!/usr/bin/env python
# Coded by Erik Johson
# erik@erikjohnson.ca

import math, csv

# Read in all the hour data from the spreadsheet csv
hourly_prices = csv.reader(open('prices.csv','rb'), delimiter=',', quotechar='\'' )

# Set up some constants for readability
BUY			= 0
SELL			= 1
BATTERY_MIN_CHARGE 	= 21
BATTERY_MAX_CHARGE	= 210
MAX_HOUR_CHARGE_RATE	= 30
MAX_HOUR_DISCHARGE_RATE	= 30
CHARGE_EFFICIENCY	= 0.925
KILOWATT_CHANGE_FACTOR	= 50


# Set some of the initial values for the simulation
sell_threshold		= 30
current_battery_level 	= 0
current_time_of_day 	= BUY # Possible heuristics to affect the algorithm
current_time_of_year 	= BUY
total_revenue		= 0
avg_purchase_price 	= 0
avg_sale_price 		= 0
new_avg_kwh_price	= 0
avg_kwh_price		= 0

# Determine if we want to be charging or not?
def charging(price_row, battery_change):

	# Check if we really need energy!
	if( current_battery_level <= BATTERY_MIN_CHARGE or ( (current_battery_level < BATTERY_MAX_CHARGE) and (getHour(price_row)) < 8)):
		return -1


	# Let's get the price and hour for our calculations
	current_price 	= getPrice(price_row)
	kwh_price = current_price / battery_change
	curr_average = ((avg_kwh_price + ( KILOWATT_CHANGE_FACTOR) / current_battery_level))
	print "Curr Avg: " , curr_average  , " New: " , kwh_price	
	
	if( current_price > 70):
		# We really should sell from what we know
		return 1

	# Check what the current price looks like in comparison to what weve been buying	
	if( kwh_price > ((avg_kwh_price + KILOWATT_CHANGE_FACTOR) / current_battery_level) and current_price > sell_threshold):
		return 1
	else:
		return -1

# Return the hour portion of the row nicely factoried
def getHour(price_row):
	return float( price_row[1].strip('\n').replace('\"\'',''))

# Return the price portion of the row nicely factoried
def getPrice(price_row):
	return float( price_row[2].strip('\n').replace('\"\'',''))
	
	
index = 0
print "Starting Simulation of Arbitrage of Alberta Energy prices"	
# Get all the prices from the array
for price_row in hourly_prices:
	#if(index < 100):
	#	index+=1
	#else:
	#	break

	# Let's get some electricity
	price_this_hour = getPrice(price_row)
	
	# MARK: Below this can be changed to a weighted moving average, or some other form of a statistical model 
	#	To get better results, experiementation based on the input data, I didn't have time to examine it too much
	#

	if ( ((current_battery_level + MAX_HOUR_CHARGE_RATE) < BATTERY_MAX_CHARGE) and ((current_battery_level + MAX_HOUR_CHARGE_RATE) > BATTERY_MIN_CHARGE)):
		avg_kwh_price = ( avg_kwh_price +  ( price_this_hour / ( MAX_HOUR_CHARGE_RATE * CHARGE_EFFICIENCY)) ) / 2
	else:
		if( ((current_battery_level + MAX_HOUR_CHARGE_RATE) > BATTERY_MAX_CHARGE)):
			battery_charge_change   = BATTERY_MAX_CHARGE - current_battery_level
			if battery_charge_change > 0:
				avg_kwh_price = ( avg_kwh_price +  ( price_this_hour / ( battery_charge_change * CHARGE_EFFICIENCY)) ) / 2
		else:
			battery_charge_change   = current_battery_level - BATTERY_MIN_CHARGE
			if battery_charge_change > 0:
				avg_kwh_price = ( avg_kwh_price +  ( price_this_hour / ( battery_charge_change * CHARGE_EFFICIENCY)) ) / 2


	# Same as per your spreadsheet
	battery_charge_value =  ( MAX_HOUR_CHARGE_RATE * CHARGE_EFFICIENCY)
	battery_charge_change = -1 * charging(price_row, battery_charge_value) * ( MAX_HOUR_CHARGE_RATE * CHARGE_EFFICIENCY)
	hourly_revenue = 0


	if ( ((current_battery_level + battery_charge_change) < BATTERY_MAX_CHARGE) and ((current_battery_level + battery_charge_change) > BATTERY_MIN_CHARGE)):
		hourly_revenue = charging(price_row, battery_charge_value) * MAX_HOUR_CHARGE_RATE * CHARGE_EFFICIENCY * price_this_hour 
		current_battery_level += battery_charge_change
	else:
		# Let's see if we are at a boundary we need ot set it to the max?
		if( ((current_battery_level + battery_charge_change) > BATTERY_MAX_CHARGE)):
			new_battery_level 	= BATTERY_MAX_CHARGE
			battery_charge_change	= BATTERY_MAX_CHARGE - current_battery_level
			hourly_revenue = charging(price_row, battery_charge_value) * battery_charge_change * price_this_hour 
			current_battery_level	= new_battery_level
		else:
			new_battery_level  	=  BATTERY_MIN_CHARGE
			battery_charge_change	= new_battery_level - current_battery_level
			hourly_revenue = -1 * charging(price_row, battery_charge_value) * battery_charge_change * price_this_hour 
			current_battery_level 	= new_battery_level  



	total_revenue += hourly_revenue

	print "Hour: " , getHour(price_row) , "Price" , price_this_hour , "Battery Charge: ", current_battery_level , " Hourly Revenue: " , hourly_revenue , " Total Revenue " , total_revenue 

print " Total calculated revenue is: " , total_revenue



