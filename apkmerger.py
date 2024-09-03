import os
from shutil import copyfileobj

# the most simple way :/
def combine_apks(output_path,first_apk,second_apk):
    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Copy the first APK (wb: write as binary)
    with open(output_path, "wb") as output_file:
        with open(first_apk, "rb") as input_file:
            copyfileobj(input_file, output_file)

    # Copy the second APK (ab: append as binary)
    with open(output_path, "ab") as output_file:
        with open(second_apk, "rb") as input_file:
            copyfileobj(input_file, output_file)

    return output_path


output_apk = input("give me the output apk path")
first_apk = input("give me the first apk path")
second_apk =  input("give me the second apk path")
output_apk = combine_apks("path/to/output/combined_apk.apk")
print(f"Combined APK saved to: {output_apk}")
