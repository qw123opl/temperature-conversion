unit = input("請選擇輸入的溫度單位(F/C): ")
temperature = int(input("請輸入要換算的溫度: "))
if unit == "F":
    print("換算結果為: 攝氏", (temperature-32)*5/9, "度")
else:
    print("換算結果為: 華氏", 9/5*temperature+32, "度")
