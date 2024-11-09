import pandas as pd

# Define the input file path
input_file = 'C:\\Users\\Eillo\\PycharmProjects\\Store-Sales-AI\\data\\train.csv'  # Replace with the path to your input CSV file

# Define the maximum number of data points per output file
max_data_points_per_file = 1_500_000

# Define the chunk size for reading the data
chunk_size = 100000

# Initialize counters
data_points_copied = 0
file_index = 1

# Open the CSV file in chunks
with pd.read_csv(input_file, chunksize=chunk_size) as reader:
    for chunk in reader:
        # Calculate the remaining data points for the current output file
        remaining_points = max_data_points_per_file - data_points_copied

        # If the chunk has more rows than remaining points, split it
        if len(chunk) > remaining_points:
            # Write the needed rows to the current file
            chunk.iloc[:remaining_points].to_csv(f'copied_data_part_{file_index}.csv',
                                                 mode='a', index=False, header=(data_points_copied == 0))

            # Increment the file index and reset the counter for the next file
            file_index += 1
            data_points_copied = 0

            # Write the remaining part of the chunk to the new file
            chunk = chunk.iloc[remaining_points:]

        # Write the chunk to the current output file
        chunk.to_csv(f'copied_data_part_{file_index}.csv',
                     mode='a', index=False, header=(data_points_copied == 0))

        # Update the counter with the number of rows copied in this chunk
        data_points_copied += len(chunk)

print("Data copy completed. Files created:", file_index)
