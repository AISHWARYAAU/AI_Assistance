from transformers import GPT2LMHeadModel, GPT2Tokenizer
import streamlit as st
import torch
# import yake
# from rake_nltk import Rake
# rake_nltk_var = Rake()


st.set_page_config(
    page_title="Khayal-Writing Tool App"
)
st.sidebar.success("Select an App")
#
# page_bg_img = """
# <style>
# [data-testid="stAppViewContainer"] {
# background-image url("https://images.unsplash.com/photo-1490633874781-1c63cc424610?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80");
# background-size: cover;
# }
# <style>
# """
# st.markdown(page_bg_img, unsafe_allow_html= True)
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1488415032361-b7e238421f1b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2069&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         [data-testid="stHeader"] {{
         background-color: rgba(0,0,0,0);
         }}
         [data-testid="stSidebar"] {{
         background-image: url("https://images.unsplash.com/photo-1487528742387-d53d4f12488d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1922&q=80");
         background-size: cover;
         }}
         </style>
         
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

#primaryColor="#F63366"
#backgroundColor="#FFFFFF"
#secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="Serif"




#
# base="dark"
# primaryColor="purple"
#st.title("Khayal- Writing Tool ")
st.markdown("<h1 style='text-align: center; color: white;'>Khayal- Writing Tool</h1>", unsafe_allow_html=True)
st.write("This writing tool currently has two applications within it, poem generation and text summarizer."
         " To summarize text you can use 'Summarizer from the sidebar. ")
st.header("Poem Generation")
st.markdown("This is a poem generator app. you can use it to create poems by providing text to it.")

@st.cache(allow_output_mutation=True)
def get_model():
    tokenizer = GPT2Tokenizer.from_pretrained("Silvers-145/khayal-generate")
    model = GPT2LMHeadModel.from_pretrained("Silvers-145/khayal-generate")
    return tokenizer, model

tokenizer,model = get_model()

# # load the model
# #model = GPT2LMHeadModel.from_pretrained("Silvers-145/khayal-generate")
# #tokenizer = GPT2Tokenizer.from_pretrained("Silvers-145/khayal-generate")

#model.eval()

#prompt = input("Enter the start of poem here:")
#button = st.button("Create")

prompt = st.text_input("Enter Text:",placeholder="Enter The text here")
click = st.button("Create")
if click and prompt:
    generated = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)

    sample_outputs = model.generate(
        generated,
        do_sample=True,
        top_k=50,
        max_length=300,
        top_p=0.95,
        num_return_sequences=3
    )

    for i, sample_output in enumerate(sample_outputs):
        poemm = tokenizer.decode(sample_output, skip_special_tokens=True)
    # print("{}: {}\n\n".format(i,


    st.text_area("Generated Poem:", poemm,height=250)
 #   st.snow()
    st.success("Poem Generated")



# kw_extractor = yake.KeywordExtractor()
# text = poemm
# language = "en"
# max_ngram_size = 3
# deduplication_threshold = 0.9
# numOfKeywords = 5
# custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
# keywords = custom_kw_extractor.extract_keywords(text)
# for kw in keywords:
#     print(kw)

# from rake_nltk import Rake
# rake_nltk_var = Rake()
# rake_nltk_var.extract_keywords_from_text(poemm)
# kw = rake_nltk_var.get_ranked_phrases()
# st.t