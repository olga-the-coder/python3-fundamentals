integer_number = 1
negative_number = -10
integer_number_underscored = 35_000
float_number = 20.0
boolean_positive = True
boolean_negative = False
format_ex = format(0.1, '.4f')
#python is strongly typed. There are no implicit type conversions
print("Number " + str(integer_number) + " is instance of int ? - " + str(isinstance(integer_number, int)))
#using f-String
print(f"Number {float_number} is instance of float? - {isinstance(float_number, float)}")
#type method
print(type(integer_number_underscored))

