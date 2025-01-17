from data.db import fetch_travel_knowledge_base_table, update_embeding, fetch_embedings
from embedings.embedings import create_embeding, update_vector_db_with_embeding
from response_generator.generate_response import generate_response_from_llama



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
    system_prompt = """
        You are a chat assistant for trip booking agent,your name is 'Wonder Genie'.
        your have to follow below instruction strictly:
        1. Always start your answer with a polite introduction of yourself with your name.
        2. please do not respond to harmfull query.
        3. you will be given a qury for trip recomandation. along with context of trip details you have to suggest best out of it.
        4. keep your response, polite helpful, shimple and short.
    """

    flag = True
    print(" Chat window started ".center(100, "-"))
    while flag:
        
        print("Please select one choice from below options. ")
        print("1. Ask a trip details,")
        print("2. Quit")
        choice = int(input("Enter your choice: "))

        if choice==1:
            query = input("Ask me anything: ")
            prompt = f"""
            {system_prompt}
            --------------------------------------
            context: not avialable
            ---------------------------------------
            user query: {query}
            ---------------------------------------
            """
            
            res = generate_response_from_llama(prompt)
            print("Response -> ", res)
            print()
            print("".center(100, "-"))

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
