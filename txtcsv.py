import csv

input_file = 'data_mrna_seq_v2_rsem.txt'
output_file = 'data_mrna_seq_v2_rsem.csv'

with open(input_file, 'r') as txt_file:
    # Use csv.reader with delimiter='\t' to handle the tab-separated format
    # This automatically handles potential issues with spaces or varying tab widths
    reader = csv.reader(txt_file, delimiter='\t')
    
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        for row in reader:
            # Clean each cell by removing leading/trailing whitespace
            cleaned_row = [cell.strip() for cell in row]
            writer.writerow(cleaned_row)

print(f"Successfully converted {input_file} to {output_file}")