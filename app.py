import os
import streamlit as st
import openai
import tiktoken


MODEL_NAME = "gpt-3.5-turbo-16k"

# Load OpenAI credentials from environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.organization = os.environ.get("OPENAI_ORG")


def get_token_count(text: str) -> int:
    """Count the number of tokens in a text string"""
    encoder = tiktoken.encoding_for_model(MODEL_NAME)
    return len(encoder.encode(text))


def truncate_to_15k_tokens(text):
    """Truncate a text string to 15,000 tokens"""

    encoder = tiktoken.encoding_for_model(MODEL_NAME)
    tokens = encoder.encode(text)
    truncated_tokens = tokens[:15000]
    truncated_text = encoder.decode(truncated_tokens)

    return truncated_text


def main():
    """OpenAI API Demo """
    st.title("OpenAI API Demo")

    # Create multiline text areas with larger sizes
    text_input = st.text_area("Text to Analyze:", height=200)
    system_input = st.text_area("System:", height=25)
    prompt_input = st.text_area("Prompt:", height=25)

    # Create a slider for temperature selection at the bottom
    temperature = st.slider("Temperature:", 0.0, 2.0, 1.0, key="temperature_slider")

    # Define a button to trigger the API call
    if st.button("Generate Output"):
        # Count tokens in the input text
        input_token_count = get_token_count(text_input)

        # Check if input exceeds 15,000 tokens and truncate if necessary
        if input_token_count > 15000:
            st.warning("Input text exceeds 15,000 tokens. Truncating to exactly 15,000 tokens.")
            text_input = truncate_to_15k_tokens(text_input)

        # Call the OpenAI API using the inputs and selected temperature
        response = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_input},
                {"role": "user", "content": prompt_input},
                {"role": "user", "content": text_input},
            ],
            temperature=temperature,
            max_tokens=1000,  # Set output tokens to 1K
        )

        # Display the API response with line breaks
        st.subheader("API Response:")
        response_text = response["choices"][0]["message"]["content"]
        st.markdown(response_text)


if __name__ == "__main__":
    main()
