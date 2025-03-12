#!/bin/bash

# Directory to store test logs
LOG_DIR="test_logs"
mkdir -p "$LOG_DIR"

# Find the next available log filename
i=1
while [[ -f "$LOG_DIR/test_output_$i.txt" ]]; do
    ((i++))
done
LOG_FILE="$LOG_DIR/test_output_$i.txt"

# Run pytest and save output to the file
pytest tests/ -v | tee "$LOG_FILE"

echo "Test results saved to $LOG_FILE"

