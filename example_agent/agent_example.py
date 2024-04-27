from llm_request import llama_request, find_most_similar, extract_from_first_to_last_brackets


problem = "Person: I am hungry and would like to eat some fries. \n"

prompt = "Please tell me with a simple yes or no answer if the Person is hungry."

options = ["Yes", "No"]

answer = llama_request(problem + prompt)

decision = find_most_similar(answer, options)

if decision== 0:
    print("The person is Hungry")
elif decision== 1:
    print("The person is NOT Hungry")