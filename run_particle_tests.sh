#!/bin/bash

# Directory to store test output files
OUTPUT_DIR="test_outputs"
mkdir -p "$OUTPUT_DIR"

# Find the next available file number
i=1
while [[ -e "$OUTPUT_DIR/test_output_${i}.txt" ]]; do
    ((i++))
done

# Run pytest for test_particle_system.py and save output to an incremented file
pytest tests/test_particle_system.py | tee "$OUTPUT_DIR/test_output_${i}.txt"

echo "Test output saved to: $OUTPUT_DIR/test_output_${i}.txt"

