def weight_on_planets():
   # cast is changing an operation form float to string 
   weight = input("What do you weigh on earth? ")
   weight = int(weight)
   mar_weight = 0.38 * weight
   jup_weight = 2.34 * weight
   line1 = f"\nOn Mars you would weigh {mar_weight} pounds.\n"
   line2 = f"On Jupiter you would weigh {jup_weight} pounds."
   print(line1 + line2)   
   
if __name__ == '__main__':
   weight_on_planets()