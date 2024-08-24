
import openai
import streamlit as st

# OpenAI API anahtarınızı doğru şekilde buraya yapıştırın
openai.api_key = "YOUR_OPENAI_API_KEY"


def get_movie_recommendations(genres, favorite_movies):
    """
    Kullanıcının sevdiği film türlerine ve en sevdiği filmlere göre OpenAI GPT-4'ü kullanarak film önerileri alır.

    Args:
    - genres (list): Kullanıcının sevdiği film türlerinin listesi.
    - favorite_movies (list): Kullanıcının en sevdiği filmlerin listesi.

    Returns:
    - str: Film önerilerinin tablo formatında döndüğü metin.
    """
    # Kullanıcı girdi bilgilerini birleştirip bir prompt oluşturuyoruz
    prompt = f"User loves the following genres: {', '.join(genres)}. The user's top 3 favorite movies are: {', '.join(favorite_movies)}. Based on this information, suggest 5 movies in a table format with columns: 'Film Name', 'Genre', and 'Short Description'."

    try:
        # OpenAI API çağrısı
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=500
        )
        # Yanıtı döndürme
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error fetching recommendations: {str(e)}"


def main():
    # Başlık ve giriş metni
    st.set_page_config(page_title="Film Öneri Sistemi", page_icon="🎬", layout="centered")
    st.title("🎬 Film Öneri Sistemi")
    st.write("Kendi zevkinize göre film önerileri almak için favori türlerinizi ve en sevdiğiniz 3 filmi girin!")

    # Kullanıcıdan sevdiği film türlerini ve en sevdiği 3 filmi alın
    genres = st.text_input("Sevdiğiniz film türlerini girin (örneğin: Aksiyon, Komedi, Drama):")
    favorite_movies = st.text_input("En sevdiğiniz 3 filmi girin (örneğin: Inception, The Godfather, The Dark Knight):")

    # Kullanıcıdan öneri alma butonu
    if st.button("Öneri Al"):
        if genres and favorite_movies:
            genres_list = [genre.strip() for genre in genres.split(",")]
            favorite_movies_list = [movie.strip() for movie in favorite_movies.split(",")]

            # Film önerilerini alın
            recommendations = get_movie_recommendations(genres_list, favorite_movies_list)

            # Önerileri göster
            st.markdown("### 🍿 Sizin İçin Film Önerileri:")
            st.markdown(recommendations)
        else:
            st.warning("Lütfen tüm alanları doldurun!")

    # Footer tasarımı
    st.markdown("---")
    st.markdown("📽️ Hazırlayan: [Nuray GÖNCÜ] | 2024")


if __name__ == "__main__":
    main()
