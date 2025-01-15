from db import fetch_travel_knowledge_base_table, update_embeding, fetch_embedings
from transformers import GPT2LMHeadModel, GPT2Tokenizer, AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from sentence_transformers import SentenceTransformer
import torch
import faiss
import numpy as np



"""
Created embeding 
"""
def create_embeding(data):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(data).tolist()
    return embedding


"""
Creating embeding out of travel_knowledge_base data 
and updating table with embedings.
"""
def update_travel_knowledge_base_with_embedings():
    rows = fetch_travel_knowledge_base_table()
    for row in rows:
        embeding = create_embeding(row)
        update_embeding(row[0], embedding=embeding)


"""
Updating vector database with embedings of travel_knowldge_base
"""
def update_vector_db_with_embeding():
    rows = fetch_embedings()
    ids = [row[0] for row in rows]
    embeddings = np.array([eval(row[1]) for row in rows]).astype('float32')
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)



"""
Setup local llm
"""
def setup_local_llm():
    model_name = "mistralai/Mistral-7B-v0.1"
    hf_token = ""

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # bnb_config = BitsAndBytesConfig(
    #     load_in_4bit=True,  # Enable 4-bit quantization
    #     # llm_int8_threshold=6.0,  # Optional: Set LLM INT8 threshold
    #     # llm_int8_has_fp16_weight=False,  # Optional: Ensure compatibility with CPU-only
    # )

    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        token=hf_token,
        # quantization_config=bnb_config,
        torch_dtype=torch.float16,
        device_map="cpu",  # Automatically handle device placement
    )
    return model, tokenizer



"""
Generate response
"""
def generate_response(user_query="places to visit in france"):

    model, tokenizer = setup_local_llm()

    system_prompt = """You are the travel agent and your name is 'WonderGenie', always start conversattion with your name,
        your task is to give recomendadtion from user query and the relavaent qury added in the context.
    """

    prompt = f"""<s>[INST] {system_prompt}
    
    User Query: {user_query} 

    Relevant Info: Eiffel Tower, Louvre Museum.

    give very sort friendle answer.
    [/INST]
    """

    # if tokenizer.pad_token is None:
    #     tokenizer.add_special_tokens({'pad_token': '[PAD]'})  # Add a padding token
    #     model.resize_token_embeddings(len(tokenizer))  # Resize model embeddings to include the new token


    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        padding=True,  # Adds padding to align token lengths
        truncation=True,  # Truncates input if too long
        max_length=512  # Adjust max length as needed
    ).to(model.device)

    # if tokenizer.pad_token_id is None:
    #     tokenizer.pad_token_id = tokenizer.eos_token_id
    # model.config.pad_token_id = tokenizer.pad_token_id

    outputs = model.generate(
        inputs.input_ids,
        attention_mask=inputs.attention_mask,  # Explicitly pass attention_mask
        max_new_tokens=50,  # Limit response length
        temperature=0.7,  # Control randomness
        top_p=0.9,  # Use nucleus sampling
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
    )

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("context -> ", prompt)
    print("res -> ", response)
    # return response


    # tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    # model = GPT2LMHeadModel.from_pretrained('gpt2')

    # user_query = "places to visit in france"

    # context = f"""
    #     You are the travel agent and your name is 'WonderGenie', always start conversattion with your name,
    #     your task is to give recomendadtion from user query and the relavaent qury added in the context
    #     -----------------------------------------------------------------
    #     User Query: {user_query}
    #     -----------------------------------------------------------------

    #     Relevant Info: Eiffel Tower, Louvre Museum.

    #     give very sort friendle answer.
    # """
    # inputs = tokenizer.encode(context, return_tensors='pt', add_special_tokens=True)
    # outputs = model.generate(
    #     inputs,
    #     max_length=500,
    #     min_length=50,
    #     do_sample=True,
    #     temperature=0.2,
    #     top_k=50,
    #     top_p=0.95,
    #     num_return_sequences=1,
    #     pad_token_id=tokenizer.pad_token_id,
    #     no_repeat_ngram_size=2
    # )
    # response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # print("Original context:", context)
    # print("\nGenerated response:", response.strip())
    # print("response -->> ",response.strip())
                                                                 


"""
===================================================================
=========================== MAIN FUNCTION =========================
===================================================================
"""
def main():

    print(" Main ".center(100, '-'))
    print()
    generate_response()


if __name__=="__main__":
    main()
