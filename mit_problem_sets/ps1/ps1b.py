def main():
	
	
	
	
	
	
	
	############################################################
	#
	#	Block:	Data structure
	#
	#
	############################################################
	
	
	#Number of months requierd to get enough for down paymant
	month_count_down_payment = 0
	#Coast of a home
	total_cost = 0.0
	#Portion of cost for down payment decimal (%/100)
	portion_down_paymant = 0.25
	#Currently saved amount in dollars $
	current_savings = 0.0
	#Annual investment return decimal (%/100)
	r = 0.04
	#Annual salary
	annual_salary = 0.0
	#Portion of a salary saved decimal (%/100)
	portion_saved = 0.1
	#Count of months required for down payment
	month_count_down_payment = 0.0
	#How much salry increases every 6 months decimal (%/100)
	semi_annual_rais = 0.0
	
	
	
	
	
	
	
	############################################################
	#
	#	Block:	User input
	#
	#
	############################################################
	
	
	annual_salary    = float( input("Enter starting annual salary: ") )
	portion_saved    = float( input("Enter portion of monthly salary for saving: ") )
	total_cost       = float( input("Enter total cost of your dream home: ") )
	semi_annual_rais = float( input("Enter semi annual rais: ") )
	
	
	
	
	
	
	
	############################################################
	#
	#	Block:	Algorithm for time required for down payment
	#
	#
	############################################################
	
	
	#Add savings monthly and count months
	while( current_savings < total_cost * portion_down_paymant ):
		
		
		month_count_down_payment += 1
		
		
		if month_count_down_payment % 6 == 0:
			annual_salary += annual_salary * semi_annual_rais
		#End if
		
		
		#Add investment return
		current_savings += current_savings * r/12.0
		#Add monthly savings
		current_savings += annual_salary/12.0 * portion_saved
		
		
	#End while
	
	
	
	
	
	
	
	############################################################
	#
	#	Block:	Program output
	#
	#
	############################################################
	
	
	#Output to the console
	print( int(month_count_down_payment) )
	
#End main





























#Starts from main after script loads
if __name__ == "__main__":
	main()
#End if
