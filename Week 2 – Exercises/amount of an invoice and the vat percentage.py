
def calculate_total_payment(amount, vat_percentage): 
    vat_amount = amount * (vat_percentage / 100)
    total_payment = amount + vat_amount1
    return total_payment


def main():
   
    amount = float(input("Enter the amount of the invoice: "))
    vat_percentage = float(input("Enter the VAT percentage: "))
    
  
    total = calculate_total_payment(amount, vat_percentage)
    
   
    print(f'TOTAL: {total:.2f}')


if __name__ == "__main__":
    main()
