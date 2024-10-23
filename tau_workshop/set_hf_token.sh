
#!/bin/bash

# Prompt the user for the value of the environment variable
read -p "Enter your huggingface token: " var_value;

# Export the environment variable
export HF_TOKEN=$var_value;

# Display the created environment variable
echo "Environment variable HF_TOKEN set to $var_value";
