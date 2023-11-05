import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Önceden eğitilmiş GPT-2 modelini ve belirli bir tokenezasyonu yükleyin
model_name = "gpt2"  # GPT-2 model adı
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Streamlit uygulama başlığı
st.title("GPT-2 Tabanlı Metin Oluşturucu")

# Kullanıcıdan giriş metni alın
user_input = st.text_area("Metin girişi:", "")

# Kullanıcı bir giriş yaptığında çalışacak işlev
if user_input:
    # Metni belirli bir maksimum uzunlukta oluşturmak için modeli kullanın
    max_length = 50  # Oluşturulan metin maksimum 50 token ile sınırlı
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    output = model.generate(input_ids, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Oluşturulan metni kullanıcıya gösterin
    st.write("Oluşturulan Metin:")
    st.write(generated_text)
