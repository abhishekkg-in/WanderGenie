from data.db import fetch_travel_knowledge_base_table, update_embeding, fetch_embedings
from embedings.embedings import create_embeding, update_vector_db_with_embeding
from response_generator.generate_response import generate_response_from_llama
from data.prompts import prompt_guardrails, prompt_travel_recomendation



"""
Creating embeding out of travel_knowledge_base data 
and updating table with embedings.
"""
def update_travel_knowledge_base_with_embedings():
    rows = fetch_travel_knowledge_base_table()
    for row in rows:
        embeding = create_embeding(row)
        update_embeding(row[0], embedding=embeding)



def chat_with_genie():

    flag = True
    print(" Chat window started ".center(100, "-"))
    while flag:
        
        print("Please select one choice from below options. ")
        print("1. Ask a trip details,")
        print("2. Quit")
        choice = int(input("Enter your choice: "))

        if choice==1:
            query = input("Ask me anything: ")

            is_safe = generate_response_from_llama(prompt_guardrails(query))

            # print("is safe --->> ", is_safe)
            if is_safe=='UNSAFE':
                print("\nGenie -> Sorry, I can not assit you with that.\n")
                print("".center(100, "-"))
                continue
            else:
                res = generate_response_from_llama(prompt_travel_recomendation(query))
                print("Genie -> ", res)
                print()
                print("".center(100, "-"))
                continue
        elif choice==2:
            flag = False
        else:
            print("Please enter a valide number.")
            continue







"""
===================================================================
=========================== MAIN FUNCTION =========================
===================================================================
"""
def main():
    # print(" Main Started ".center(100, '-'))
    print()
    chat_with_genie()


if __name__=="__main__":
    main()
