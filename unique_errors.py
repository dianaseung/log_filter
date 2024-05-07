def filter_unique_errors(log_file, output_file):
  """
  This function reads a Liferay log file and writes unique error messages to a file.

  Args:
      log_file (str): Path to the Liferay log file.
      output_file (str): Path to the output file for unique errors.
  """
  seen_errors = set()
  with open(log_file, 'r') as f, open(output_file, 'w') as out_file:
    for line in f:
      if 'ERROR' in line:
        # Extract error message (assuming basic format)
        error_message = line.split('ERROR', 1)[1].strip()
        if error_message not in seen_errors:
          seen_errors.add(error_message)
          out_file.write(error_message + '\n')

# Example usage
log_file = "liferay.log"
output_file = "unique_errors.txt"  # Replace with desired output filename
filter_unique_errors(log_file, output_file)
