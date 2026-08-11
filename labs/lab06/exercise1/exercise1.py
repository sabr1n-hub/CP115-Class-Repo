Coffe_Total = 3.50*2
Muffin_Total = 2.10*3
Water_Total = 1.05*4
Sub_Total = Coffe_Total+Muffin_Total+Water_Total
Tax = Sub_Total *0.06
Total = Tax + Sub_Total

print(
    f"==========\tRECEIPT\t==========\n",
    f"Item\tPrice\tQty\tTotal\n",
    f"Coffee\t$3.50\t2\t${Coffe_Total}\n",
    f"Muffin\t$2.10\t3\t${Muffin_Total}\n",
    f"Water\t$1.05\t4\t${Water_Total}\n",
    f"------------------------------\n",
    f"Subtotal\t\t${Sub_Total}\n",
    f"Tax(6%)\t\t${Tax}\n",
    f"Total\t\t${Total}",
)