input_data = open('input.txt', 'r')
data = input_data.read()
if data == "1":
    output_data.write(str(0))
    output_data.write(' ')
    output_data.write(str(0))    
time = float(data) / 12
time_b = time % 1
time_c = int(time - time_b)
time_2 = int(time_b * 60)
if time_c >= 12:
    output_data.write("NO")
output_data = open('output.txt', 'w')
output_data.write(str(time_c))
output_data.write(' ')
output_data.write(str(time_2))
input_data.close()
output_data.close()