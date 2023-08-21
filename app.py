import os
import streamlit as st
import openai


# Load OpenAI credentials from environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.organization = os.environ.get("OPENAI_ORG_ID")


def main():
    """OpenAI API Demo App"""
    st.title("OpenAI API Demo")

    # Create multiline text areas with larger sizes
    text_input = st.text_area("Text to Analyze (Max 15K tokens):", height=200)
    system_input = st.text_area("System:", height=25)
    prompt_input = st.text_area("Prompt:", height=25)

    # Create a slider for temperature selection at the bottom
    temperature = st.slider("Temperature:", 0.0, 2.0, 1.0, key="temperature_slider")

    # Define a button to trigger the API call
    if st.button("Generate Output"):
        # Truncate input to 15K tokens
        text_input = text_input[:15000]

        # Call the OpenAI API using the inputs and selected temperature
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
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
