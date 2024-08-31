import numpy as np

def process_file(input_file, output_file):
    # Read the input file and extract the numbers
    with open(input_file, 'r') as file:
        data = file.read()
    
    # Convert the string data into a list of floats
    numbers = [float(num) for num in data.split()]
    
    # Find the largest value in the list
    max_value = max(numbers)
    
    # Process the numbers: divide by the max value and set negative values to 0
    processed_numbers = [round((num / max_value)*128) if num > 0 else 0 for num in numbers]
    
    # Convert the processed numbers back to a string
    processed_data = ' '.join(map(str, processed_numbers))
    
    # Write the processed data to the output file
    with open(output_file, 'w') as file:
        file.write(processed_data)

def convert_file_to_tensor(file):
    with open(file, 'r') as file:
        data = file.read()
        numbers = [int(num) for num in data.split()]

        listcomp = [numbers[i:i+256:] for i in range(0,256*4*255, 256 * 4)]
        # print(listcomp)

        summary = []
        column_sum = 0
       
        for i in range(len(listcomp)):
            sum = 0
            for j in range(0,len(listcomp[i]),8):
                if (j % 8 != 0) :
                    sum += listcomp[i][j]   
                else:
                    column_sum += sum/8
            if i % 8 == 0:
                summary.append(column_sum / 8)

        # print(summary)

        retlist = [summary[i:i+7:1] for i in range(len(summary)-8)]
        print(retlist)

        retense = np.array(retlist)
        # print(retense)

        return retense


# Example usage

def main_method():
    input_file = '/Users/rithwiknukala/Desktop/blenderChatbot/DepthDataInterp/input.txt'
    output_file = '/Users/rithwiknukala/Desktop/blenderChatbot/DepthDataInterp/output.txt'
    process_file(input_file, output_file)
    return convert_file_to_tensor(output_file)

main_method()


