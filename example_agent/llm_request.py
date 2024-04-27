import requests
import re
import difflib

def llama_request(prompt:str):
    # Define the API endpoint URL
    url = "http://localhost:11434/api/generate"

    # Set up the data payload for the POST request
    data = {
        "model": "llama3:8b",
        "prompt": prompt,
        "stream": False  # Ensure the response is not streamed
    }

    # Send the POST request to the API
    response = requests.post(url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract and print only the response content
        response_data = response.json()
        return response_data['response']
    else:
        return "Failed to generate response. Status code:", response.status_code



def find_most_similar(target, strings):
    """
    Find the index of the most similar string in a list compared to a target string.
    
    Args:
    target (str): The target string to compare against the list.
    strings (list of str): A list of strings to compare the target to.
    
    Returns:
    int: The index of the most similar string in the list.
    """
    # Check if the list is empty
    if not strings:
        return -1  # Return -1 or any appropriate value for your use case when the list is empty
    
    # Initialize the best match variables
    highest_ratio = 0.0
    best_index = 0
    
    # Compare the target string to each string in the list
    for index, string in enumerate(strings):
        # Use SequenceMatcher to calculate the similarity
        ratio = difflib.SequenceMatcher(None, target, string).ratio()
        
        # Check if the current ratio is higher than the highest found so far
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_index = index
    
    return best_index


def extract_from_first_to_last_brackets(s):
    """
    Extracts the substring from the first opening "{" to the last closing "}" in a string,
    including these brackets.

    Args:
    s (str): The string from which to extract the substring.

    Returns:
    str: The substring from the first "{" to the last "}", or an empty string if no such substring exists.
    """
    # Regular expression to find content from the first '{' to the last '}'
    match = re.search(r'\{.*\}', s)
    if match:
        return match.group(0)  # Return the matched substring including the first "{" and the last "}"
    return ""  # Return an empty string if there is no match



if __name__ == "__main__":

    # LLM Request Example
    print(llama_request("How are you?"))


    # Example usage of finding closest string:
    strings = ["hello world", "hello", "hello there", "hola"]
    target = "hello world"
    print(find_most_similar(target, strings))  # Output will be the index of "hello world"


    # Example usage of extracting substring {}
    example_string = "Here is an example {extract this part} and also {this part} too."
    print(extract_from_first_to_last_brackets(example_string))  # Output: {extract this part} and also {this part}


